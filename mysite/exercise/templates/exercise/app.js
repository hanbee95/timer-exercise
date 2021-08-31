const confirm = function(title, msg, resvNum) {
  swal({
    title : title,
    text : msg,
    type : "warning",
    showCancelButton : true,
    confirmButtonClass : "btn-danger",
    confirmButtonText : "YES it is",
    cancelButtonText : "NO",
    closeOnConfirm : false,
    closeOnCancel : true
  }, 
  function(isConfirm) {
    if (isConfirm) {
      swal('', 'The TIMER will start now.', "success");
      let secTimer = $('section.right .timer');
      secTimer.removeClass('disNon').find('script').replaceWith('<script>exerciseTimer();</script>');
      $('section.right .h1Title').replaceWith(secTimer);
      $('section.right input[type=button]').attr('disabled','disabled');
    }
  });
}

//var alert = function(title, msg, type) {
//  swal({
//    title : title,
//    text : msg,
//    type : type,
//    timer : 500,
//    customClass : 'sweet-size',
//    showConfirmButton : false
//  });
//}

function starttimer() {
  let set = document.getElementById('set').value;
  let breakt = document.getElementById('breakt').value;
  let times = document.getElementById('times').value;
  let text = "I'm going to exercise " + times + "min with " + breakt + "min break times in " + set + "set";
  confirm ('Is this your set?', text, '');
}

window.onload = function(){

  const input = $('input:not(#button)');
  input.on('click', function () {
    let $this = $(this);
    if (!$this.val()) {
      $this.val('1');
      showCount($this.attr('id'));
    }
    $this.siblings('input:not(#button)').each(function () {
      if (!$(this).val()) {
        $(this).prev().removeClass('on');
      }
    })
    $this.prev('label').addClass('on');
  });
  
}

function showCount(event) {
  let e = document.getElementById(event).value;
  let e_id = event + '-span';
  document.getElementById(e_id).innerText = e;
}

function exerciseTimer() {
  let set = document.getElementById('set').value;
  let breakt = document.getElementById('breakt').value;
  let times = document.getElementById('times').value;
  let total = Number( times * breakt * set );
  
  let Timer = setInterval(() => {
    $('section.right .timer span').text(total);
    total--;

    if (total <= -1 ) {
      clearInterval(Timer); 
      $('section.right .timer').html('Break Time!');
      $('section.right input[type=button]').removeAttr('disabled');
    }

  }, 1000);

}