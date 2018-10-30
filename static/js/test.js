var buttons = ['button1', 'button2', 'button3'];
var modals = ['modal1', 'modal2', 'modal3'];
var closebuttons = ['close1', 'close2', 'close3'];

var map = {};
function mapping (button, modal, closebutton) {
    [button] = [modal, closebutton];
}

for (var i; i<buttons.length; i++) {
    mapping(buttons[i], modals[i], closebuttons[i]);
}
console.log(map);

