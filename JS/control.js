const screen = document.getElementById('screen');
const context = screen.getContext('2d');
let controlContext = null;
let positionX = null;
let positionY = null;
let over = false;
let over_control = null;
var controls = [];


class Control {
    /**
    * @param {number} width
    * @param {number} height
    * @param {number} x
    * @param {number} y
    */
    constructor(type, width, height, x, y) {
        this.width = width;
        this.height = height;
        this.x = x;
        this.y = y;
        this.controls = [];
        this.context = null;
        this.name = "";
        this.id = -1
        this.contextAdm = null;
        this.type = type;
    }
    get getName() {
        return this.name;
    }
    set setName(value) {
        this.name = value;
    }
    get getId() {
        return this.id;
    }
    set setId(value) {
        this.id = value;
    }
    get getType() {
        return this.type;
    }
    draw(context) {
        this.context = context;
    }
    /**
     * @param {this} contextAdm
     */
    addContextAdm(contextAdm) {

        this.contextAdm = contextAdm;
        this.controls.forEach((control) => {
            control.addContextAdm(contextAdm);
        });
        if (this.controls.length >= 1)
            contextAdm.controls.push(this);
        else
            contextAdm.controls.unshift(this);
    }
    /**
     * @param {this} contextAdm
     */
    removeContextAdm(contextAdm) {

        this.controls.forEach((control) => {
            control.removeContextAdm(contextAdm);
            this.controls.splice(this.controls.indexOf(control), 1);
        });
        contextAdm.controls.splice(contextAdm.controls.indexOf(this), 1);
    }
    /**
     * @param {Control} control
     */
    addControl(control) {

        this.controls.unshift(control);
        if (this.contextAdm !== null)
            control.addContextAdm(this.contextAdm);

    }
    /**
     * @param {Control} control
     */
    removeControl(control) {

        if (this.contextAdm !== null)
            control.removeContextAdm(this.contextAdm);
        this.controls.splice(this.controls.indexOf(control), 1);
    }
    bringToFront() {
        this.context.globalCompositeOperation = "source-over";
    }
    sendToBack() {
        this.context.globalCompositeOperation = "destination-over";
    }
    get getWidth() {
        return this.width;
    }
    set setWidth(value) {
        this.width = value;
    }
    get getHeight() {
        return this.height
    }
    set setHeight(value) {
        this.height = value;
    }
    get getX() {
        return this.x;
    }
    set setX(value) {
        this.x = value;
    }
    get getY() {
        return this.y;
    }
    set setY(value) {
        this.y = value;
    }
    /**
     * @param {Number} x
     * @param {Number} y
     */
    move(x, y) {

        const minX = 0;
        const maxX = screen.width - this.getWidth;

        const minY = 0;
        const maxY = screen.height - this.getHeight;

        const oldX = this.x;
        const oldY = this.y;

        this.x = Math.max(minX, Math.min(x, maxX));
        this.y = Math.max(minY, Math.min(y, maxY));

        this.controls.forEach((control) => {
            if (this.y > minY && this.y < maxY) {
                control.move(control.getX, control.getY + y - oldY);
            }
            if (this.x > minX && this.x < maxX) {
                control.move(control.getX + x - oldX, control.getY);
            }
        });

    }
}
class ImageControl extends Control {
    /**
    * @param {Number} width
    * @param {Number} height
    * @param {Number} x
    * @param {Number} y
    * @param {string} imagePath
    */
    constructor(width, height, x, y, imagePath) {
        super(1, width, height, x, y);
        this.image = new Image(width, height);
        this.image.src = imagePath;
    }
    /**
     * @param {any} context
     */
    draw(context) {
        super.draw(context);
        context.drawImage(this.image, this.getX, this.getY, this.getWidth, this.getHeight);
    }
    set imagePath(value) {
        this.image.src = value;
    }
}
class TextControl extends Control {

    constructor(x, y) {
        super(2, 0, 0, x, y)
        this.text = "";
        this.font = "Arial";
        this.fontSize = 8;
    }
    get getText() {
        return this.text;
    }
    set setText(value) {
        this.text = value;
    }
    get getFont() {
        return this.font;
    }
    set setFont(value) {
        this.font = value;
    }
    get getFontSize() {
        return this.fontSize;
    }
    set setFontSize(value) {
        this.fontSize = value;
    }
    draw(context) {
        super.draw(context);
        if (this.getWidth == 0) {
            this.setWidth = Math.round(context.measureText(this.getText).width);
        }
        if (this.getHeight == 0) {
            this.setHeight = this.fontSize;
        }
        context.textAlign = 'start';
        context.textBaseline = "top";
        context.font = "".concat(this.fontSize).concat("px ").concat(this.font);
        context.fillText(this.text, this.getX, this.getY, this.getWidth);
    }
}
/**
* @param {Control} control
*/
function add(control) {
    control.addContextAdm(this)
}
/**
* @param {Control} control
*/
function remove(control) {
    control.removeContextAdm(this)
}
function draw() {

    context.clearRect(0, 0, screen.width, screen.height);
    context.imageSmoothingEnabled = true;
    controls.forEach((control) => {
        control.draw(context);
    });
    requestAnimationFrame(draw);
}
/**
* @param {Event} event
*/
function getControl(event) {
    if (event.button == 0) {
        const control = controls.find(control =>
            event.offsetX >= control.getX &&
            event.offsetX <= control.getX + control.getWidth &&
            event.offsetY >= control.getY &&
            event.offsetY <= control.getY + control.getHeight);
        if (control != undefined && control != null) {
            return control;
        }
    }
    return null;
}
/**
* @param {Event} event
*/
function moveCotrol(event) {

    if (controlContext !== undefined && controlContext != null) {
        const x = Math.max(0, Math.min(event.offsetX - positionX, screen.width));
        const y = Math.max(0, Math.min(event.offsetY - positionY, screen.height));
        controlContext.move(x, y);
    }
}
/**
* @param {Event} event
*/
function mouseDown(event) {
    const control = getControl(event);
    if (control !== null) {
        controlContext = control;
        positionX = Math.abs(control.getX - event.offsetX);
        positionY = Math.abs(control.getY - event.offsetY);
        this.dispatchEvent(new CustomEvent('clicked', { detail: control }));
    }

}
/**
* @param {Event} event
*/
function mouseDoubleClick(event) {
    const control = getControl(event);
    if (control !== null) {
        this.dispatchEvent(new CustomEvent('mouseDoubleClick', { detail: control }));
    }
}
/**
* @param {Event} event
*/
function mouseUp(event) {

    if (controlContext !== null) {
        this.dispatchEvent(new CustomEvent('mouseUp', { detail: controlContext }));
    }
    clearAll(event);
}
/**
* @param {Event} event
*/
function clearAll(event) {

    controlContext = null;
    positionX = null;
    positionY = null;
}
/**
* @param {Event} event
*/
function mouseMoveOver(event) {

    const control = getControl(event);
    if (control !== null && !over && over_control === null) {

        this.dispatchEvent(new CustomEvent('mouseOver', { detail: control }));
        over_control = control;
        over = true;

    }
    else if (control === null && over && over_control !== null) {

        this.dispatchEvent(new CustomEvent('mouseLeave', { detail: over_control }));
        over_control = null;
        over = false;

    }
}

screen.addEventListener('mousedown', mouseDown);
screen.addEventListener('dblclick', mouseDoubleClick);
screen.addEventListener('mouseup', mouseUp);
screen.addEventListener('mousemove', moveCotrol);
screen.addEventListener('mouseleave', clearAll);
screen.addEventListener('mousemove', mouseMoveOver);
window.addEventListener('load', draw);


