$(document).ready(function () {
  $("#desig").click(function () {
    $("#design").toggle();
  });
});
$(document).ready(function () {
  $("#devshow").click(function () {
    $("#devhide").toggle();
  });
});
$(document).ready(function () {
  $("#productshow").click(function () {
    $("#producthide").toggle();
  });
});
$("#show1").hover(function () {
  $("#img1").toggle();
});
$("#show2").hover(function () {
  $("#img2").toggle();
});
$("#show3").hover(function () {
  $("#img3").toggle();
});
$("#show4").hover(function () {
  $("#img4").toggle();
});
$("#show5").hover(function () {
  $("#img5").toggle();
});
$("#show6").hover(function () {
  $("#img6").toggle();
});
$("#show7").hover(function () {
  $("#img7").toggle();
});
$("#show8").hover(function () {
  $("#img8").toggle();
});
function getData(){
  var name = document.getElementById("name").value;
alert(name +" we have received your message.Thank you for reaching out to us.");
}


