function print(n){

    if(n>0){
        console.log("Hello")
        n--
        print(n)
    }
}

n = 5;
print(n)