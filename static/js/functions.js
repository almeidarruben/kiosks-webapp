
/*
    Date Functions
*/
var date = new Date();
function getDayName() {
  var day = new Array(7);
  day[0]="Domingo";
  day[1]="Segunda";
  day[2]="Terça";
  day[3]="Quarta";
  day[4]="Quinta";
  day[5]="Sexta";
  day[6]="Sábado";
  var dayName = day[date.getDay()];
  $('#clock-day').empty();
  $('#clock-day').append(dayName);
}

function getFullDate() {
  var day = date.getDate();
  var month=new Array();
  month[0]="Janeiro";
  month[1]="Fevereiro";
  month[2]="Março";
  month[3]="Abril";
  month[4]="Maio";
  month[5]="Junho";
  month[6]="Julho";
  month[7]="Agosto";
  month[8]="Setembro";
  month[9]="Outubro";
  month[10]="Novembro";
  month[11]="Dezembro";
  var monthName = month[date.getMonth()];
  $('#clock-date').empty();
  $('#clock-date').append(day + " de " + monthName);
}

function getTime() {
  var time = new Date();
  var hours = (hours = time.getHours()) < 10 ? '0' + hours : hours
  var minutes = (minutes = time.getMinutes()) < 10 ? '0' + minutes : minutes
  $('#clock-time').empty();
  $('#clock-time').append(hours + ":" + minutes + "h");
}

/*
    Page Sub-nav
*/
/* Set nav buttons css class */
function setNavCss(navID, navCount) {
  var navClass;
  
  if (navCount <= 2) {
    navClass = 2;
  } else if (navCount > 2 && navCount <= 4) {
    navClass = 4;
  } else if (navCount > 4 && navCount <= 6) {
      navClass = 6;
  } else {
    // TODO: se tiver mais de 15, cria um botão do lado direito e faz slide para os outros botões que faltam
      navClass = 15;
  }
  
  $("#" + navID).addClass("page-subnav-" + navClass);
}

/* Set z-index order */
function setZindexOrder(navID) {
  var cntElements = $(navID).length;

  $(navID).css('z-index', function(i) {
      return cntElements - i;
  })
}

/* gotoBack */
function gotoBack(elementID, currentID) {
  $(".content-container").animate({"left": -($("#" + elementID).position().left)}, 600);
  $("#" + currentID).attr("id", "goto_div");
  setTimeout(function() { $("#goto_div").empty();}, 700);
  
}

function getSliderGoto(elementID) {
  $(".sidebar-content").empty();
  //$(".content-container").animate({"left": -($("#slide-" + elementID).position().left)}, 600);

  $.get("/get/sliders/1", function(data) {
    $(".sidebar-content").html("<h1>" + data[elementID].titulo + "</h1><h2>" + data[elementID].subtitulo + "</h2><h3>" + data[elementID].detalhes + "</h3><p>" + data[elementID].texto + "p</p>");
  });
}

function getMainSidebar() {
  sidebar_str = "";
  sidebar_content = document.getElementById("sidebar-get");

  $.get("/get/sliders/1", function(data) {
    sidebar_str += "<div class='sidebar-content'><h1>" + data[1].titulo + "</h1><h2>" + data[1].subtitulo + "</h2><h3>" + data[1].detalhes + "</h3><p>" + data[1].texto + "p</p></div>";

    sidebar_str += "<nav>";
    $.each(data, function(id, element) {
      sidebar_str += "<div onclick='getSliderGoto(" + id + ");'></div>";
    });
    sidebar_str += "</nav>";
    sidebar_content.innerHTML = sidebar_str;
  });
}

/***
    Ready funciton
***/
$(function() {
  setInterval(function(){
    getDayName();
    getFullDate();
    getTime();
  },500);

  getMainSidebar();
});


