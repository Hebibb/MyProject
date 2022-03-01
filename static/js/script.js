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
// Blog section button2
const birinci = document.getElementById('case1')
const ikinci = document.getElementById('case2')
const ucuncu = document.getElementById('case3')
const bir = document.getElementById('rev-cont')
const biri = bir.children[0]
const ikisi = bir.children[1]
const ucu = bir.children[2]

// mesele bilirsen nedi bu blogu men flaska salmisam bunda javascript normal isliyir? // men blog sekillerinin ustuste qoymusam elebilki bir xanaya basanda ancaq biri display block olur qalanlari none olur
birinci.addEventListener('click', () => {
    nextImage('birinci');
})

ikinci.addEventListener('click', () => {
    nextImage('ikinci');
})
ucuncu.addEventListener('click', () => {
    nextImage('ucuncu');
})

function nextImage(direction) {

    if (direction == 'birinci') {
        biri.style.width = '500px';
        biri.style.transition = 'ease 0.5s';
        ikisi.style.display = 'none';
        ucu.style.display = 'none';

    } else if (direction == 'ikinci') {
        biri.style.display = 'none';
        ikisi.style.display = 'block';
        ikisi.style.transition = 'ease 0.5s';
        ucu.style.display = 'none';
    }
    if (direction == 'ucuncu') {
        biri.style.display = 'none';
        ikisi.style.display = 'none';
        ucu.style.display = 'block';
        ucu.style.transition = 'ease 0.5s';

    }

}