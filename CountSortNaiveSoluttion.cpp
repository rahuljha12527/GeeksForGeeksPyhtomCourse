

// arr[]=[1,4,4,1,0,1]
// k=5


int CountSort(int arr,int n,int k){
   
    int count[k];

    for(int i=0;i<k;i++){
        count[i]=0;
    }

    for(int i=0;i<n;i++){
        count[arr[i]]++;
    }

    int index=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<count[j];j++){
            arr[index]=i;
            index++;
        }
    }

    return 1;

}


int arr[]=[1,4,4,1,0,1];
cout<<CountSort(arr,5,5);
//cout<<ans<<endl;


