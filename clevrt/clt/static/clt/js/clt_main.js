// document.getElementById('btn-add').onclick = function() {
//   document.getElementById('new-reminder__wrapper').classList.add('new-reminder__active');
// }

// document.getElementById('close-reminder-add').onclick = function() {
//   document.getElementById('new-reminder__wrapper').classList.remove('new-reminder__active');
// }

let gatewaysBuffer;
let sshInfoUrl = '/clt/ssh-info/';
let localhost_port;
let ajaxUrl = '/client/ajax/';

window.onload = function () {
  document.body.classList.add('loaded');
}

function checkNotifier() {
  newReminders = $('.active-notifier__reminder');
  for (let reminder of newReminders) {
    let reminderId = $(reminder).attr('data-id');
    $.ajax({
      url: ajaxUrl,
      type: 'POST',
      dataType: 'text',
      data: ({action: 'reminder-view', reminderId: reminderId})
    })
  }
}

$(document).ready(function () {
  checkNotifier();
  
  //ssh popup script
  $(document).on('click', '.last-activity__ssh', function (e) {
    let margin = 10;
    let popupSSH = $('.popup-ssh');
    popupSSH.empty();
    popupSSH.append('<p class="error-form-message"></p>');
    $('.error-form-message').hide();
    let buttonPosition = $(e.target).position();

    let client = $(e.target).attr('data-id');
    $.ajax({
      url: ajaxUrl,
      type: 'POST',
      dataType: 'text',
      data: ({ action: 'ssh-connect', client: client }),
      success: function (data) {
        let parse_data = JSON.parse(data);
        let params_gateways = '';
        let i = 0;
        gatewaysBuffer = parse_data['gateways'];
        localhost_port = parse_data['localhost_port'];
        for (let key in parse_data['gateways']) {
          i++;
          params_gateways += `gateway${i}_ip=` + parse_data['gateways'][key] + "&" + `gateway${i}_port=${key}&`
        }
        params_gateways = params_gateways.slice(0, -1);
        for (let key in parse_data['ip_list']) {
          let ip = parse_data['ip_list'][key];
          let ip_param = `ip=${ip}`;
          popupSSH.append(`<a href="${sshInfoUrl}?localhost_port=${localhost_port}&client=${client}&${ip_param}&${params_gateways}" target="blank" class="ssh__link">${ip}</a>`);
        }
        let sshPopupWidth = $('.popup-ssh').outerWidth();
        let sshPopupHeight = $('.popup-ssh').outerHeight();
        popupSSH.css('visible', 'none');
        popupSSH.css('display', 'block');
        if ((sshPopupHeight + margin) < buttonPosition.top) {
          if ((sshPopupWidth / 2) < buttonPosition.left) {
            popupSSH.offset({ top: buttonPosition.top - sshPopupHeight - margin, left: buttonPosition.left - (sshPopupWidth / 2) });
          } else {
            popupSSH.offset({ top: buttonPosition.top - sshPopupHeight - margin, left: margin });
          }
        } else {
          if ((sshPopupWidth / 2) < buttonPosition.left) {
            popupSSH.offset({ top: buttonPosition.top + $(e.target).outerHeight() + margin, left: buttonPosition.left - (sshPopupWidth / 2) });
          } else {
            popupSSH.offset({ top: buttonPosition.top + $(e.target).outerHeight() + margin, left: margin });
          }
        }
        popupSSH.fadeIn(1);
      }
    });
  });

  $(document).on('click', '.ssh__link', function (e) {
    let ip = $(e.target).text();
    console.log(ip);

    $.ajax({
      url: 'http://localhost:12632/',
      type: 'POST',
      dataType: 'text',
      data: ({ ip: JSON.stringify(ip), gateways: JSON.stringify(gatewaysBuffer), localhost_port: JSON.stringify(localhost_port) }),
      success: function (data) {
        let popupSSH = $('.popup-ssh');
        console.log(JSON.parse(data));
        popupSSH.empty();
        gatewaysBuffer = '';
        localhost_port = '';
        popupSSH.fadeOut(10);
        popupSSH.offset({ top: 0, left: 0 });
      },
      error: function () {
        $('.error-form-message').slideDown(200);
        $('.error-form-message').text('Teleport ssh не запущен');
      }
    })
  })

  $(document).mouseup(function (e) {
    let popupSSH = $('.popup-ssh');
    if (!popupSSH.is(e.target) && popupSSH.has(e.target).length === 0 && popupSSH.css('display') == 'block' && !$('.last-activity__ssh').is(e.target)) {
      popupSSH.empty()
      gatewaysBuffer = '';
      popupSSH.fadeOut(1);
      popupSSH.offset({ top: 0, left: 0 });
    }
  });

  //ssh popup script end

  $(document).on('click', '#setting-btn', function (e) {
    $('#settings-panel').toggle(50);
  });

  $(document).on('click', '.popup-button', function (e) {
    let popupName = $(e.target).attr('data-target')
    console.log(`click ${popupName}`);
    $(`#popup-${popupName}`).css('display', 'block');
  });

  $(document).on('click', '.cancel-popup', function (e) {
    let popupName = $(e.target).attr('data-target')
    console.log(`click cancel ${popupName}`);
    e.preventDefault();
    $(`#popup-${popupName}`).css('display', 'none');
  });

  $(document).on('keydown', function (e) {
    if (e.key == 'Escape') {
      //hide popup form
      $('.popup-form').css('display', 'none');
      //hide settings
      $('#settings-panel').slideUp(50);
      //destruct popup ssh
      $('.popup-ssh').empty();
      gatewaysBuffer = '';
      $('.popup-ssh').fadeOut(1);
      $('.popup-ssh').offset({ top: 0, left: 0 });
    };
  });

  $(document).on('submit', '.form-container', function (e) {
    e.preventDefault();
    let data = ({});
    let form = $(e.target);
    let resultDiv = form.find('.result-form')
    let inputs = form.find('.popup-input-field')
    for (let elem of inputs) {
      let name = $(elem).attr('name');
      let val;
      if ($(elem).attr('type') == 'checkbox') {
        val = $(elem).is(':checked')
      }
      else {
        val = $(elem).val();
      }
      console.log(`Name: ${name} | Value: ${val}`);
      data[name] = val;
    }
    $.ajax({
      url: '/clients/',
      type: 'POST',
      dataType: 'text',
      data: data,
      beforeSend: function () {
        resultDiv.removeClass('error-form-message');
        resultDiv.text('Ожидайте сохранения')
      },
      success: function (data) {
        if (data == 'Done') {
          location.reload();
        }
        else {
          resultDiv.addClass('error-form-message');
          resultDiv.text(data)
        }
      },
      error: function () {
        resultDiv.addClass('error-form-message');
        resultDiv.text('Ошибка передачи данных');
      }
    });
  });

  $(document).on('click', '.collapse', function (e) {
    console.log('collapse is working')
    let target = $(e.target).attr('data-target');
    console.log($(e.target).attr('data-target'));
    // $(e.target).next('.clients').toggle(400);
    if ($(`[data-id="${target}"`).css('display') == 'block') {
      $(`[data-id="${target}"`).slideUp(200);
    } else {
      $(`[data-id="${target}"`).slideDown(200);
    }
  });

  $('.number-input').on('keydown', function (e) {
    try {
      if (e.key.length == 1 && e.key.match(/[^0-9'".]/)) {
        return false;
      };
    } catch (e) {
      //pass
    }
  })
})