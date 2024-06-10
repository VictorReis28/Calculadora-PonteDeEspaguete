var data_id;
const modalresultado = new bootstrap.Modal('#modalresultado');

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

function addTodo(url, payload) {
  $.ajax({
    url: url,
    type: "POST",
    dataType: "json",
    data: JSON.stringify({payload: payload,}),
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    success: (data) => {
      console.log(data);
      var aux = getbarra();
    },
    error: (error) => {
      console.log(error);
    }
  });
}

$("li.ponte").click(function getbarras() {
    var data_id = $(this).attr("data-ponte");
    var aux = getbarra(data_id);
      
});



function deleteTodo(url) {
  $.ajax({
    url: url,
    type: "DELETE",
    dataType: "json",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    success: (data) => {
      console.log(data);
      var aux = getbarra();
    },
    error: (error) => {
      console.log(error);
    }
  });
}


function getbarra(idponte = null) {
  if (idponte) {
    data_id = idponte;
  }
  var url = "/get-barras/"
  var aux = data_id
  $.ajax({
      url: url,
      type: "GET",
      data: {'data_id': data_id},
      dataType: "json",
      success: (data) => {
        console.log(data);
        var barras = data.barras;
        console.log(barras);
        $("#table-barras tbody tr").remove();
        for (var i = 0; i < barras.length; i++) {
          var barra = barras[i];
          console.log(barra.nome_barra, barra.esforco_interno);
          console.log(barra.tipo);
          if (barra.tipo == "T") {
              barra.tipo = "Tração";
          } else {
              barra.tipo = "Compressão";
          }

          if (barra.n_fios_revisado == null) {
              barra.n_fios_revisado = "Não existe";
          }
          var html =  '<tr><td class="text-center align-middle">'+barra.nome_barra+
                      '</td><td class="text-center align-middle">'+barra.esforco_interno+
                      ' N</td><td class="text-center align-middle">'+barra.tipo+
                      '</td><td class="text-center align-middle">'+barra.cm+
                      ' cm</td><td class="text-center align-middle">'+barra.n_fios+
                      '</td><td class="text-center align-middle">'+barra.n_fios_revisado+
                      '</td><td class="text-center align-middle"><button class="btn btn-outline-light ml-1 mr-1" type="button" onclick="return editbarra('+data_id+')">Editar</button><button id="barra'+data_id+'" onclick="return deletebarra('+data_id+')" class="btn btn-danger ml-1 mr-1" type="button">Excluir</button></td></tr>';
          $("#table-barras tbody").append(html);

        }
      }
    });
    
}

$("#addTodoForm").on('submit', (e) => {
  // prevent page reload
  e.preventDefault();
  const url = "/todos/";
  var aux = data_id;
  // get the values from the form fields
  const formData = {
    ponte_id: aux,
    nome_barra: addTodoForm.elements["nome-barra"].value,
    cm: addTodoForm.elements["comprimento-barra"].value,
    esforco_interno: addTodoForm.elements["esforco-interno"].value,
    tipo: addTodoForm.elements["tipo-esforco"].value,
  }
  addTodo(url, formData);
  $("#addTodoForm").trigger("reset");
  });

function deletebarra(id) {
// prevent page reload
console.log("entrou!!!!!!!!")
const todoId = id
const singleTodoUrl = "/todos/"+todoId+"/";
deleteTodo(singleTodoUrl);
$("barra"+id).trigger("reset");
}

function infoponte(nomeponte) {
    var nponte = nomeponte  
    document.getElementById("selected-bridge").innerHTML = nponte;
    
}

function updateTodo(url, payload) {
  $.ajax({
    url: url,
    type: "PUT",
    dataType: "json",
    data: JSON.stringify({payload: payload,}),
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    success: (data) => {
      console.log(data);
      var aux = openresultado()
    },
    error: (error) => {
      console.log(error);
    }
  });
}

$("#updateTodoForm").on('submit', (e) => {
  // prevent page reload
  e.preventDefault();
  // get the values from the form fields
  const formData = {
    peso_linear: updateTodoForm.elements["peso-linear"].value,
  }
  const singleTodoUrl = '/todos/'+data_id+'/';
  updateTodo(singleTodoUrl, formData);
  $("#updateTodoForm").trigger("reset");
});
/* 
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
const modalnovaponte = new bootstrap.Modal('#modalnovaponte');
function opennovaponte() {
    modalnovaponte.show();
}

function closenovaponte() {
    modalnovaponte.hide();
}

function openresultado() {
    console.log("Era para abrir")
    modalresultado.show();
}
function closeresultado() {
    modalresultado.hide();
}
