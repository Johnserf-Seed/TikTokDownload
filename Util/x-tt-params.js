let CryptoJS = require("crypto-js");
getXTTP = e => {
    const t = [];
    return Object.keys(e).forEach((i => {
            const o = `${i}=${e[i]}`;
            t.push(o)
        })),
    t.push("is_encryption=1"),
    ((e, t) => {
        const i = ((e, t) => {
            let i = e.toString();
            const o = i.length;
            return o < 16 ? i = new Array(16 - o + 1).join("0") + i : o > 16 && (i = i.slice(0, 16)),
            i
        })("webapp1.0+20210628"),
        n = CryptoJS.enc.Utf8.parse(i);
        return CryptoJS.AES.encrypt(e, n, {
            iv: n,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }).toString()
    })(t.join("&"))
}

module.exports = {
    getXTTP: getXTTP
};