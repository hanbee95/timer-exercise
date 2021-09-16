window.onload = function(){

  const input = 'input:not(#button)';
  $(input).on('click', function () {
    let $this = $(this);
    if (!$this.val()) {
      $this.val('1');
      showCount($this.attr('id'));
    }
    $this.siblings(input).each(function () {
      if (!$(this).val()) {
        $(this).prev().removeClass('on');
      }
    })
    $this.prev('label').addClass('on');
  });
  
}
function showCount(event) {
  document.getElementById(event + '-span').innerText = document.getElementById(event).value;
  return event === 'set' ? set = Number(document.getElementById('set').value) : '';
}

const confirm = function(title, msg, resvNum) {
  swal({
    title : title,
    text : msg,
    type : "warning",
    showCancelButton : true,
    closeOnConfirm : false,
    confirmButtonText : "YES it is",
    cancelButtonText : "NO"
  }, 
  function(isConfirm) {
    if (isConfirm) {

      swal('', 'The TIMER will start now.', "success");

      let section = $('section');
      let sectionH1 = section.find('h1');
      sectionH1.addClass('timer');
      section.find('input[type=button]').attr('disabled','disabled');
      exerciseTimer();
    }
  });
}

function setTimer() {
  confirm ('Is this your set?', document.getElementsByClassName('result')[0].innerText, '');
}

let times;
let breakt;
let set;

function exerciseTimer() {
  times = Number(document.getElementById('times').value)*100;
  $('.timer').html('You left <br><span></span><br> seconds!');
  if (set > 0) {
    let et = setInterval(() => {
      times--;
      $('.timer span').text(times / 100);

      if (times <= 0 ) {
        clearInterval(et);
        set--;
        breakTimer();
      }
    }, 10);
  }
}

function breakTimer() {
  breakt = Number(document.getElementById('breakt').value)*100;
  if (set > 0) {
    $('.timer').html('Take a break<br><span></span><br> seconds!');
    let bt = setInterval(() => {
      breakt--;
      $('.timer span').text(breakt / 100);

      if (breakt <= 0 ) {
        clearInterval(bt);
        exerciseTimer();
      }
    }, 10);
  } else {
    $('.timer').html('Finish!');
    $('section input[type=button]').removeAttr('disabled');
    set = Number(document.getElementById('set').value);
    console.log("finish")
    console.log(Number(document.getElementById('breakt').value))
    console.log(Number(document.getElementById('set').value))
    console.log(Number(document.getElementById('times').value))
    $.ajax({
        type: "POST",
        url: '/exercise/timer',
        data: {
            "times": Number(document.getElementById('times').value),
            "breakt": Number(document.getElementById('breakt').value),
            "set": Number(document.getElementById('set').value),
        },
        dataType: "json",
        success: function (data) {
            // any process in data
            alert("successfull")
        },
        failure: function () {
            alert("failure");
        }
    });
    window.location.href="http://127.0.0.1:8000/exercise/timer";  
  }

}