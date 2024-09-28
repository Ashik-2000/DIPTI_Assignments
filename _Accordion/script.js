function showpanel(section) {
    var i, panel;
    panel = document.getElementsByClassName("panel");
    for (i = 0; i < panel.length; i++){
        panel[i].style.display = "none";
    }
    document.getElementById(section).style.display = "block"
}