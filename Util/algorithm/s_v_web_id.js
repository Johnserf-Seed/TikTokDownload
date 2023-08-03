function create_s_v_web_id() {
    var e = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split("")
        , t = e.length
        , n = (new Date).getTime().toString(36)
        , r = [];

    r[8] = r[13] = r[18] = r[23] = "_",
        r[14] = "4";
    for (var o, i = 0; i < 36; i++)
        r[i] || (o = 0 | Math.random() * t,
            r[i] = e[19 == i ? 3 & o | 8 : o]);
    return "verify_" + n + "_" + r.join("")
}

console.log(create_s_v_web_id())