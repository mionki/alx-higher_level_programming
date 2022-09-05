#!/usr/bin/node

const x = process.ArgV[2];
if (isNaN(x)){
    console.log("Missing occurrences")
}else{
    let i = 0;
    while (i < x) {
        console.log("C is fun")
        i++;
    }
}
