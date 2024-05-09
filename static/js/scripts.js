$("li.ponte").click(function () {
    var data_id = $(this).attr("data_ponte");
    var url = "./get-barras/";
    $.ajax({
        url: url,
        type: "GET",
        data: {'data_id': data_id},
        dataType: "json",
        success: (data) => {
          console.log(data);
          var barras = data.barras;
          console.log(barras);
          /*var elementoPai = document.getElementById('table-barras');
          elementoPai.append('tr');*/
          $("#table-barras tbody tr").remove();
          for (var i = 0; i < barras.length; i++) {
            var barra = barras[i];
            
            console.log(barra.tipo);
            if (barra.tipo == "T") {
                barra.tipo = "Tração";
            } else {
                barra.tipo = "Compressão";
            }
            var html =  '<tr><td class="text-center">'+barra.nome+
                        '</td><td class="text-center">'+barra.cm+
                        '</td><td class="text-center">'+barra.esforco_interno+
                        '</td><td class="text-center">'+barra.tipo+
                        '</td><td class="text-center">'+barra.n_fios+
                        '</td><td class="text-center"><button class="btn btn-danger" type="button">Excluir</button><button class="btn btn-danger" type="button">Editar</button></td></tr>';
            $("#table-barras tbody").append(html);

          }
        }
      });
      
});
function infoponte(nomeponte) {
    var nponte = nomeponte  
    document.getElementById("selected-bridge").innerHTML = nponte;
    
}
/** 
function popupnovaponte() {
    window.open("usuario/", "some-name", 'height=500,width=800,resizable=yes,scrollbars=yes');
}

const opennovaponte = document.getElementById("novaponte")
const modalnovaponte = document.getElementById("popupnovaponte")
//const closenovaponte = 

$("#novaponte").click(function(){
    $("#popupnovaponte").modal();
});
*/
const modal = new bootstrap.Modal('#popupnovaponte');
function openmodal() {
    modal.show();
}

function closemodal() {
    modal.hide();
}
