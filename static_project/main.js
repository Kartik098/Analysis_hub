$(document).ready(function(){
    console.log("Heeloo")
    $('.ui.dropdown')
        .dropdown();
        
    
   
});
console.log("Hello")
$(document).ready(function(){
   
    $('.message .close')
    .on('click', function() {
      $(this)
        .closest('.message')
        .transition('fade')
      ;
    })
  ;
  $("#modal-btn").click(function(){
    $('.ui.modal')
    .modal('show')
  ;
  })
   
});
