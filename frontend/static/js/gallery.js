(function() {
    Galleria.run('.galleria');
    Galleria.configure('imageCrop', false);
    Galleria.configure('theme', 'classic');
    Galleria.configure('width', 400);
    Galleria.configure('height', 400);
    Galleria.configure('transition', 'slide');
    Galleria.configure('thumbCrop', 'height');
    Galleria.configure('autoplay', false);
    Galleria.configure('lightbox', true);
    Galleria.on('image', function(e) {
      Galleria.log('Now viewing ' + e.imageTarget.src);
  });
})();
