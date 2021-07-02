class Device extends ImageControl {

    constructor(x, y) {
        super(48, 48, x, y, "router-red-48.png");
    }

}

class Label extends TextControl {
    constructor(x, y) {
        super(x, y)
    }
}

const device = new Device(100, 100);

this.add(device);


const label = new Label(30, 30);
label.setFontSize = 12;
label.setText= "Movimetar Objeto na Tela";
device.addControl(label);
