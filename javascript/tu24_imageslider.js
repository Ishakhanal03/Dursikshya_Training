const imgArray=['image1.jpg','image2.jpg','image3.jpg','image4.jpg']
const arrlength=imgArray.length
let i=0
const demoFunction=()=>{
    i++
    i=i%arrlength

    //0%5=0  1%5=1 2%5=2 3%5=3 4%5=4 5%5=0 then repeat the process
    document.querySelector(`img`).src=`images/${imgArray[i]}`
}
let set=setInterval(demoFunction,5000)

//addEventListener()
document.querySelector('.container .right').addEventListener('click',()=>{
    i++
    i=i%arrlength

    //0%5=0  1%5=1 2%5=2 3%5=3 4%5=4 5%5=0 then repeat the process
    document.querySelector(`img`).src=`images/${imgArray[i]}`

})
document.querySelector(".container .left").addEventListener("click", () => {
    i--;
    if (i < 0) {
        i = arrlength - 1;
    }
    document.querySelector(`img`).src = `images/${imgArray[i]}`;
});

document.querySelector('.container').addEventListener('mouseover',()=>{
    clearInterval(set)
})

document.querySelector('.container').addEventListener('mouseout',()=>{
    set=setInterval(demoFunction,5000)
})


