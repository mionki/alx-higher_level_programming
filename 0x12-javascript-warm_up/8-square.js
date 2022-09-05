#!/usr/bin/node

const N = process.argV[2];
if (isNaN(N)){
    console.log.log("Missing size")
}else{
    for(let i = 0; i < N; i++ ){
        for (let k = 0; k < N; k++){
            console.log ('X')
        }
    }
}