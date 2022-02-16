let btn = document.getElementById("btn-top");

window.onscroll = function() {
    scrollFunction();
};
window.onload = function() {
    loadinfunc()
}
yukleme = window.onload

function loadinfunc() {
    if (yukleme == true || document.body.scrollTop < 700) {
        btn.style.display = "none"
    }

}

function scrollFunction() {
    if (
        document.body.scrollTop > 700 ||
        document.documentElement.scrollTop > 700
    ) {
        btn.style.display = "block";
        btn.style.zIndex = "99"
        btn.style.transition = "0.4s"
    } else {
        btn.style.display = "none";
        btn.style.zIndex = "-1"
        btn.style.transition = "0.4s"
    }
}
// When the user clicks on the button, scroll to the top of the document
btn.addEventListener("click", backToTop)

function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}