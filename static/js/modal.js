window.onload = function() {
  //all buttons should be added here
  buttons = {
    button_ask_question: ["modal_ask_question", "close-modal-button"],
    button_send_message: ["modal_send_message", "close-modal-send-message"],
    button_send_message_bottom: [
      "modal_send_message",
      "close-modal-send-message"
    ]
  };
  //handler for buttons on main page
  window.onclick = function(event) {
    if (event.target.id != "undefined" && event.target.id in buttons) {
      // console.log(event.target.id);
      var modalshadow = document.getElementById(buttons[event.target.id][0]);
      var crossbutton = document.getElementById(buttons[event.target.id][1]);

      modalshadow.style.display = "block";

      crossbutton.onclick = function() {
        modalshadow.style.display = "none";
      };
      modalshadow.addEventListener("click", function(e) {
        if (modalshadow != e.target) {
          return;
        }
        modalshadow.style.display = "none";
      });
    }
  };
  burger = document.getElementById("burger");
  var menu_items = document.getElementsByClassName(
    "main-content__nav-menu--menu-item"
  );
  burger.onclick = function() {
    // console.log('burger');
    // var container = document.getElementsByClassName('main-content__nav-menu--container');
    for (var i = 1; i < menu_items.length; i++) {
      if (menu_items[i].style.display == "block") {
        menu_items[i].style.display = "none";
      } else {
        menu_items[i].style.display = "block";
      }
    }
    // menu_item.style.display = 'block';
  };

  //     window.onresize = function() {
  //         if (window.outerWidth>900 && menu_items[1].style.display=='none') {
  //             for (var i = 0 ; i<menu_items.length; i++) {
  //                 menu_items[i].style.display = 'block';
  //         }
  //     }
  // }
  // how to iterate through all elements of page that have an id
  // var elements = document.getElementsByTagName("*");
  // var len = elements.length;
  // for (var i=0; i<len; i++) {
  //     if (elements[i].id != "undefined") {
  //         console.log("ID is here: " + elements[i].id);
  //     }
  // }
};
