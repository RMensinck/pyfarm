window.onload = function() {
  var box = document.getElementById('draggableBox');
  var mousePosition;
  var offset = {x: 0, y: 0};

  box.addEventListener('mousedown', function(e) {
    mousePosition = {
      x: e.clientX,
      y: e.clientY
    };
    offset = {
      x: box.offsetLeft - mousePosition.x,
      y: box.offsetTop - mousePosition.y
    };
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
  });

  function onMouseMove(e) {
    mousePosition = {
      x: e.clientX,
      y: e.clientY
    };
    box.style.left = (mousePosition.x + offset.x) + 'px';
    box.style.top = (mousePosition.y + offset.y) + 'px';
  }

  function onMouseUp() {
    document.removeEventListener('mousemove', onMouseMove);
    document.removeEventListener('mouseup', onMouseUp);
  }
}