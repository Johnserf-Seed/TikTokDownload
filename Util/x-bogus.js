let MD5 = require("md5");

let Array = [ null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 10, 11, 12, 13, 14, 15 ];

// let _0x4129ad = 'Dkdpgh4ZKsQB80/Mfvw36XI1R25+WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe';
// let _0x127ecb = '=';
let _0x377d66 = "Dkdpgh4ZKsQB80/Mfvw36XI1R25-WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe=";

function _0x39ced2(l) {
    let n = [];
    for (let u = 0; u < l.length; ) {
        n.push(Array[l.charCodeAt(u++)] << 4 | Array[l.charCodeAt(u++)]);
    }
    return n;
}

function _0x1da120(l) {
    return _0x39ced2(MD5(_0x39ced2(MD5(l))));
}

function _0x2efd11(l) {
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".indexOf(l);
}

function _0x2d9dba(l) {
    var n, u, e, t, r, o = "";
    for (n = 0; n < l.length - 3; n += 4) {
        u = _0x2efd11(l.charAt(n)), e = _0x2efd11(l.charAt(n + 1)), t = _0x2efd11(l.charAt(n + 2)), 
        r = _0x2efd11(l.charAt(n + 3)), o += String.fromCharCode(u << 2 | e >>> 4), "=" !== l.charAt(n + 2) && (o += String.fromCharCode(e << 4 & 240 | t >>> 2 & 15)), 
        "=" !== l.charAt(n + 3) && (o += String.fromCharCode(t << 6 & 192 | r));
    }
    return o;
}

function _0x24e7c9() {
    var l = "";
    try {
        window.sessionStorage && (l = window.sessionStorage.getItem("_byted_param_sw")), 
        l && !window.localStorage || (l = window.localStorage.getItem("_byted_param_sw"));
    } catch (l) {}
    if (l) {
        try {
            var n = _0x3459bb(_0x2d9dba(l.slice(8)), l.slice(0, 8));
            if ("on" === n) {
                return !0;
            }
            if ("off" === n) {
                return !1;
            }
        } catch (l) {}
    }
    return !1;
}

function _0x4d54ed(l) {
    try {
        return window.localStorage ? window.localStorage.getItem(l) : null;
    } catch (l) {
        return null;
    }
}

function _0x478bb3(l, n, u) {
    let e = (255 & l) << 16;
    let t = (255 & n) << 8;
    let r = e | t | u;
    return _0x377d66[(16515072 & r) >> 18] + _0x377d66[(258048 & r) >> 12] + _0x377d66[(4032 & r) >> 6] + _0x377d66[63 & r];
}

function _0x481826(l) {
    void 0 !== l && "" != l && (_0x402a35.ttwid = l);
}

function _0x37f15d() {
    var l = _0x4d54ed("xmst");
    return l || "";
}

function _0x330d11(l, n, u, e, t, r, o, d, a, c, i, f, x, _, h, g, C, s, p) {
    let w = new Uint8Array(19);
    w[0] = l, w[1] = i, w[2] = n, w[3] = f, w[4] = u, w[5] = x, w[6] = e, w[7] = _, 
    w[8] = t, w[9] = h, w[10] = r, w[11] = g, w[12] = o, w[13] = C, w[14] = d, w[15] = s, 
    w[16] = a, w[17] = p, w[18] = c;
    return String.fromCharCode.apply(null, w);
}

function _0x330d112(l, n) {
    let u, e = [], t = 0, r = "", o = 0, d = 0, a = 0;
    for (let l = 0; l < 256; l++) {
        e[l] = l;
    }
    for (;o < 256; o++) {
        t = (t + e[o] + l.charCodeAt(o % l.length)) % 256, u = e[o], e[o] = e[t], e[t] = u;
    }
    t = 0;
    for (;d < n.length; d++) {
        t = (t + e[a = (a + 1) % 256]) % 256, u = e[a], e[a] = e[t], e[t] = u, r += String.fromCharCode(n.charCodeAt(d) ^ e[(e[a] + e[t]) % 256]);
    }
    return r;
}

function _0x33baa6(l, n, u) {
    return String.fromCharCode(l) + String.fromCharCode(n) + u;
}

function getXB(l) {
	// douyin
    let n = _0x39ced2(MD5("d4+pTKoNjJFb5tMtAC3XB9XrDDxlig1kjbh32u+x5YcwWb/me2pvLTh6ZdBVN5skEeIaOYNixbnFK6wyJdl/Lcy9CDAcpXLLQc3QFKIDQ3KkQYie3n258eLS1YFUqFLDjn7dqCRp1jjoORamU2SV"));
    // douyin & tiktok
	let u = _0x39ced2(MD5(_0x39ced2("d41d8cd98f00b204e9800998ecf8427e")));
    let e = _0x1da120(l), t = new Date().getTime() / 1e3, r = 536919696, o = [], d = [], a = "";
    let c = [ 64, .00390625, 1, 8, e[14], e[15], u[14], u[15], n[14], n[15], t >> 24 & 255, t >> 16 & 255, t >> 8 & 255, t >> 0 & 255, r >> 24 & 255, r >> 16 & 255, r >> 8 & 255, r >> 0 & 255 ];
    c.push(c.reduce(function(l, n) {
        return l ^ n;
    }));
    for (let l = 0; l < c.length; l += 2) {
        o.push(c[l]);
        d.push(c[l + 1]);
    }
	//unescape('%FF')
    let i = _0x33baa6.apply(null, [ 2, 255, _0x330d112.apply(null, [String.fromCharCode(255), _0x330d11.apply(null, o.concat(d).slice(0, 19)) ]) ]);
    for (let l = 0; l < i.length; ) {
        a += _0x478bb3(i.charCodeAt(l++), i.charCodeAt(l++), i.charCodeAt(l++));
    }
    return a;
}

_0x180b4c = _0x37f15d();

module.exports = {
    getXB: getXB
};