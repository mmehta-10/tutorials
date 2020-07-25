package main

import (
	"fmt"
	"log"
	"os" //declared but not used, hence preceded with _

	// corev1 "k8s.io/api/core/v1"
	"k8s.io/apimachinery/pkg/apis/meta/v1"

	"k8s.io/apimachinery/pkg/util/runtime"

	// "k8s.io/client-go@kubernetes-1.15.11"
	"k8s.io/client-go/informers"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/cache"
	"k8s.io/client-go/tools/clientcmd"
)

const (
	// K8S_LABEL_AWS_REGION is the key name to retrieve the region from a
	// Node that runs on AWS.
	K8S_LABEL_AWS_REGION = "failure-domain.beta.kubernetes.io/region"
)

func main() {
	log.Print("Shared Informer app started")
	kubeconfig := os.Getenv("HOME") + "/.kube/config"
	config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
	if err != nil {
		log.Panic(err.Error())
	}
	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		log.Panic(err.Error())
	}

	factory := informers.NewSharedInformerFactory(clientset, 0)
	// informer := factory.Core().V1().Nodes().Informer()
	informer := factory.Core().V1().Pods().Informer()
	stopper := make(chan struct{})
	defer close(stopper)

	defer runtime.HandleCrash()
	informer.AddEventHandler(cache.ResourceEventHandlerFuncs{
		AddFunc: onAdd,
		UpdateFunc: func(oldObj, newObj interface{}) {
            log.Printf("pod changed: %s \n", newObj.(v1.Object).GetName())
        },
		
	})
	go informer.Run(stopper)
	if !cache.WaitForCacheSync(stopper, informer.HasSynced) {
		runtime.HandleError(fmt.Errorf("Timed out waiting for caches to sync"))
		return
	}
	<-stopper
}

// onAdd is the function executed when the kubernetes informer notified the
// presence of a new kubernetes node in the cluster
func onAdd(obj interface{}) {
	// Cast the obj as node
	// node := obj.(*corev1.Node)
	// _, ok := node.GetLabels()[K8S_LABEL_AWS_REGION]
	// if ok {
	// 	fmt.Printf("It has the label!")
	// }

	// Source: https://www.firehydrant.io/blog/stay-informed-with-kubernetes-informers/
    // "k8s.io/apimachinery/pkg/apis/meta/v1" provides an Object
    // interface that allows us to get metadata easily
    mObj := obj.(v1.Object)
    log.Printf("New Pod Added to Store: %s", mObj.GetName())
	
}

