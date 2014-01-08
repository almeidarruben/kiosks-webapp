
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
  $('#clock-day').append(dayName);
}
getDayName();

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
  $('#clock-date').append(day + " de " + monthName);
}
getFullDate();
function getTime() {
  var time = new Date();
  var hours = (hours = time.getHours()) < 10 ? '0' + hours : hours
  var minutes = (minutes = time.getMinutes()) < 10 ? '0' + minutes : minutes
  $('#clock-time').empty();
  $('#clock-time').append(hours + ":" + minutes + "h");
}
setInterval(function(){getTime()},500);

/*
    Page Sub-nav
*/
/* Set z-index order */
function setZindexOrder(navID) {
  var cntElements = $(navID).length;

  $(navID).css('z-index', function(i) {
      return cntElements - i;
  })
}

/* Set nav buttons css class */
function setNavCss(navID, navCount) {
  var ID = document.getElementById(navID);
  var navClass;
  
  if (navCount <= 2) {
    navClass = 2;
  } else if (navCount > 2 && navCount <= 4) {
    navClass = 4;
  } else if (navCount > 4 && navCount <= 6) {
      navClass = 6;
  } else {
      navClass = 15;
  }
  
  $(ID).addClass("page-subnav-" + navClass);
}
