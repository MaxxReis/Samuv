// DRAWING CANVAS
var canvas;
var result;
var canvasWidth = 500;
var canvasHeight = 500;
var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();
var paint = false;
var paintWidth = 5;
var img = new Image();
var currentContext;
var fg_data_copy;
var offsetWithSideBarX = 274;
var offsetWithSideBarY = 119;
var offsetWithoutSideBarX = 23;
var offsetWithoutSideBarY = 119;

// CANVAS HANDLER
function prepareCanvas() {
    currentContext = document.getElementById("foreground_canvas").getContext("2d");

    fg_canvas = document.getElementById("foreground_canvas");
    currentContext = fg_canvas.getContext("2d");
    clearCurrentContext();

    setMouseEvents();
    setCallbacks();
}

function setMouseEvents() {
    $('#foreground_canvas').mousedown(function(e){
      var mouseX = e.pageX - this.offsetLeft;
      var mouseY = e.pageY - this.offsetTop;

      paint = true;
      addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
      redraw();
    });

    $('#foreground_canvas').mousemove(function(e){
      if(paint){
        addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
        redraw();
      }
    });

    $('#foreground_canvas').mouseup(function(e){
      paint = false;
    });

    $('#foreground_canvas').mouseleave(function(e){
      paint = false;
    });

    function addClick(x, y, dragging){
      if(document.body.clientWidth >= 902){
        clickX.push(x - offsetWithSideBarX);
        clickY.push(y - offsetWithSideBarY);
      } else {
        clickX.push(x - offsetWithoutSideBarX);
        clickY.push(y - offsetWithoutSideBarY);
      }
      clickDrag.push(dragging);
    }

    function redraw(){
      currentContext.clearRect(0, 0, canvasWidth, canvasHeight);
      currentContext.strokeStyle = "#FFF";
      currentContext.lineJoin = "round";
      currentContext.lineWidth = paintWidth;

      for(var i=0; i < clickX.length; i++) {
        currentContext.beginPath();
        if(clickDrag[i] && i){
          currentContext.moveTo(clickX[i-1], clickY[i-1]);
         }else{
           currentContext.moveTo(clickX[i]-1, clickY[i]);
         }
         currentContext.lineTo(clickX[i], clickY[i]);
         currentContext.closePath();
         currentContext.stroke();
      }
    }
}

function clearCanvas(){
    clickX = new Array();
    clickY = new Array();
    clickDrag = new Array();

    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = "transparent";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    var fg_canvas = document.getElementById('foreground_canvas');
    var fg_ctx = canvas.getContext('2d');
    fg_ctx.fillStyle = "transparent";
    fg_ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    fg_canvas.width = canvasWidth;
    fg_canvas.height = canvasHeight;

    if(img && scaleFactor){
        ctx.drawImage(img, 0, 0, img.width * scaleFactor, img.height * scaleFactor);
    }
    else {
        canvas.setAttribute('width', 0);
        canvas.setAttribute('height', 0);
    }
}

function clearCurrentContext(){
    clickX = new Array();
    clickY = new Array();
    clickDrag = new Array();

    ctx = currentContext;
    ctx.fillStyle = "transparent";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
}

function offset(el) {
    var rect = el.getBoundingClientRect(),
    scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
    scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    return { top: rect.top + scrollTop, left: rect.left + scrollLeft }
}

function aumentarPincel() {
    if(paintWidth < 20) {
        paintWidth += 5;
    }
}

function diminuirPincel() {
    if(paintWidth < 20) {
        paintWidth += 5;
    }
}
// END CANVAS HANDLER

// FILE HANDLER
var scaleFactor;

function setCallbacks() {
  var inputElement = document.getElementById("my-file");
  canvas = document.getElementById("canvas");
}

// SERVER COMMUNICATION
function enviarParaSegmentacao(idAtendimento) {
    var url = "{% url 'api_rest:segmentar_imagem' %}/" + idAtendimento;
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        var reader = new FileReader();
        reader.onloadend = function() {
            callback(reader.result);
        }
        reader.readAsDataURL(xhr.response);
    };
    xhr.open('GET', url);
    xhr.responseType = 'blob';
    xhr.send();

    function callback(data){
        var image = new Image();
        image.src = data;
        resultImage = document.getElementById("resultImage");
        if(!resultImage.src){
            resultImage.src = data.src;
        }
        document.body.appendChild(image);
    }
}
// END SERVER COMMUNICATION
