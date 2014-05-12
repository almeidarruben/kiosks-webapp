
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

function getMonthName(monthID) {
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
  return month[monthID-1];
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

/* Back & Forward Buttons --- to delete --- */
function addBackForwardBtn(btnName, elementID, currentID) {
  if (btnName == "forward") {
    $("#dynamic-content").append("<div class='page-" + btnName + "-button' onclick=\"gotoForward(" + elementID + ","+ currentID +"');\"></div>");
  } else {
    $("#dynamic-content").append("<div class='page-" + btnName + "-button' onclick=\"gotoBackSub(" + elementID + ","+ currentID +"');\"></div>");
  }
}

function gotoBack(elementID, currentID) {
  $(".content-container").animate({"left": -($("#" + elementID).position().left)}, 600);
  $("#" + currentID).attr("id", "hold_div");
  setTimeout(function() { 
    $("#hold_div").remove();
  }, 700); 
}

function gotoBackSub(elementID, currentID) {
  $(".content-container").animate({"left": -($("#" + elementID).position().left)}, 600);
}

function gotoForward(elementID, currentID) {
  $(".content-container").animate({"left": -($("#" + elementID).position().left)}, 600);
  setTimeout(function() {
    addBackForwardBtn("back","'" + currentID + "'", "'" + elementID);
    $(".page-back-button").css({
      'position': 'absolute',
      'left': '1044px'});
  }, 700); 
}

function gotoForwardSub(elementID, currentID, navCnt) {
  $(".content-container").animate({"left": -($("#" + elementID).position().left)}, 600);
  setTimeout(function() {
    addBackForwardBtn("back","'" + currentID + "'", "'" + elementID);
    var leftPosition = 1044;
    if (navCnt == 0) {
      leftPosition *= 2;
      $(".page-back-button").css({
        'position': 'absolute',
        'left': leftPosition});  
    } else {
      leftPosition *= (2 + navCnt);
      $(".page-back-button").css({
        'position': 'absolute',
        'left': leftPosition});
    }
  }, 700); 
}

function getSliderGoto(elementID) {
  $(".sidebar-content").empty();

  $.get("/get/sliders/1", function(data) {
    $(".sidebar-content").html("<h1>" + data[elementID].titulo + "</h1><h2>" + data[elementID].subtitulo + "</h2><h3>" + data[elementID].detalhes + "</h3><p>" + data[elementID].texto + "p</p>");
  });

  $(".content-container").animate({"left": -($("#slide-" + elementID).position().left)}, 600);
}

function getMainSidebar() {
  sidebar_str = "";
  sidebar_content = document.getElementById("sidebar-container");

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

function getBottoms(listagem, pagina_pk, titulo, tipo, slug, returnDivID) {
  bottoms_str = "";
  if(!listagem){
    var cnt = 1;
    $.get("/get/bottoms", function(data) {
      $.each(data.bottoms, function(id, e) {
        if (cnt < data.tamanho) {
          bottoms_str += "<div class='bottom-0'>";
        } else {
          bottoms_str += "<div class='news'>";  
        }
        bottoms_str += "<h1>" + id + "</h1><ul>"

        $.each(e, function(eid, element) {
          if (eid != "peso") {
            bottoms_str += "<li>";
            if ((element.data != "None") && (element.data != undefined)) {
              var date_str = element.data.split("-");
              bottoms_str += "<div class='topic-date'><div class='topic-day'>" + date_str[2] + "</div><div class='topic-month'>" + getMonthName(date_str[1]).substring(0,3) + "</div></div>";
            }
            bottoms_str += "<h2>" + element.titulo + "</h2><p>" + element.descricao + "</p></li>";
          }
        });
        bottoms_str += "</ul></div>";
        cnt ++;
      });
      $(".footer-info").html(bottoms_str);
    });
  }
  else {
    if(tipo == "prot_pub"){
      var url = "/get/unidades/" + pagina_pk;
      var footer_div = $("footer");
      $.get(url, function(data) {
        var bottoms_str = "";
        if(!jQuery.isEmptyObject(data)){
          bottoms_str = "<div class=\"footer-search\"><h1>Pesquisa</h1><select>";
          $.each(data, function(id, e) {
            bottoms_str += "<option value=unidade-" + e + ">" + e + "</option>";
          });
          bottoms_str += "</select><div class=\"footer-search-button\" onclick=\"filterUnidades(" + pagina_pk + ")\"><a>OK</a></div></div>";
        }
        footer_div.html(bottoms_str);
      });
    } else {
      var url = "/get/categorias/" + pagina_pk;
      var footer_div = $("footer");
      var bottoms_str = "<div class=\"footer-search\"><h1>Pesquisa</h1><select>";
      $.get(url, function(data) {
        $.each(data, function(id, e) {
          bottoms_str += "<option value=categoria-" + id + ">" + e + "</option>";
        });
        bottoms_str += "</select><div class=\"footer-search-button\" onclick=\"filterCategorias(" + pagina_pk + ", '" + titulo + "', '" + tipo + "', '" + slug + "', '" + returnDivID + "')\"><a>OK</a></div></div>";
        footer_div.html(bottoms_str);
      });
    }
  }
}

function filterCategorias(pagina_pk, titulo, tipo, slug, returnDivID) {
  var categoria_pk = $(".footer-search").find(":selected").val();
  var url = "/get/items/" + pagina_pk + "?categoria=" + categoria_pk.substring(10);
  slug = "#"+slug;
  var formatedSlug = slug.replace("/", "-");
  var divID = document.getElementById(formatedSlug);
  $.get(url, function(data) {
      if(returnDivID == null)
        str = "<div id=" + slug + " class='page'><div class='page-back-button' onclick=\"gotoBack('" + returnDivID + "','"+ formatedSlug +"');\"></div><div class='list-wrapper'><h1>" + titulo + "</h1><div class='list-container'>";
      else
        str = "<div id=" + slug + " class='page'><div class='list-wrapper'><h1>" + titulo + "</h1><div class='list-container'>";

        $.each(data, function(category, element) {
          str += "<div class='list-item-category'><h1>" + category + "</h1>";
          $.each(element, function(index, e) {
            str += "<div class='list-item'><h2>" + e.titulo +"</h2><div class='list-item-parag-wrapper'><p class='list-item-parag-bold'>Candidatura:</p><p>"+ e.candidatura +"</p></div>";

                      str += "<div class='list-item-parag-wrapper'><p class='list-item-parag-bold'>Fonte de Financiamento:</p><p>" + e.financiamento + "</p></div>";

                      str += "<div class='list-item-parag-wrapper'><p class='list-item-parag-bold'>Unidade:</p><p>" + e.unidade + "</p></div>";

                      str += "<div class='list-item-parag-wrapper'><p class='list-item-parag-bold'>Responsável:</p><p>" + e.responsavel + "</p></div></div>";
                  });
        });
        str += "</div></div>";
        divID.innerHTML = str;
    });
}


function filterUnidades(pagina_pk) {
  var unidade_pk = $(".footer-search").find(":selected").val();
  var url = "/get/items/" + pagina_pk + "?unidade=" + unidade_pk.substring(8);
  var divID = $(".protocol-content");
  $.get(url, function(data) {
      if(data) {
          str = "";
          $.each(data, function(protocol, element) {
            str += "<div class='protocol-topic'><h1>" + element.titulo + "</h1><p>" + element.objectivos + "</p><div class='protocol-subtitle'><h2>Assinatura:</h2><p>" + element.assinatura + "</p><h2>Termo:</h2><p>" + element.termo + "</p></div><div class='protocol-subtitle'><h2>Unidade:</h2><p>" + element.unidade + "</p></div></div>"
          });
          divID.html(str);
          console.log(divID.innerHTML);
      }
    });
}
