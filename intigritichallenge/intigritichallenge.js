const params = new URLSearchParams(window.location.search);
const url = params.get("url");
if (!isValidUrl(url)) {
    throw "Not a valid URL";
}
const size = params.get("size") || 400;
const code = new QRCode({
    content: params.get("url"),
    color: "#ef3257",
    width: parseInt(size),
    height: parseInt(size)
});
const svg = code.svg();
const container = document.getElementById("qr");
container.onclick = scanCode;
container.setAttribute("style", `width:${size}px;`);
container.insertAdjacentHTML('beforeend', svg);

function isValidUrl(url) {
    return /^http(s)?:\/\//.test(url.toLowerCase());
}

function scanCode() {
    html2canvas(document.querySelector("#qr"), { scale: devicePixelRatio, width: parseInt(size), height: parseInt(size) }).then(canvas => {
        document.body.appendChild(canvas);
        var c = document.getElementsByTagName("canvas")[0];
        var ctx = c.getContext("2d");
        var imageData = ctx.getImageData(0, 0, parseInt(size) * devicePixelRatio, parseInt(size) * devicePixelRatio);
        var code = jsQR(imageData.data, parseInt(size) * devicePixelRatio, parseInt(size) * devicePixelRatio);
        c.remove();
        if (code) {
            window.open(code.data);
        } else {
            throw "Could not read QR code.";
        }
    });
}