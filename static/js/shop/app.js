let preloaderBtn = document.querySelector(".preloader-text-enter")
let story = document.querySelector("#story")
let canv = document.querySelector("#canvas")
let main = document.querySelector("#main")
let viewModes = document.querySelector("#view-modes")
let bgVideo = document.getElementById("bg_video")
const contain = document.body.classList.contains("end")
let body = document.querySelector("body")

console.log(contain)
// body.addEventListener('click', function(){
//     story.style.display = "none";
//     canv.style.display = "none";
//     main.style.display = "none";
//     viewModes.style.display = "none";
// })
var observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        console.log(mutation.type);
    });    
});
var config = { childList: true, }
 