function _h(i, s) {
    for (var l = 0; l < s.length; l++) {
        const u = s[l];
        if (typeof u != "string" && !Array.isArray(u)) {
            for (const d in u)
                if (d !== "default" && !(d in i)) {
                    const f = Object.getOwnPropertyDescriptor(u, d);
                    f && Object.defineProperty(i, d, f.get ? f : {
                        enumerable: !0,
                        get: () => u[d]
                    })
                }
        }
    }
    return Object.freeze(Object.defineProperty(i, Symbol.toStringTag, {
        value: "Module"
    }))
}
(function() {
    const s = document.createElement("link").relList;
    if (s && s.supports && s.supports("modulepreload"))
        return;
    for (const d of document.querySelectorAll('link[rel="modulepreload"]'))
        u(d);
    new MutationObserver(d => {
        for (const f of d)
            if (f.type === "childList")
                for (const h of f.addedNodes)
                    h.tagName === "LINK" && h.rel === "modulepreload" && u(h)
    }
    ).observe(document, {
        childList: !0,
        subtree: !0
    });
    function l(d) {
        const f = {};
        return d.integrity && (f.integrity = d.integrity),
        d.referrerPolicy && (f.referrerPolicy = d.referrerPolicy),
        d.crossOrigin === "use-credentials" ? f.credentials = "include" : d.crossOrigin === "anonymous" ? f.credentials = "omit" : f.credentials = "same-origin",
        f
    }
    function u(d) {
        if (d.ep)
            return;
        d.ep = !0;
        const f = l(d);
        fetch(d.href, f)
    }
}
)();
function Nd(i) {
    return i && i.__esModule && Object.prototype.hasOwnProperty.call(i, "default") ? i.default : i
}
var ma = {
    exports: {}
}
  , Vr = {}
  , ga = {
    exports: {}
}
  , ie = {};
/**
 * @license React
 * react.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Dc;
function Rh() {
    if (Dc)
        return ie;
    Dc = 1;
    var i = Symbol.for("react.element")
      , s = Symbol.for("react.portal")
      , l = Symbol.for("react.fragment")
      , u = Symbol.for("react.strict_mode")
      , d = Symbol.for("react.profiler")
      , f = Symbol.for("react.provider")
      , h = Symbol.for("react.context")
      , g = Symbol.for("react.forward_ref")
      , m = Symbol.for("react.suspense")
      , x = Symbol.for("react.memo")
      , b = Symbol.for("react.lazy")
      , w = Symbol.iterator;
    function v(k) {
        return k === null || typeof k != "object" ? null : (k = w && k[w] || k["@@iterator"],
        typeof k == "function" ? k : null)
    }
    var R = {
        isMounted: function() {
            return !1
        },
        enqueueForceUpdate: function() {},
        enqueueReplaceState: function() {},
        enqueueSetState: function() {}
    }
      , E = Object.assign
      , _ = {};
    function P(k, T, le) {
        this.props = k,
        this.context = T,
        this.refs = _,
        this.updater = le || R
    }
    P.prototype.isReactComponent = {},
    P.prototype.setState = function(k, T) {
        if (typeof k != "object" && typeof k != "function" && k != null)
            throw Error("setState(...): takes an object of state variables to update or a function which returns an object of state variables.");
        this.updater.enqueueSetState(this, k, T, "setState")
    }
    ,
    P.prototype.forceUpdate = function(k) {
        this.updater.enqueueForceUpdate(this, k, "forceUpdate")
    }
    ;
    function $() {}
    $.prototype = P.prototype;
    function I(k, T, le) {
        this.props = k,
        this.context = T,
        this.refs = _,
        this.updater = le || R
    }
    var V = I.prototype = new $;
    V.constructor = I,
    E(V, P.prototype),
    V.isPureReactComponent = !0;
    var H = Array.isArray
      , se = Object.prototype.hasOwnProperty
      , K = {
        current: null
    }
      , te = {
        key: !0,
        ref: !0,
        __self: !0,
        __source: !0
    };
    function ee(k, T, le) {
        var ae, fe = {}, pe = null, ve = null;
        if (T != null)
            for (ae in T.ref !== void 0 && (ve = T.ref),
            T.key !== void 0 && (pe = "" + T.key),
            T)
                se.call(T, ae) && !te.hasOwnProperty(ae) && (fe[ae] = T[ae]);
        var ge = arguments.length - 2;
        if (ge === 1)
            fe.children = le;
        else if (1 < ge) {
            for (var ke = Array(ge), st = 0; st < ge; st++)
                ke[st] = arguments[st + 2];
            fe.children = ke
        }
        if (k && k.defaultProps)
            for (ae in ge = k.defaultProps,
            ge)
                fe[ae] === void 0 && (fe[ae] = ge[ae]);
        return {
            $$typeof: i,
            type: k,
            key: pe,
            ref: ve,
            props: fe,
            _owner: K.current
        }
    }
    function J(k, T) {
        return {
            $$typeof: i,
            type: k.type,
            key: T,
            ref: k.ref,
            props: k.props,
            _owner: k._owner
        }
    }
    function ue(k) {
        return typeof k == "object" && k !== null && k.$$typeof === i
    }
    function ce(k) {
        var T = {
            "=": "=0",
            ":": "=2"
        };
        return "$" + k.replace(/[=:]/g, function(le) {
            return T[le]
        })
    }
    var me = /\/+/g;
    function De(k, T) {
        return typeof k == "object" && k !== null && k.key != null ? ce("" + k.key) : T.toString(36)
    }
    function je(k, T, le, ae, fe) {
        var pe = typeof k;
        (pe === "undefined" || pe === "boolean") && (k = null);
        var ve = !1;
        if (k === null)
            ve = !0;
        else
            switch (pe) {
            case "string":
            case "number":
                ve = !0;
                break;
            case "object":
                switch (k.$$typeof) {
                case i:
                case s:
                    ve = !0
                }
            }
        if (ve)
            return ve = k,
            fe = fe(ve),
            k = ae === "" ? "." + De(ve, 0) : ae,
            H(fe) ? (le = "",
            k != null && (le = k.replace(me, "$&/") + "/"),
            je(fe, T, le, "", function(st) {
                return st
            })) : fe != null && (ue(fe) && (fe = J(fe, le + (!fe.key || ve && ve.key === fe.key ? "" : ("" + fe.key).replace(me, "$&/") + "/") + k)),
            T.push(fe)),
            1;
        if (ve = 0,
        ae = ae === "" ? "." : ae + ":",
        H(k))
            for (var ge = 0; ge < k.length; ge++) {
                pe = k[ge];
                var ke = ae + De(pe, ge);
                ve += je(pe, T, le, ke, fe)
            }
        else if (ke = v(k),
        typeof ke == "function")
            for (k = ke.call(k),
            ge = 0; !(pe = k.next()).done; )
                pe = pe.value,
                ke = ae + De(pe, ge++),
                ve += je(pe, T, le, ke, fe);
        else if (pe === "object")
            throw T = String(k),
            Error("Objects are not valid as a React child (found: " + (T === "[object Object]" ? "object with keys {" + Object.keys(k).join(", ") + "}" : T) + "). If you meant to render a collection of children, use an array instead.");
        return ve
    }
    function Pe(k, T, le) {
        if (k == null)
            return k;
        var ae = []
          , fe = 0;
        return je(k, ae, "", "", function(pe) {
            return T.call(le, pe, fe++)
        }),
        ae
    }
    function Oe(k) {
        if (k._status === -1) {
            var T = k._result;
            T = T(),
            T.then(function(le) {
                (k._status === 0 || k._status === -1) && (k._status = 1,
                k._result = le)
            }, function(le) {
                (k._status === 0 || k._status === -1) && (k._status = 2,
                k._result = le)
            }),
            k._status === -1 && (k._status = 0,
            k._result = T)
        }
        if (k._status === 1)
            return k._result.default;
        throw k._result
    }
    var ye = {
        current: null
    }
      , F = {
        transition: null
    }
      , Y = {
        ReactCurrentDispatcher: ye,
        ReactCurrentBatchConfig: F,
        ReactCurrentOwner: K
    };
    function U() {
        throw Error("act(...) is not supported in production builds of React.")
    }
    return ie.Children = {
        map: Pe,
        forEach: function(k, T, le) {
            Pe(k, function() {
                T.apply(this, arguments)
            }, le)
        },
        count: function(k) {
            var T = 0;
            return Pe(k, function() {
                T++
            }),
            T
        },
        toArray: function(k) {
            return Pe(k, function(T) {
                return T
            }) || []
        },
        only: function(k) {
            if (!ue(k))
                throw Error("React.Children.only expected to receive a single React element child.");
            return k
        }
    },
    ie.Component = P,
    ie.Fragment = l,
    ie.Profiler = d,
    ie.PureComponent = I,
    ie.StrictMode = u,
    ie.Suspense = m,
    ie.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED = Y,
    ie.act = U,
    ie.cloneElement = function(k, T, le) {
        if (k == null)
            throw Error("React.cloneElement(...): The argument must be a React element, but you passed " + k + ".");
        var ae = E({}, k.props)
          , fe = k.key
          , pe = k.ref
          , ve = k._owner;
        if (T != null) {
            if (T.ref !== void 0 && (pe = T.ref,
            ve = K.current),
            T.key !== void 0 && (fe = "" + T.key),
            k.type && k.type.defaultProps)
                var ge = k.type.defaultProps;
            for (ke in T)
                se.call(T, ke) && !te.hasOwnProperty(ke) && (ae[ke] = T[ke] === void 0 && ge !== void 0 ? ge[ke] : T[ke])
        }
        var ke = arguments.length - 2;
        if (ke === 1)
            ae.children = le;
        else if (1 < ke) {
            ge = Array(ke);
            for (var st = 0; st < ke; st++)
                ge[st] = arguments[st + 2];
            ae.children = ge
        }
        return {
            $$typeof: i,
            type: k.type,
            key: fe,
            ref: pe,
            props: ae,
            _owner: ve
        }
    }
    ,
    ie.createContext = function(k) {
        return k = {
            $$typeof: h,
            _currentValue: k,
            _currentValue2: k,
            _threadCount: 0,
            Provider: null,
            Consumer: null,
            _defaultValue: null,
            _globalName: null
        },
        k.Provider = {
            $$typeof: f,
            _context: k
        },
        k.Consumer = k
    }
    ,
    ie.createElement = ee,
    ie.createFactory = function(k) {
        var T = ee.bind(null, k);
        return T.type = k,
        T
    }
    ,
    ie.createRef = function() {
        return {
            current: null
        }
    }
    ,
    ie.forwardRef = function(k) {
        return {
            $$typeof: g,
            render: k
        }
    }
    ,
    ie.isValidElement = ue,
    ie.lazy = function(k) {
        return {
            $$typeof: b,
            _payload: {
                _status: -1,
                _result: k
            },
            _init: Oe
        }
    }
    ,
    ie.memo = function(k, T) {
        return {
            $$typeof: x,
            type: k,
            compare: T === void 0 ? null : T
        }
    }
    ,
    ie.startTransition = function(k) {
        var T = F.transition;
        F.transition = {};
        try {
            k()
        } finally {
            F.transition = T
        }
    }
    ,
    ie.unstable_act = U,
    ie.useCallback = function(k, T) {
        return ye.current.useCallback(k, T)
    }
    ,
    ie.useContext = function(k) {
        return ye.current.useContext(k)
    }
    ,
    ie.useDebugValue = function() {}
    ,
    ie.useDeferredValue = function(k) {
        return ye.current.useDeferredValue(k)
    }
    ,
    ie.useEffect = function(k, T) {
        return ye.current.useEffect(k, T)
    }
    ,
    ie.useId = function() {
        return ye.current.useId()
    }
    ,
    ie.useImperativeHandle = function(k, T, le) {
        return ye.current.useImperativeHandle(k, T, le)
    }
    ,
    ie.useInsertionEffect = function(k, T) {
        return ye.current.useInsertionEffect(k, T)
    }
    ,
    ie.useLayoutEffect = function(k, T) {
        return ye.current.useLayoutEffect(k, T)
    }
    ,
    ie.useMemo = function(k, T) {
        return ye.current.useMemo(k, T)
    }
    ,
    ie.useReducer = function(k, T, le) {
        return ye.current.useReducer(k, T, le)
    }
    ,
    ie.useRef = function(k) {
        return ye.current.useRef(k)
    }
    ,
    ie.useState = function(k) {
        return ye.current.useState(k)
    }
    ,
    ie.useSyncExternalStore = function(k, T, le) {
        return ye.current.useSyncExternalStore(k, T, le)
    }
    ,
    ie.useTransition = function() {
        return ye.current.useTransition()
    }
    ,
    ie.version = "18.3.1",
    ie
}
var $c;
function Aa() {
    return $c || ($c = 1,
    ga.exports = Rh()),
    ga.exports
}
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ic;
function Oh() {
    if (Ic)
        return Vr;
    Ic = 1;
    var i = Aa()
      , s = Symbol.for("react.element")
      , l = Symbol.for("react.fragment")
      , u = Object.prototype.hasOwnProperty
      , d = i.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner
      , f = {
        key: !0,
        ref: !0,
        __self: !0,
        __source: !0
    };
    function h(g, m, x) {
        var b, w = {}, v = null, R = null;
        x !== void 0 && (v = "" + x),
        m.key !== void 0 && (v = "" + m.key),
        m.ref !== void 0 && (R = m.ref);
        for (b in m)
            u.call(m, b) && !f.hasOwnProperty(b) && (w[b] = m[b]);
        if (g && g.defaultProps)
            for (b in m = g.defaultProps,
            m)
                w[b] === void 0 && (w[b] = m[b]);
        return {
            $$typeof: s,
            type: g,
            key: v,
            ref: R,
            props: w,
            _owner: d.current
        }
    }
    return Vr.Fragment = l,
    Vr.jsx = h,
    Vr.jsxs = h,
    Vr
}
var Fc;
function Th() {
    return Fc || (Fc = 1,
    ma.exports = Oh()),
    ma.exports
}
var a = Th()
  , O = Aa();
const tr = Nd(O)
  , zh = _h({
    __proto__: null,
    default: tr
}, [O]);
var cl = {}
  , xa = {
    exports: {}
}
  , rt = {}
  , ya = {
    exports: {}
}
  , va = {};
/**
 * @license React
 * scheduler.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Uc;
function Mh() {
    return Uc || (Uc = 1,
    (function(i) {
        function s(F, Y) {
            var U = F.length;
            F.push(Y);
            e: for (; 0 < U; ) {
                var k = U - 1 >>> 1
                  , T = F[k];
                if (0 < d(T, Y))
                    F[k] = Y,
                    F[U] = T,
                    U = k;
                else
                    break e
            }
        }
        function l(F) {
            return F.length === 0 ? null : F[0]
        }
        function u(F) {
            if (F.length === 0)
                return null;
            var Y = F[0]
              , U = F.pop();
            if (U !== Y) {
                F[0] = U;
                e: for (var k = 0, T = F.length, le = T >>> 1; k < le; ) {
                    var ae = 2 * (k + 1) - 1
                      , fe = F[ae]
                      , pe = ae + 1
                      , ve = F[pe];
                    if (0 > d(fe, U))
                        pe < T && 0 > d(ve, fe) ? (F[k] = ve,
                        F[pe] = U,
                        k = pe) : (F[k] = fe,
                        F[ae] = U,
                        k = ae);
                    else if (pe < T && 0 > d(ve, U))
                        F[k] = ve,
                        F[pe] = U,
                        k = pe;
                    else
                        break e
                }
            }
            return Y
        }
        function d(F, Y) {
            var U = F.sortIndex - Y.sortIndex;
            return U !== 0 ? U : F.id - Y.id
        }
        if (typeof performance == "object" && typeof performance.now == "function") {
            var f = performance;
            i.unstable_now = function() {
                return f.now()
            }
        } else {
            var h = Date
              , g = h.now();
            i.unstable_now = function() {
                return h.now() - g
            }
        }
        var m = []
          , x = []
          , b = 1
          , w = null
          , v = 3
          , R = !1
          , E = !1
          , _ = !1
          , P = typeof setTimeout == "function" ? setTimeout : null
          , $ = typeof clearTimeout == "function" ? clearTimeout : null
          , I = typeof setImmediate < "u" ? setImmediate : null;
        typeof navigator < "u" && navigator.scheduling !== void 0 && navigator.scheduling.isInputPending !== void 0 && navigator.scheduling.isInputPending.bind(navigator.scheduling);
        function V(F) {
            for (var Y = l(x); Y !== null; ) {
                if (Y.callback === null)
                    u(x);
                else if (Y.startTime <= F)
                    u(x),
                    Y.sortIndex = Y.expirationTime,
                    s(m, Y);
                else
                    break;
                Y = l(x)
            }
        }
        function H(F) {
            if (_ = !1,
            V(F),
            !E)
                if (l(m) !== null)
                    E = !0,
                    Oe(se);
                else {
                    var Y = l(x);
                    Y !== null && ye(H, Y.startTime - F)
                }
        }
        function se(F, Y) {
            E = !1,
            _ && (_ = !1,
            $(ee),
            ee = -1),
            R = !0;
            var U = v;
            try {
                for (V(Y),
                w = l(m); w !== null && (!(w.expirationTime > Y) || F && !ce()); ) {
                    var k = w.callback;
                    if (typeof k == "function") {
                        w.callback = null,
                        v = w.priorityLevel;
                        var T = k(w.expirationTime <= Y);
                        Y = i.unstable_now(),
                        typeof T == "function" ? w.callback = T : w === l(m) && u(m),
                        V(Y)
                    } else
                        u(m);
                    w = l(m)
                }
                if (w !== null)
                    var le = !0;
                else {
                    var ae = l(x);
                    ae !== null && ye(H, ae.startTime - Y),
                    le = !1
                }
                return le
            } finally {
                w = null,
                v = U,
                R = !1
            }
        }
        var K = !1
          , te = null
          , ee = -1
          , J = 5
          , ue = -1;
        function ce() {
            return !(i.unstable_now() - ue < J)
        }
        function me() {
            if (te !== null) {
                var F = i.unstable_now();
                ue = F;
                var Y = !0;
                try {
                    Y = te(!0, F)
                } finally {
                    Y ? De() : (K = !1,
                    te = null)
                }
            } else
                K = !1
        }
        var De;
        if (typeof I == "function")
            De = function() {
                I(me)
            }
            ;
        else if (typeof MessageChannel < "u") {
            var je = new MessageChannel
              , Pe = je.port2;
            je.port1.onmessage = me,
            De = function() {
                Pe.postMessage(null)
            }
        } else
            De = function() {
                P(me, 0)
            }
            ;
        function Oe(F) {
            te = F,
            K || (K = !0,
            De())
        }
        function ye(F, Y) {
            ee = P(function() {
                F(i.unstable_now())
            }, Y)
        }
        i.unstable_IdlePriority = 5,
        i.unstable_ImmediatePriority = 1,
        i.unstable_LowPriority = 4,
        i.unstable_NormalPriority = 3,
        i.unstable_Profiling = null,
        i.unstable_UserBlockingPriority = 2,
        i.unstable_cancelCallback = function(F) {
            F.callback = null
        }
        ,
        i.unstable_continueExecution = function() {
            E || R || (E = !0,
            Oe(se))
        }
        ,
        i.unstable_forceFrameRate = function(F) {
            0 > F || 125 < F ? console.error("forceFrameRate takes a positive int between 0 and 125, forcing frame rates higher than 125 fps is not supported") : J = 0 < F ? Math.floor(1e3 / F) : 5
        }
        ,
        i.unstable_getCurrentPriorityLevel = function() {
            return v
        }
        ,
        i.unstable_getFirstCallbackNode = function() {
            return l(m)
        }
        ,
        i.unstable_next = function(F) {
            switch (v) {
            case 1:
            case 2:
            case 3:
                var Y = 3;
                break;
            default:
                Y = v
            }
            var U = v;
            v = Y;
            try {
                return F()
            } finally {
                v = U
            }
        }
        ,
        i.unstable_pauseExecution = function() {}
        ,
        i.unstable_requestPaint = function() {}
        ,
        i.unstable_runWithPriority = function(F, Y) {
            switch (F) {
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                break;
            default:
                F = 3
            }
            var U = v;
            v = F;
            try {
                return Y()
            } finally {
                v = U
            }
        }
        ,
        i.unstable_scheduleCallback = function(F, Y, U) {
            var k = i.unstable_now();
            switch (typeof U == "object" && U !== null ? (U = U.delay,
            U = typeof U == "number" && 0 < U ? k + U : k) : U = k,
            F) {
            case 1:
                var T = -1;
                break;
            case 2:
                T = 250;
                break;
            case 5:
                T = 1073741823;
                break;
            case 4:
                T = 1e4;
                break;
            default:
                T = 5e3
            }
            return T = U + T,
            F = {
                id: b++,
                callback: Y,
                priorityLevel: F,
                startTime: U,
                expirationTime: T,
                sortIndex: -1
            },
            U > k ? (F.sortIndex = U,
            s(x, F),
            l(m) === null && F === l(x) && (_ ? ($(ee),
            ee = -1) : _ = !0,
            ye(H, U - k))) : (F.sortIndex = T,
            s(m, F),
            E || R || (E = !0,
            Oe(se))),
            F
        }
        ,
        i.unstable_shouldYield = ce,
        i.unstable_wrapCallback = function(F) {
            var Y = v;
            return function() {
                var U = v;
                v = Y;
                try {
                    return F.apply(this, arguments)
                } finally {
                    v = U
                }
            }
        }
    }
    )(va)),
    va
}
var Bc;
function Ah() {
    return Bc || (Bc = 1,
    ya.exports = Mh()),
    ya.exports
}
/**
 * @license React
 * react-dom.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Vc;
function Dh() {
    if (Vc)
        return rt;
    Vc = 1;
    var i = Aa()
      , s = Ah();
    function l(e) {
        for (var t = "https://reactjs.org/docs/error-decoder.html?invariant=" + e, n = 1; n < arguments.length; n++)
            t += "&args[]=" + encodeURIComponent(arguments[n]);
        return "Minified React error #" + e + "; visit " + t + " for the full message or use the non-minified dev environment for full errors and additional helpful warnings."
    }
    var u = new Set
      , d = {};
    function f(e, t) {
        h(e, t),
        h(e + "Capture", t)
    }
    function h(e, t) {
        for (d[e] = t,
        e = 0; e < t.length; e++)
            u.add(t[e])
    }
    var g = !(typeof window > "u" || typeof window.document > "u" || typeof window.document.createElement > "u")
      , m = Object.prototype.hasOwnProperty
      , x = /^[:A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD][:A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\-.0-9\u00B7\u0300-\u036F\u203F-\u2040]*$/
      , b = {}
      , w = {};
    function v(e) {
        return m.call(w, e) ? !0 : m.call(b, e) ? !1 : x.test(e) ? w[e] = !0 : (b[e] = !0,
        !1)
    }
    function R(e, t, n, r) {
        if (n !== null && n.type === 0)
            return !1;
        switch (typeof t) {
        case "function":
        case "symbol":
            return !0;
        case "boolean":
            return r ? !1 : n !== null ? !n.acceptsBooleans : (e = e.toLowerCase().slice(0, 5),
            e !== "data-" && e !== "aria-");
        default:
            return !1
        }
    }
    function E(e, t, n, r) {
        if (t === null || typeof t > "u" || R(e, t, n, r))
            return !0;
        if (r)
            return !1;
        if (n !== null)
            switch (n.type) {
            case 3:
                return !t;
            case 4:
                return t === !1;
            case 5:
                return isNaN(t);
            case 6:
                return isNaN(t) || 1 > t
            }
        return !1
    }
    function _(e, t, n, r, o, c, p) {
        this.acceptsBooleans = t === 2 || t === 3 || t === 4,
        this.attributeName = r,
        this.attributeNamespace = o,
        this.mustUseProperty = n,
        this.propertyName = e,
        this.type = t,
        this.sanitizeURL = c,
        this.removeEmptyString = p
    }
    var P = {};
    "children dangerouslySetInnerHTML defaultValue defaultChecked innerHTML suppressContentEditableWarning suppressHydrationWarning style".split(" ").forEach(function(e) {
        P[e] = new _(e,0,!1,e,null,!1,!1)
    }),
    [["acceptCharset", "accept-charset"], ["className", "class"], ["htmlFor", "for"], ["httpEquiv", "http-equiv"]].forEach(function(e) {
        var t = e[0];
        P[t] = new _(t,1,!1,e[1],null,!1,!1)
    }),
    ["contentEditable", "draggable", "spellCheck", "value"].forEach(function(e) {
        P[e] = new _(e,2,!1,e.toLowerCase(),null,!1,!1)
    }),
    ["autoReverse", "externalResourcesRequired", "focusable", "preserveAlpha"].forEach(function(e) {
        P[e] = new _(e,2,!1,e,null,!1,!1)
    }),
    "allowFullScreen async autoFocus autoPlay controls default defer disabled disablePictureInPicture disableRemotePlayback formNoValidate hidden loop noModule noValidate open playsInline readOnly required reversed scoped seamless itemScope".split(" ").forEach(function(e) {
        P[e] = new _(e,3,!1,e.toLowerCase(),null,!1,!1)
    }),
    ["checked", "multiple", "muted", "selected"].forEach(function(e) {
        P[e] = new _(e,3,!0,e,null,!1,!1)
    }),
    ["capture", "download"].forEach(function(e) {
        P[e] = new _(e,4,!1,e,null,!1,!1)
    }),
    ["cols", "rows", "size", "span"].forEach(function(e) {
        P[e] = new _(e,6,!1,e,null,!1,!1)
    }),
    ["rowSpan", "start"].forEach(function(e) {
        P[e] = new _(e,5,!1,e.toLowerCase(),null,!1,!1)
    });
    var $ = /[\-:]([a-z])/g;
    function I(e) {
        return e[1].toUpperCase()
    }
    "accent-height alignment-baseline arabic-form baseline-shift cap-height clip-path clip-rule color-interpolation color-interpolation-filters color-profile color-rendering dominant-baseline enable-background fill-opacity fill-rule flood-color flood-opacity font-family font-size font-size-adjust font-stretch font-style font-variant font-weight glyph-name glyph-orientation-horizontal glyph-orientation-vertical horiz-adv-x horiz-origin-x image-rendering letter-spacing lighting-color marker-end marker-mid marker-start overline-position overline-thickness paint-order panose-1 pointer-events rendering-intent shape-rendering stop-color stop-opacity strikethrough-position strikethrough-thickness stroke-dasharray stroke-dashoffset stroke-linecap stroke-linejoin stroke-miterlimit stroke-opacity stroke-width text-anchor text-decoration text-rendering underline-position underline-thickness unicode-bidi unicode-range units-per-em v-alphabetic v-hanging v-ideographic v-mathematical vector-effect vert-adv-y vert-origin-x vert-origin-y word-spacing writing-mode xmlns:xlink x-height".split(" ").forEach(function(e) {
        var t = e.replace($, I);
        P[t] = new _(t,1,!1,e,null,!1,!1)
    }),
    "xlink:actuate xlink:arcrole xlink:role xlink:show xlink:title xlink:type".split(" ").forEach(function(e) {
        var t = e.replace($, I);
        P[t] = new _(t,1,!1,e,"http://www.w3.org/1999/xlink",!1,!1)
    }),
    ["xml:base", "xml:lang", "xml:space"].forEach(function(e) {
        var t = e.replace($, I);
        P[t] = new _(t,1,!1,e,"http://www.w3.org/XML/1998/namespace",!1,!1)
    }),
    ["tabIndex", "crossOrigin"].forEach(function(e) {
        P[e] = new _(e,1,!1,e.toLowerCase(),null,!1,!1)
    }),
    P.xlinkHref = new _("xlinkHref",1,!1,"xlink:href","http://www.w3.org/1999/xlink",!0,!1),
    ["src", "href", "action", "formAction"].forEach(function(e) {
        P[e] = new _(e,1,!1,e.toLowerCase(),null,!0,!0)
    });
    function V(e, t, n, r) {
        var o = P.hasOwnProperty(t) ? P[t] : null;
        (o !== null ? o.type !== 0 : r || !(2 < t.length) || t[0] !== "o" && t[0] !== "O" || t[1] !== "n" && t[1] !== "N") && (E(t, n, o, r) && (n = null),
        r || o === null ? v(t) && (n === null ? e.removeAttribute(t) : e.setAttribute(t, "" + n)) : o.mustUseProperty ? e[o.propertyName] = n === null ? o.type === 3 ? !1 : "" : n : (t = o.attributeName,
        r = o.attributeNamespace,
        n === null ? e.removeAttribute(t) : (o = o.type,
        n = o === 3 || o === 4 && n === !0 ? "" : "" + n,
        r ? e.setAttributeNS(r, t, n) : e.setAttribute(t, n))))
    }
    var H = i.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED
      , se = Symbol.for("react.element")
      , K = Symbol.for("react.portal")
      , te = Symbol.for("react.fragment")
      , ee = Symbol.for("react.strict_mode")
      , J = Symbol.for("react.profiler")
      , ue = Symbol.for("react.provider")
      , ce = Symbol.for("react.context")
      , me = Symbol.for("react.forward_ref")
      , De = Symbol.for("react.suspense")
      , je = Symbol.for("react.suspense_list")
      , Pe = Symbol.for("react.memo")
      , Oe = Symbol.for("react.lazy")
      , ye = Symbol.for("react.offscreen")
      , F = Symbol.iterator;
    function Y(e) {
        return e === null || typeof e != "object" ? null : (e = F && e[F] || e["@@iterator"],
        typeof e == "function" ? e : null)
    }
    var U = Object.assign, k;
    function T(e) {
        if (k === void 0)
            try {
                throw Error()
            } catch (n) {
                var t = n.stack.trim().match(/\n( *(at )?)/);
                k = t && t[1] || ""
            }
        return `
` + k + e
    }
    var le = !1;
    function ae(e, t) {
        if (!e || le)
            return "";
        le = !0;
        var n = Error.prepareStackTrace;
        Error.prepareStackTrace = void 0;
        try {
            if (t)
                if (t = function() {
                    throw Error()
                }
                ,
                Object.defineProperty(t.prototype, "props", {
                    set: function() {
                        throw Error()
                    }
                }),
                typeof Reflect == "object" && Reflect.construct) {
                    try {
                        Reflect.construct(t, [])
                    } catch (L) {
                        var r = L
                    }
                    Reflect.construct(e, [], t)
                } else {
                    try {
                        t.call()
                    } catch (L) {
                        r = L
                    }
                    e.call(t.prototype)
                }
            else {
                try {
                    throw Error()
                } catch (L) {
                    r = L
                }
                e()
            }
        } catch (L) {
            if (L && r && typeof L.stack == "string") {
                for (var o = L.stack.split(`
`), c = r.stack.split(`
`), p = o.length - 1, y = c.length - 1; 1 <= p && 0 <= y && o[p] !== c[y]; )
                    y--;
                for (; 1 <= p && 0 <= y; p--,
                y--)
                    if (o[p] !== c[y]) {
                        if (p !== 1 || y !== 1)
                            do
                                if (p--,
                                y--,
                                0 > y || o[p] !== c[y]) {
                                    var N = `
` + o[p].replace(" at new ", " at ");
                                    return e.displayName && N.includes("<anonymous>") && (N = N.replace("<anonymous>", e.displayName)),
                                    N
                                }
                            while (1 <= p && 0 <= y);
                        break
                    }
            }
        } finally {
            le = !1,
            Error.prepareStackTrace = n
        }
        return (e = e ? e.displayName || e.name : "") ? T(e) : ""
    }
    function fe(e) {
        switch (e.tag) {
        case 5:
            return T(e.type);
        case 16:
            return T("Lazy");
        case 13:
            return T("Suspense");
        case 19:
            return T("SuspenseList");
        case 0:
        case 2:
        case 15:
            return e = ae(e.type, !1),
            e;
        case 11:
            return e = ae(e.type.render, !1),
            e;
        case 1:
            return e = ae(e.type, !0),
            e;
        default:
            return ""
        }
    }
    function pe(e) {
        if (e == null)
            return null;
        if (typeof e == "function")
            return e.displayName || e.name || null;
        if (typeof e == "string")
            return e;
        switch (e) {
        case te:
            return "Fragment";
        case K:
            return "Portal";
        case J:
            return "Profiler";
        case ee:
            return "StrictMode";
        case De:
            return "Suspense";
        case je:
            return "SuspenseList"
        }
        if (typeof e == "object")
            switch (e.$$typeof) {
            case ce:
                return (e.displayName || "Context") + ".Consumer";
            case ue:
                return (e._context.displayName || "Context") + ".Provider";
            case me:
                var t = e.render;
                return e = e.displayName,
                e || (e = t.displayName || t.name || "",
                e = e !== "" ? "ForwardRef(" + e + ")" : "ForwardRef"),
                e;
            case Pe:
                return t = e.displayName || null,
                t !== null ? t : pe(e.type) || "Memo";
            case Oe:
                t = e._payload,
                e = e._init;
                try {
                    return pe(e(t))
                } catch {}
            }
        return null
    }
    function ve(e) {
        var t = e.type;
        switch (e.tag) {
        case 24:
            return "Cache";
        case 9:
            return (t.displayName || "Context") + ".Consumer";
        case 10:
            return (t._context.displayName || "Context") + ".Provider";
        case 18:
            return "DehydratedFragment";
        case 11:
            return e = t.render,
            e = e.displayName || e.name || "",
            t.displayName || (e !== "" ? "ForwardRef(" + e + ")" : "ForwardRef");
        case 7:
            return "Fragment";
        case 5:
            return t;
        case 4:
            return "Portal";
        case 3:
            return "Root";
        case 6:
            return "Text";
        case 16:
            return pe(t);
        case 8:
            return t === ee ? "StrictMode" : "Mode";
        case 22:
            return "Offscreen";
        case 12:
            return "Profiler";
        case 21:
            return "Scope";
        case 13:
            return "Suspense";
        case 19:
            return "SuspenseList";
        case 25:
            return "TracingMarker";
        case 1:
        case 0:
        case 17:
        case 2:
        case 14:
        case 15:
            if (typeof t == "function")
                return t.displayName || t.name || null;
            if (typeof t == "string")
                return t
        }
        return null
    }
    function ge(e) {
        switch (typeof e) {
        case "boolean":
        case "number":
        case "string":
        case "undefined":
            return e;
        case "object":
            return e;
        default:
            return ""
        }
    }
    function ke(e) {
        var t = e.type;
        return (e = e.nodeName) && e.toLowerCase() === "input" && (t === "checkbox" || t === "radio")
    }
    function st(e) {
        var t = ke(e) ? "checked" : "value"
          , n = Object.getOwnPropertyDescriptor(e.constructor.prototype, t)
          , r = "" + e[t];
        if (!e.hasOwnProperty(t) && typeof n < "u" && typeof n.get == "function" && typeof n.set == "function") {
            var o = n.get
              , c = n.set;
            return Object.defineProperty(e, t, {
                configurable: !0,
                get: function() {
                    return o.call(this)
                },
                set: function(p) {
                    r = "" + p,
                    c.call(this, p)
                }
            }),
            Object.defineProperty(e, t, {
                enumerable: n.enumerable
            }),
            {
                getValue: function() {
                    return r
                },
                setValue: function(p) {
                    r = "" + p
                },
                stopTracking: function() {
                    e._valueTracker = null,
                    delete e[t]
                }
            }
        }
    }
    function es(e) {
        e._valueTracker || (e._valueTracker = st(e))
    }
    function Ba(e) {
        if (!e)
            return !1;
        var t = e._valueTracker;
        if (!t)
            return !0;
        var n = t.getValue()
          , r = "";
        return e && (r = ke(e) ? e.checked ? "true" : "false" : e.value),
        e = r,
        e !== n ? (t.setValue(e),
        !0) : !1
    }
    function ts(e) {
        if (e = e || (typeof document < "u" ? document : void 0),
        typeof e > "u")
            return null;
        try {
            return e.activeElement || e.body
        } catch {
            return e.body
        }
    }
    function Nl(e, t) {
        var n = t.checked;
        return U({}, t, {
            defaultChecked: void 0,
            defaultValue: void 0,
            value: void 0,
            checked: n ?? e._wrapperState.initialChecked
        })
    }
    function Va(e, t) {
        var n = t.defaultValue == null ? "" : t.defaultValue
          , r = t.checked != null ? t.checked : t.defaultChecked;
        n = ge(t.value != null ? t.value : n),
        e._wrapperState = {
            initialChecked: r,
            initialValue: n,
            controlled: t.type === "checkbox" || t.type === "radio" ? t.checked != null : t.value != null
        }
    }
    function Ha(e, t) {
        t = t.checked,
        t != null && V(e, "checked", t, !1)
    }
    function jl(e, t) {
        Ha(e, t);
        var n = ge(t.value)
          , r = t.type;
        if (n != null)
            r === "number" ? (n === 0 && e.value === "" || e.value != n) && (e.value = "" + n) : e.value !== "" + n && (e.value = "" + n);
        else if (r === "submit" || r === "reset") {
            e.removeAttribute("value");
            return
        }
        t.hasOwnProperty("value") ? kl(e, t.type, n) : t.hasOwnProperty("defaultValue") && kl(e, t.type, ge(t.defaultValue)),
        t.checked == null && t.defaultChecked != null && (e.defaultChecked = !!t.defaultChecked)
    }
    function Ka(e, t, n) {
        if (t.hasOwnProperty("value") || t.hasOwnProperty("defaultValue")) {
            var r = t.type;
            if (!(r !== "submit" && r !== "reset" || t.value !== void 0 && t.value !== null))
                return;
            t = "" + e._wrapperState.initialValue,
            n || t === e.value || (e.value = t),
            e.defaultValue = t
        }
        n = e.name,
        n !== "" && (e.name = ""),
        e.defaultChecked = !!e._wrapperState.initialChecked,
        n !== "" && (e.name = n)
    }
    function kl(e, t, n) {
        (t !== "number" || ts(e.ownerDocument) !== e) && (n == null ? e.defaultValue = "" + e._wrapperState.initialValue : e.defaultValue !== "" + n && (e.defaultValue = "" + n))
    }
    var sr = Array.isArray;
    function Pn(e, t, n, r) {
        if (e = e.options,
        t) {
            t = {};
            for (var o = 0; o < n.length; o++)
                t["$" + n[o]] = !0;
            for (n = 0; n < e.length; n++)
                o = t.hasOwnProperty("$" + e[n].value),
                e[n].selected !== o && (e[n].selected = o),
                o && r && (e[n].defaultSelected = !0)
        } else {
            for (n = "" + ge(n),
            t = null,
            o = 0; o < e.length; o++) {
                if (e[o].value === n) {
                    e[o].selected = !0,
                    r && (e[o].defaultSelected = !0);
                    return
                }
                t !== null || e[o].disabled || (t = e[o])
            }
            t !== null && (t.selected = !0)
        }
    }
    function Sl(e, t) {
        if (t.dangerouslySetInnerHTML != null)
            throw Error(l(91));
        return U({}, t, {
            value: void 0,
            defaultValue: void 0,
            children: "" + e._wrapperState.initialValue
        })
    }
    function Wa(e, t) {
        var n = t.value;
        if (n == null) {
            if (n = t.children,
            t = t.defaultValue,
            n != null) {
                if (t != null)
                    throw Error(l(92));
                if (sr(n)) {
                    if (1 < n.length)
                        throw Error(l(93));
                    n = n[0]
                }
                t = n
            }
            t == null && (t = ""),
            n = t
        }
        e._wrapperState = {
            initialValue: ge(n)
        }
    }
    function qa(e, t) {
        var n = ge(t.value)
          , r = ge(t.defaultValue);
        n != null && (n = "" + n,
        n !== e.value && (e.value = n),
        t.defaultValue == null && e.defaultValue !== n && (e.defaultValue = n)),
        r != null && (e.defaultValue = "" + r)
    }
    function Ya(e) {
        var t = e.textContent;
        t === e._wrapperState.initialValue && t !== "" && t !== null && (e.value = t)
    }
    function Qa(e) {
        switch (e) {
        case "svg":
            return "http://www.w3.org/2000/svg";
        case "math":
            return "http://www.w3.org/1998/Math/MathML";
        default:
            return "http://www.w3.org/1999/xhtml"
        }
    }
    function Cl(e, t) {
        return e == null || e === "http://www.w3.org/1999/xhtml" ? Qa(t) : e === "http://www.w3.org/2000/svg" && t === "foreignObject" ? "http://www.w3.org/1999/xhtml" : e
    }
    var ns, Ga = (function(e) {
        return typeof MSApp < "u" && MSApp.execUnsafeLocalFunction ? function(t, n, r, o) {
            MSApp.execUnsafeLocalFunction(function() {
                return e(t, n, r, o)
            })
        }
        : e
    }
    )(function(e, t) {
        if (e.namespaceURI !== "http://www.w3.org/2000/svg" || "innerHTML" in e)
            e.innerHTML = t;
        else {
            for (ns = ns || document.createElement("div"),
            ns.innerHTML = "<svg>" + t.valueOf().toString() + "</svg>",
            t = ns.firstChild; e.firstChild; )
                e.removeChild(e.firstChild);
            for (; t.firstChild; )
                e.appendChild(t.firstChild)
        }
    });
    function lr(e, t) {
        if (t) {
            var n = e.firstChild;
            if (n && n === e.lastChild && n.nodeType === 3) {
                n.nodeValue = t;
                return
            }
        }
        e.textContent = t
    }
    var ir = {
        animationIterationCount: !0,
        aspectRatio: !0,
        borderImageOutset: !0,
        borderImageSlice: !0,
        borderImageWidth: !0,
        boxFlex: !0,
        boxFlexGroup: !0,
        boxOrdinalGroup: !0,
        columnCount: !0,
        columns: !0,
        flex: !0,
        flexGrow: !0,
        flexPositive: !0,
        flexShrink: !0,
        flexNegative: !0,
        flexOrder: !0,
        gridArea: !0,
        gridRow: !0,
        gridRowEnd: !0,
        gridRowSpan: !0,
        gridRowStart: !0,
        gridColumn: !0,
        gridColumnEnd: !0,
        gridColumnSpan: !0,
        gridColumnStart: !0,
        fontWeight: !0,
        lineClamp: !0,
        lineHeight: !0,
        opacity: !0,
        order: !0,
        orphans: !0,
        tabSize: !0,
        widows: !0,
        zIndex: !0,
        zoom: !0,
        fillOpacity: !0,
        floodOpacity: !0,
        stopOpacity: !0,
        strokeDasharray: !0,
        strokeDashoffset: !0,
        strokeMiterlimit: !0,
        strokeOpacity: !0,
        strokeWidth: !0
    }
      , zf = ["Webkit", "ms", "Moz", "O"];
    Object.keys(ir).forEach(function(e) {
        zf.forEach(function(t) {
            t = t + e.charAt(0).toUpperCase() + e.substring(1),
            ir[t] = ir[e]
        })
    });
    function Ja(e, t, n) {
        return t == null || typeof t == "boolean" || t === "" ? "" : n || typeof t != "number" || t === 0 || ir.hasOwnProperty(e) && ir[e] ? ("" + t).trim() : t + "px"
    }
    function Xa(e, t) {
        e = e.style;
        for (var n in t)
            if (t.hasOwnProperty(n)) {
                var r = n.indexOf("--") === 0
                  , o = Ja(n, t[n], r);
                n === "float" && (n = "cssFloat"),
                r ? e.setProperty(n, o) : e[n] = o
            }
    }
    var Mf = U({
        menuitem: !0
    }, {
        area: !0,
        base: !0,
        br: !0,
        col: !0,
        embed: !0,
        hr: !0,
        img: !0,
        input: !0,
        keygen: !0,
        link: !0,
        meta: !0,
        param: !0,
        source: !0,
        track: !0,
        wbr: !0
    });
    function El(e, t) {
        if (t) {
            if (Mf[e] && (t.children != null || t.dangerouslySetInnerHTML != null))
                throw Error(l(137, e));
            if (t.dangerouslySetInnerHTML != null) {
                if (t.children != null)
                    throw Error(l(60));
                if (typeof t.dangerouslySetInnerHTML != "object" || !("__html" in t.dangerouslySetInnerHTML))
                    throw Error(l(61))
            }
            if (t.style != null && typeof t.style != "object")
                throw Error(l(62))
        }
    }
    function Pl(e, t) {
        if (e.indexOf("-") === -1)
            return typeof t.is == "string";
        switch (e) {
        case "annotation-xml":
        case "color-profile":
        case "font-face":
        case "font-face-src":
        case "font-face-uri":
        case "font-face-format":
        case "font-face-name":
        case "missing-glyph":
            return !1;
        default:
            return !0
        }
    }
    var Ll = null;
    function _l(e) {
        return e = e.target || e.srcElement || window,
        e.correspondingUseElement && (e = e.correspondingUseElement),
        e.nodeType === 3 ? e.parentNode : e
    }
    var Rl = null
      , Ln = null
      , _n = null;
    function Za(e) {
        if (e = Pr(e)) {
            if (typeof Rl != "function")
                throw Error(l(280));
            var t = e.stateNode;
            t && (t = Ss(t),
            Rl(e.stateNode, e.type, t))
        }
    }
    function eo(e) {
        Ln ? _n ? _n.push(e) : _n = [e] : Ln = e
    }
    function to() {
        if (Ln) {
            var e = Ln
              , t = _n;
            if (_n = Ln = null,
            Za(e),
            t)
                for (e = 0; e < t.length; e++)
                    Za(t[e])
        }
    }
    function no(e, t) {
        return e(t)
    }
    function ro() {}
    var Ol = !1;
    function so(e, t, n) {
        if (Ol)
            return e(t, n);
        Ol = !0;
        try {
            return no(e, t, n)
        } finally {
            Ol = !1,
            (Ln !== null || _n !== null) && (ro(),
            to())
        }
    }
    function ar(e, t) {
        var n = e.stateNode;
        if (n === null)
            return null;
        var r = Ss(n);
        if (r === null)
            return null;
        n = r[t];
        e: switch (t) {
        case "onClick":
        case "onClickCapture":
        case "onDoubleClick":
        case "onDoubleClickCapture":
        case "onMouseDown":
        case "onMouseDownCapture":
        case "onMouseMove":
        case "onMouseMoveCapture":
        case "onMouseUp":
        case "onMouseUpCapture":
        case "onMouseEnter":
            (r = !r.disabled) || (e = e.type,
            r = !(e === "button" || e === "input" || e === "select" || e === "textarea")),
            e = !r;
            break e;
        default:
            e = !1
        }
        if (e)
            return null;
        if (n && typeof n != "function")
            throw Error(l(231, t, typeof n));
        return n
    }
    var Tl = !1;
    if (g)
        try {
            var or = {};
            Object.defineProperty(or, "passive", {
                get: function() {
                    Tl = !0
                }
            }),
            window.addEventListener("test", or, or),
            window.removeEventListener("test", or, or)
        } catch {
            Tl = !1
        }
    function Af(e, t, n, r, o, c, p, y, N) {
        var L = Array.prototype.slice.call(arguments, 3);
        try {
            t.apply(n, L)
        } catch (M) {
            this.onError(M)
        }
    }
    var ur = !1
      , rs = null
      , ss = !1
      , zl = null
      , Df = {
        onError: function(e) {
            ur = !0,
            rs = e
        }
    };
    function $f(e, t, n, r, o, c, p, y, N) {
        ur = !1,
        rs = null,
        Af.apply(Df, arguments)
    }
    function If(e, t, n, r, o, c, p, y, N) {
        if ($f.apply(this, arguments),
        ur) {
            if (ur) {
                var L = rs;
                ur = !1,
                rs = null
            } else
                throw Error(l(198));
            ss || (ss = !0,
            zl = L)
        }
    }
    function dn(e) {
        var t = e
          , n = e;
        if (e.alternate)
            for (; t.return; )
                t = t.return;
        else {
            e = t;
            do
                t = e,
                (t.flags & 4098) !== 0 && (n = t.return),
                e = t.return;
            while (e)
        }
        return t.tag === 3 ? n : null
    }
    function lo(e) {
        if (e.tag === 13) {
            var t = e.memoizedState;
            if (t === null && (e = e.alternate,
            e !== null && (t = e.memoizedState)),
            t !== null)
                return t.dehydrated
        }
        return null
    }
    function io(e) {
        if (dn(e) !== e)
            throw Error(l(188))
    }
    function Ff(e) {
        var t = e.alternate;
        if (!t) {
            if (t = dn(e),
            t === null)
                throw Error(l(188));
            return t !== e ? null : e
        }
        for (var n = e, r = t; ; ) {
            var o = n.return;
            if (o === null)
                break;
            var c = o.alternate;
            if (c === null) {
                if (r = o.return,
                r !== null) {
                    n = r;
                    continue
                }
                break
            }
            if (o.child === c.child) {
                for (c = o.child; c; ) {
                    if (c === n)
                        return io(o),
                        e;
                    if (c === r)
                        return io(o),
                        t;
                    c = c.sibling
                }
                throw Error(l(188))
            }
            if (n.return !== r.return)
                n = o,
                r = c;
            else {
                for (var p = !1, y = o.child; y; ) {
                    if (y === n) {
                        p = !0,
                        n = o,
                        r = c;
                        break
                    }
                    if (y === r) {
                        p = !0,
                        r = o,
                        n = c;
                        break
                    }
                    y = y.sibling
                }
                if (!p) {
                    for (y = c.child; y; ) {
                        if (y === n) {
                            p = !0,
                            n = c,
                            r = o;
                            break
                        }
                        if (y === r) {
                            p = !0,
                            r = c,
                            n = o;
                            break
                        }
                        y = y.sibling
                    }
                    if (!p)
                        throw Error(l(189))
                }
            }
            if (n.alternate !== r)
                throw Error(l(190))
        }
        if (n.tag !== 3)
            throw Error(l(188));
        return n.stateNode.current === n ? e : t
    }
    function ao(e) {
        return e = Ff(e),
        e !== null ? oo(e) : null
    }
    function oo(e) {
        if (e.tag === 5 || e.tag === 6)
            return e;
        for (e = e.child; e !== null; ) {
            var t = oo(e);
            if (t !== null)
                return t;
            e = e.sibling
        }
        return null
    }
    var uo = s.unstable_scheduleCallback
      , co = s.unstable_cancelCallback
      , Uf = s.unstable_shouldYield
      , Bf = s.unstable_requestPaint
      , _e = s.unstable_now
      , Vf = s.unstable_getCurrentPriorityLevel
      , Ml = s.unstable_ImmediatePriority
      , fo = s.unstable_UserBlockingPriority
      , ls = s.unstable_NormalPriority
      , Hf = s.unstable_LowPriority
      , po = s.unstable_IdlePriority
      , is = null
      , jt = null;
    function Kf(e) {
        if (jt && typeof jt.onCommitFiberRoot == "function")
            try {
                jt.onCommitFiberRoot(is, e, void 0, (e.current.flags & 128) === 128)
            } catch {}
    }
    var gt = Math.clz32 ? Math.clz32 : Yf
      , Wf = Math.log
      , qf = Math.LN2;
    function Yf(e) {
        return e >>>= 0,
        e === 0 ? 32 : 31 - (Wf(e) / qf | 0) | 0
    }
    var as = 64
      , os = 4194304;
    function cr(e) {
        switch (e & -e) {
        case 1:
            return 1;
        case 2:
            return 2;
        case 4:
            return 4;
        case 8:
            return 8;
        case 16:
            return 16;
        case 32:
            return 32;
        case 64:
        case 128:
        case 256:
        case 512:
        case 1024:
        case 2048:
        case 4096:
        case 8192:
        case 16384:
        case 32768:
        case 65536:
        case 131072:
        case 262144:
        case 524288:
        case 1048576:
        case 2097152:
            return e & 4194240;
        case 4194304:
        case 8388608:
        case 16777216:
        case 33554432:
        case 67108864:
            return e & 130023424;
        case 134217728:
            return 134217728;
        case 268435456:
            return 268435456;
        case 536870912:
            return 536870912;
        case 1073741824:
            return 1073741824;
        default:
            return e
        }
    }
    function us(e, t) {
        var n = e.pendingLanes;
        if (n === 0)
            return 0;
        var r = 0
          , o = e.suspendedLanes
          , c = e.pingedLanes
          , p = n & 268435455;
        if (p !== 0) {
            var y = p & ~o;
            y !== 0 ? r = cr(y) : (c &= p,
            c !== 0 && (r = cr(c)))
        } else
            p = n & ~o,
            p !== 0 ? r = cr(p) : c !== 0 && (r = cr(c));
        if (r === 0)
            return 0;
        if (t !== 0 && t !== r && (t & o) === 0 && (o = r & -r,
        c = t & -t,
        o >= c || o === 16 && (c & 4194240) !== 0))
            return t;
        if ((r & 4) !== 0 && (r |= n & 16),
        t = e.entangledLanes,
        t !== 0)
            for (e = e.entanglements,
            t &= r; 0 < t; )
                n = 31 - gt(t),
                o = 1 << n,
                r |= e[n],
                t &= ~o;
        return r
    }
    function Qf(e, t) {
        switch (e) {
        case 1:
        case 2:
        case 4:
            return t + 250;
        case 8:
        case 16:
        case 32:
        case 64:
        case 128:
        case 256:
        case 512:
        case 1024:
        case 2048:
        case 4096:
        case 8192:
        case 16384:
        case 32768:
        case 65536:
        case 131072:
        case 262144:
        case 524288:
        case 1048576:
        case 2097152:
            return t + 5e3;
        case 4194304:
        case 8388608:
        case 16777216:
        case 33554432:
        case 67108864:
            return -1;
        case 134217728:
        case 268435456:
        case 536870912:
        case 1073741824:
            return -1;
        default:
            return -1
        }
    }
    function Gf(e, t) {
        for (var n = e.suspendedLanes, r = e.pingedLanes, o = e.expirationTimes, c = e.pendingLanes; 0 < c; ) {
            var p = 31 - gt(c)
              , y = 1 << p
              , N = o[p];
            N === -1 ? ((y & n) === 0 || (y & r) !== 0) && (o[p] = Qf(y, t)) : N <= t && (e.expiredLanes |= y),
            c &= ~y
        }
    }
    function Al(e) {
        return e = e.pendingLanes & -1073741825,
        e !== 0 ? e : e & 1073741824 ? 1073741824 : 0
    }
    function ho() {
        var e = as;
        return as <<= 1,
        (as & 4194240) === 0 && (as = 64),
        e
    }
    function Dl(e) {
        for (var t = [], n = 0; 31 > n; n++)
            t.push(e);
        return t
    }
    function dr(e, t, n) {
        e.pendingLanes |= t,
        t !== 536870912 && (e.suspendedLanes = 0,
        e.pingedLanes = 0),
        e = e.eventTimes,
        t = 31 - gt(t),
        e[t] = n
    }
    function Jf(e, t) {
        var n = e.pendingLanes & ~t;
        e.pendingLanes = t,
        e.suspendedLanes = 0,
        e.pingedLanes = 0,
        e.expiredLanes &= t,
        e.mutableReadLanes &= t,
        e.entangledLanes &= t,
        t = e.entanglements;
        var r = e.eventTimes;
        for (e = e.expirationTimes; 0 < n; ) {
            var o = 31 - gt(n)
              , c = 1 << o;
            t[o] = 0,
            r[o] = -1,
            e[o] = -1,
            n &= ~c
        }
    }
    function $l(e, t) {
        var n = e.entangledLanes |= t;
        for (e = e.entanglements; n; ) {
            var r = 31 - gt(n)
              , o = 1 << r;
            o & t | e[r] & t && (e[r] |= t),
            n &= ~o
        }
    }
    var xe = 0;
    function mo(e) {
        return e &= -e,
        1 < e ? 4 < e ? (e & 268435455) !== 0 ? 16 : 536870912 : 4 : 1
    }
    var go, Il, xo, yo, vo, Fl = !1, cs = [], Ft = null, Ut = null, Bt = null, fr = new Map, pr = new Map, Vt = [], Xf = "mousedown mouseup touchcancel touchend touchstart auxclick dblclick pointercancel pointerdown pointerup dragend dragstart drop compositionend compositionstart keydown keypress keyup input textInput copy cut paste click change contextmenu reset submit".split(" ");
    function wo(e, t) {
        switch (e) {
        case "focusin":
        case "focusout":
            Ft = null;
            break;
        case "dragenter":
        case "dragleave":
            Ut = null;
            break;
        case "mouseover":
        case "mouseout":
            Bt = null;
            break;
        case "pointerover":
        case "pointerout":
            fr.delete(t.pointerId);
            break;
        case "gotpointercapture":
        case "lostpointercapture":
            pr.delete(t.pointerId)
        }
    }
    function hr(e, t, n, r, o, c) {
        return e === null || e.nativeEvent !== c ? (e = {
            blockedOn: t,
            domEventName: n,
            eventSystemFlags: r,
            nativeEvent: c,
            targetContainers: [o]
        },
        t !== null && (t = Pr(t),
        t !== null && Il(t)),
        e) : (e.eventSystemFlags |= r,
        t = e.targetContainers,
        o !== null && t.indexOf(o) === -1 && t.push(o),
        e)
    }
    function Zf(e, t, n, r, o) {
        switch (t) {
        case "focusin":
            return Ft = hr(Ft, e, t, n, r, o),
            !0;
        case "dragenter":
            return Ut = hr(Ut, e, t, n, r, o),
            !0;
        case "mouseover":
            return Bt = hr(Bt, e, t, n, r, o),
            !0;
        case "pointerover":
            var c = o.pointerId;
            return fr.set(c, hr(fr.get(c) || null, e, t, n, r, o)),
            !0;
        case "gotpointercapture":
            return c = o.pointerId,
            pr.set(c, hr(pr.get(c) || null, e, t, n, r, o)),
            !0
        }
        return !1
    }
    function bo(e) {
        var t = fn(e.target);
        if (t !== null) {
            var n = dn(t);
            if (n !== null) {
                if (t = n.tag,
                t === 13) {
                    if (t = lo(n),
                    t !== null) {
                        e.blockedOn = t,
                        vo(e.priority, function() {
                            xo(n)
                        });
                        return
                    }
                } else if (t === 3 && n.stateNode.current.memoizedState.isDehydrated) {
                    e.blockedOn = n.tag === 3 ? n.stateNode.containerInfo : null;
                    return
                }
            }
        }
        e.blockedOn = null
    }
    function ds(e) {
        if (e.blockedOn !== null)
            return !1;
        for (var t = e.targetContainers; 0 < t.length; ) {
            var n = Bl(e.domEventName, e.eventSystemFlags, t[0], e.nativeEvent);
            if (n === null) {
                n = e.nativeEvent;
                var r = new n.constructor(n.type,n);
                Ll = r,
                n.target.dispatchEvent(r),
                Ll = null
            } else
                return t = Pr(n),
                t !== null && Il(t),
                e.blockedOn = n,
                !1;
            t.shift()
        }
        return !0
    }
    function No(e, t, n) {
        ds(e) && n.delete(t)
    }
    function ep() {
        Fl = !1,
        Ft !== null && ds(Ft) && (Ft = null),
        Ut !== null && ds(Ut) && (Ut = null),
        Bt !== null && ds(Bt) && (Bt = null),
        fr.forEach(No),
        pr.forEach(No)
    }
    function mr(e, t) {
        e.blockedOn === t && (e.blockedOn = null,
        Fl || (Fl = !0,
        s.unstable_scheduleCallback(s.unstable_NormalPriority, ep)))
    }
    function gr(e) {
        function t(o) {
            return mr(o, e)
        }
        if (0 < cs.length) {
            mr(cs[0], e);
            for (var n = 1; n < cs.length; n++) {
                var r = cs[n];
                r.blockedOn === e && (r.blockedOn = null)
            }
        }
        for (Ft !== null && mr(Ft, e),
        Ut !== null && mr(Ut, e),
        Bt !== null && mr(Bt, e),
        fr.forEach(t),
        pr.forEach(t),
        n = 0; n < Vt.length; n++)
            r = Vt[n],
            r.blockedOn === e && (r.blockedOn = null);
        for (; 0 < Vt.length && (n = Vt[0],
        n.blockedOn === null); )
            bo(n),
            n.blockedOn === null && Vt.shift()
    }
    var Rn = H.ReactCurrentBatchConfig
      , fs = !0;
    function tp(e, t, n, r) {
        var o = xe
          , c = Rn.transition;
        Rn.transition = null;
        try {
            xe = 1,
            Ul(e, t, n, r)
        } finally {
            xe = o,
            Rn.transition = c
        }
    }
    function np(e, t, n, r) {
        var o = xe
          , c = Rn.transition;
        Rn.transition = null;
        try {
            xe = 4,
            Ul(e, t, n, r)
        } finally {
            xe = o,
            Rn.transition = c
        }
    }
    function Ul(e, t, n, r) {
        if (fs) {
            var o = Bl(e, t, n, r);
            if (o === null)
                li(e, t, r, ps, n),
                wo(e, r);
            else if (Zf(o, e, t, n, r))
                r.stopPropagation();
            else if (wo(e, r),
            t & 4 && -1 < Xf.indexOf(e)) {
                for (; o !== null; ) {
                    var c = Pr(o);
                    if (c !== null && go(c),
                    c = Bl(e, t, n, r),
                    c === null && li(e, t, r, ps, n),
                    c === o)
                        break;
                    o = c
                }
                o !== null && r.stopPropagation()
            } else
                li(e, t, r, null, n)
        }
    }
    var ps = null;
    function Bl(e, t, n, r) {
        if (ps = null,
        e = _l(r),
        e = fn(e),
        e !== null)
            if (t = dn(e),
            t === null)
                e = null;
            else if (n = t.tag,
            n === 13) {
                if (e = lo(t),
                e !== null)
                    return e;
                e = null
            } else if (n === 3) {
                if (t.stateNode.current.memoizedState.isDehydrated)
                    return t.tag === 3 ? t.stateNode.containerInfo : null;
                e = null
            } else
                t !== e && (e = null);
        return ps = e,
        null
    }
    function jo(e) {
        switch (e) {
        case "cancel":
        case "click":
        case "close":
        case "contextmenu":
        case "copy":
        case "cut":
        case "auxclick":
        case "dblclick":
        case "dragend":
        case "dragstart":
        case "drop":
        case "focusin":
        case "focusout":
        case "input":
        case "invalid":
        case "keydown":
        case "keypress":
        case "keyup":
        case "mousedown":
        case "mouseup":
        case "paste":
        case "pause":
        case "play":
        case "pointercancel":
        case "pointerdown":
        case "pointerup":
        case "ratechange":
        case "reset":
        case "resize":
        case "seeked":
        case "submit":
        case "touchcancel":
        case "touchend":
        case "touchstart":
        case "volumechange":
        case "change":
        case "selectionchange":
        case "textInput":
        case "compositionstart":
        case "compositionend":
        case "compositionupdate":
        case "beforeblur":
        case "afterblur":
        case "beforeinput":
        case "blur":
        case "fullscreenchange":
        case "focus":
        case "hashchange":
        case "popstate":
        case "select":
        case "selectstart":
            return 1;
        case "drag":
        case "dragenter":
        case "dragexit":
        case "dragleave":
        case "dragover":
        case "mousemove":
        case "mouseout":
        case "mouseover":
        case "pointermove":
        case "pointerout":
        case "pointerover":
        case "scroll":
        case "toggle":
        case "touchmove":
        case "wheel":
        case "mouseenter":
        case "mouseleave":
        case "pointerenter":
        case "pointerleave":
            return 4;
        case "message":
            switch (Vf()) {
            case Ml:
                return 1;
            case fo:
                return 4;
            case ls:
            case Hf:
                return 16;
            case po:
                return 536870912;
            default:
                return 16
            }
        default:
            return 16
        }
    }
    var Ht = null
      , Vl = null
      , hs = null;
    function ko() {
        if (hs)
            return hs;
        var e, t = Vl, n = t.length, r, o = "value" in Ht ? Ht.value : Ht.textContent, c = o.length;
        for (e = 0; e < n && t[e] === o[e]; e++)
            ;
        var p = n - e;
        for (r = 1; r <= p && t[n - r] === o[c - r]; r++)
            ;
        return hs = o.slice(e, 1 < r ? 1 - r : void 0)
    }
    function ms(e) {
        var t = e.keyCode;
        return "charCode" in e ? (e = e.charCode,
        e === 0 && t === 13 && (e = 13)) : e = t,
        e === 10 && (e = 13),
        32 <= e || e === 13 ? e : 0
    }
    function gs() {
        return !0
    }
    function So() {
        return !1
    }
    function lt(e) {
        function t(n, r, o, c, p) {
            this._reactName = n,
            this._targetInst = o,
            this.type = r,
            this.nativeEvent = c,
            this.target = p,
            this.currentTarget = null;
            for (var y in e)
                e.hasOwnProperty(y) && (n = e[y],
                this[y] = n ? n(c) : c[y]);
            return this.isDefaultPrevented = (c.defaultPrevented != null ? c.defaultPrevented : c.returnValue === !1) ? gs : So,
            this.isPropagationStopped = So,
            this
        }
        return U(t.prototype, {
            preventDefault: function() {
                this.defaultPrevented = !0;
                var n = this.nativeEvent;
                n && (n.preventDefault ? n.preventDefault() : typeof n.returnValue != "unknown" && (n.returnValue = !1),
                this.isDefaultPrevented = gs)
            },
            stopPropagation: function() {
                var n = this.nativeEvent;
                n && (n.stopPropagation ? n.stopPropagation() : typeof n.cancelBubble != "unknown" && (n.cancelBubble = !0),
                this.isPropagationStopped = gs)
            },
            persist: function() {},
            isPersistent: gs
        }),
        t
    }
    var On = {
        eventPhase: 0,
        bubbles: 0,
        cancelable: 0,
        timeStamp: function(e) {
            return e.timeStamp || Date.now()
        },
        defaultPrevented: 0,
        isTrusted: 0
    }, Hl = lt(On), xr = U({}, On, {
        view: 0,
        detail: 0
    }), rp = lt(xr), Kl, Wl, yr, xs = U({}, xr, {
        screenX: 0,
        screenY: 0,
        clientX: 0,
        clientY: 0,
        pageX: 0,
        pageY: 0,
        ctrlKey: 0,
        shiftKey: 0,
        altKey: 0,
        metaKey: 0,
        getModifierState: Yl,
        button: 0,
        buttons: 0,
        relatedTarget: function(e) {
            return e.relatedTarget === void 0 ? e.fromElement === e.srcElement ? e.toElement : e.fromElement : e.relatedTarget
        },
        movementX: function(e) {
            return "movementX" in e ? e.movementX : (e !== yr && (yr && e.type === "mousemove" ? (Kl = e.screenX - yr.screenX,
            Wl = e.screenY - yr.screenY) : Wl = Kl = 0,
            yr = e),
            Kl)
        },
        movementY: function(e) {
            return "movementY" in e ? e.movementY : Wl
        }
    }), Co = lt(xs), sp = U({}, xs, {
        dataTransfer: 0
    }), lp = lt(sp), ip = U({}, xr, {
        relatedTarget: 0
    }), ql = lt(ip), ap = U({}, On, {
        animationName: 0,
        elapsedTime: 0,
        pseudoElement: 0
    }), op = lt(ap), up = U({}, On, {
        clipboardData: function(e) {
            return "clipboardData" in e ? e.clipboardData : window.clipboardData
        }
    }), cp = lt(up), dp = U({}, On, {
        data: 0
    }), Eo = lt(dp), fp = {
        Esc: "Escape",
        Spacebar: " ",
        Left: "ArrowLeft",
        Up: "ArrowUp",
        Right: "ArrowRight",
        Down: "ArrowDown",
        Del: "Delete",
        Win: "OS",
        Menu: "ContextMenu",
        Apps: "ContextMenu",
        Scroll: "ScrollLock",
        MozPrintableKey: "Unidentified"
    }, pp = {
        8: "Backspace",
        9: "Tab",
        12: "Clear",
        13: "Enter",
        16: "Shift",
        17: "Control",
        18: "Alt",
        19: "Pause",
        20: "CapsLock",
        27: "Escape",
        32: " ",
        33: "PageUp",
        34: "PageDown",
        35: "End",
        36: "Home",
        37: "ArrowLeft",
        38: "ArrowUp",
        39: "ArrowRight",
        40: "ArrowDown",
        45: "Insert",
        46: "Delete",
        112: "F1",
        113: "F2",
        114: "F3",
        115: "F4",
        116: "F5",
        117: "F6",
        118: "F7",
        119: "F8",
        120: "F9",
        121: "F10",
        122: "F11",
        123: "F12",
        144: "NumLock",
        145: "ScrollLock",
        224: "Meta"
    }, hp = {
        Alt: "altKey",
        Control: "ctrlKey",
        Meta: "metaKey",
        Shift: "shiftKey"
    };
    function mp(e) {
        var t = this.nativeEvent;
        return t.getModifierState ? t.getModifierState(e) : (e = hp[e]) ? !!t[e] : !1
    }
    function Yl() {
        return mp
    }
    var gp = U({}, xr, {
        key: function(e) {
            if (e.key) {
                var t = fp[e.key] || e.key;
                if (t !== "Unidentified")
                    return t
            }
            return e.type === "keypress" ? (e = ms(e),
            e === 13 ? "Enter" : String.fromCharCode(e)) : e.type === "keydown" || e.type === "keyup" ? pp[e.keyCode] || "Unidentified" : ""
        },
        code: 0,
        location: 0,
        ctrlKey: 0,
        shiftKey: 0,
        altKey: 0,
        metaKey: 0,
        repeat: 0,
        locale: 0,
        getModifierState: Yl,
        charCode: function(e) {
            return e.type === "keypress" ? ms(e) : 0
        },
        keyCode: function(e) {
            return e.type === "keydown" || e.type === "keyup" ? e.keyCode : 0
        },
        which: function(e) {
            return e.type === "keypress" ? ms(e) : e.type === "keydown" || e.type === "keyup" ? e.keyCode : 0
        }
    })
      , xp = lt(gp)
      , yp = U({}, xs, {
        pointerId: 0,
        width: 0,
        height: 0,
        pressure: 0,
        tangentialPressure: 0,
        tiltX: 0,
        tiltY: 0,
        twist: 0,
        pointerType: 0,
        isPrimary: 0
    })
      , Po = lt(yp)
      , vp = U({}, xr, {
        touches: 0,
        targetTouches: 0,
        changedTouches: 0,
        altKey: 0,
        metaKey: 0,
        ctrlKey: 0,
        shiftKey: 0,
        getModifierState: Yl
    })
      , wp = lt(vp)
      , bp = U({}, On, {
        propertyName: 0,
        elapsedTime: 0,
        pseudoElement: 0
    })
      , Np = lt(bp)
      , jp = U({}, xs, {
        deltaX: function(e) {
            return "deltaX" in e ? e.deltaX : "wheelDeltaX" in e ? -e.wheelDeltaX : 0
        },
        deltaY: function(e) {
            return "deltaY" in e ? e.deltaY : "wheelDeltaY" in e ? -e.wheelDeltaY : "wheelDelta" in e ? -e.wheelDelta : 0
        },
        deltaZ: 0,
        deltaMode: 0
    })
      , kp = lt(jp)
      , Sp = [9, 13, 27, 32]
      , Ql = g && "CompositionEvent" in window
      , vr = null;
    g && "documentMode" in document && (vr = document.documentMode);
    var Cp = g && "TextEvent" in window && !vr
      , Lo = g && (!Ql || vr && 8 < vr && 11 >= vr)
      , _o = " "
      , Ro = !1;
    function Oo(e, t) {
        switch (e) {
        case "keyup":
            return Sp.indexOf(t.keyCode) !== -1;
        case "keydown":
            return t.keyCode !== 229;
        case "keypress":
        case "mousedown":
        case "focusout":
            return !0;
        default:
            return !1
        }
    }
    function To(e) {
        return e = e.detail,
        typeof e == "object" && "data" in e ? e.data : null
    }
    var Tn = !1;
    function Ep(e, t) {
        switch (e) {
        case "compositionend":
            return To(t);
        case "keypress":
            return t.which !== 32 ? null : (Ro = !0,
            _o);
        case "textInput":
            return e = t.data,
            e === _o && Ro ? null : e;
        default:
            return null
        }
    }
    function Pp(e, t) {
        if (Tn)
            return e === "compositionend" || !Ql && Oo(e, t) ? (e = ko(),
            hs = Vl = Ht = null,
            Tn = !1,
            e) : null;
        switch (e) {
        case "paste":
            return null;
        case "keypress":
            if (!(t.ctrlKey || t.altKey || t.metaKey) || t.ctrlKey && t.altKey) {
                if (t.char && 1 < t.char.length)
                    return t.char;
                if (t.which)
                    return String.fromCharCode(t.which)
            }
            return null;
        case "compositionend":
            return Lo && t.locale !== "ko" ? null : t.data;
        default:
            return null
        }
    }
    var Lp = {
        color: !0,
        date: !0,
        datetime: !0,
        "datetime-local": !0,
        email: !0,
        month: !0,
        number: !0,
        password: !0,
        range: !0,
        search: !0,
        tel: !0,
        text: !0,
        time: !0,
        url: !0,
        week: !0
    };
    function zo(e) {
        var t = e && e.nodeName && e.nodeName.toLowerCase();
        return t === "input" ? !!Lp[e.type] : t === "textarea"
    }
    function Mo(e, t, n, r) {
        eo(r),
        t = Ns(t, "onChange"),
        0 < t.length && (n = new Hl("onChange","change",null,n,r),
        e.push({
            event: n,
            listeners: t
        }))
    }
    var wr = null
      , br = null;
    function _p(e) {
        Zo(e, 0)
    }
    function ys(e) {
        var t = $n(e);
        if (Ba(t))
            return e
    }
    function Rp(e, t) {
        if (e === "change")
            return t
    }
    var Ao = !1;
    if (g) {
        var Gl;
        if (g) {
            var Jl = "oninput" in document;
            if (!Jl) {
                var Do = document.createElement("div");
                Do.setAttribute("oninput", "return;"),
                Jl = typeof Do.oninput == "function"
            }
            Gl = Jl
        } else
            Gl = !1;
        Ao = Gl && (!document.documentMode || 9 < document.documentMode)
    }
    function $o() {
        wr && (wr.detachEvent("onpropertychange", Io),
        br = wr = null)
    }
    function Io(e) {
        if (e.propertyName === "value" && ys(br)) {
            var t = [];
            Mo(t, br, e, _l(e)),
            so(_p, t)
        }
    }
    function Op(e, t, n) {
        e === "focusin" ? ($o(),
        wr = t,
        br = n,
        wr.attachEvent("onpropertychange", Io)) : e === "focusout" && $o()
    }
    function Tp(e) {
        if (e === "selectionchange" || e === "keyup" || e === "keydown")
            return ys(br)
    }
    function zp(e, t) {
        if (e === "click")
            return ys(t)
    }
    function Mp(e, t) {
        if (e === "input" || e === "change")
            return ys(t)
    }
    function Ap(e, t) {
        return e === t && (e !== 0 || 1 / e === 1 / t) || e !== e && t !== t
    }
    var xt = typeof Object.is == "function" ? Object.is : Ap;
    function Nr(e, t) {
        if (xt(e, t))
            return !0;
        if (typeof e != "object" || e === null || typeof t != "object" || t === null)
            return !1;
        var n = Object.keys(e)
          , r = Object.keys(t);
        if (n.length !== r.length)
            return !1;
        for (r = 0; r < n.length; r++) {
            var o = n[r];
            if (!m.call(t, o) || !xt(e[o], t[o]))
                return !1
        }
        return !0
    }
    function Fo(e) {
        for (; e && e.firstChild; )
            e = e.firstChild;
        return e
    }
    function Uo(e, t) {
        var n = Fo(e);
        e = 0;
        for (var r; n; ) {
            if (n.nodeType === 3) {
                if (r = e + n.textContent.length,
                e <= t && r >= t)
                    return {
                        node: n,
                        offset: t - e
                    };
                e = r
            }
            e: {
                for (; n; ) {
                    if (n.nextSibling) {
                        n = n.nextSibling;
                        break e
                    }
                    n = n.parentNode
                }
                n = void 0
            }
            n = Fo(n)
        }
    }
    function Bo(e, t) {
        return e && t ? e === t ? !0 : e && e.nodeType === 3 ? !1 : t && t.nodeType === 3 ? Bo(e, t.parentNode) : "contains" in e ? e.contains(t) : e.compareDocumentPosition ? !!(e.compareDocumentPosition(t) & 16) : !1 : !1
    }
    function Vo() {
        for (var e = window, t = ts(); t instanceof e.HTMLIFrameElement; ) {
            try {
                var n = typeof t.contentWindow.location.href == "string"
            } catch {
                n = !1
            }
            if (n)
                e = t.contentWindow;
            else
                break;
            t = ts(e.document)
        }
        return t
    }
    function Xl(e) {
        var t = e && e.nodeName && e.nodeName.toLowerCase();
        return t && (t === "input" && (e.type === "text" || e.type === "search" || e.type === "tel" || e.type === "url" || e.type === "password") || t === "textarea" || e.contentEditable === "true")
    }
    function Dp(e) {
        var t = Vo()
          , n = e.focusedElem
          , r = e.selectionRange;
        if (t !== n && n && n.ownerDocument && Bo(n.ownerDocument.documentElement, n)) {
            if (r !== null && Xl(n)) {
                if (t = r.start,
                e = r.end,
                e === void 0 && (e = t),
                "selectionStart" in n)
                    n.selectionStart = t,
                    n.selectionEnd = Math.min(e, n.value.length);
                else if (e = (t = n.ownerDocument || document) && t.defaultView || window,
                e.getSelection) {
                    e = e.getSelection();
                    var o = n.textContent.length
                      , c = Math.min(r.start, o);
                    r = r.end === void 0 ? c : Math.min(r.end, o),
                    !e.extend && c > r && (o = r,
                    r = c,
                    c = o),
                    o = Uo(n, c);
                    var p = Uo(n, r);
                    o && p && (e.rangeCount !== 1 || e.anchorNode !== o.node || e.anchorOffset !== o.offset || e.focusNode !== p.node || e.focusOffset !== p.offset) && (t = t.createRange(),
                    t.setStart(o.node, o.offset),
                    e.removeAllRanges(),
                    c > r ? (e.addRange(t),
                    e.extend(p.node, p.offset)) : (t.setEnd(p.node, p.offset),
                    e.addRange(t)))
                }
            }
            for (t = [],
            e = n; e = e.parentNode; )
                e.nodeType === 1 && t.push({
                    element: e,
                    left: e.scrollLeft,
                    top: e.scrollTop
                });
            for (typeof n.focus == "function" && n.focus(),
            n = 0; n < t.length; n++)
                e = t[n],
                e.element.scrollLeft = e.left,
                e.element.scrollTop = e.top
        }
    }
    var $p = g && "documentMode" in document && 11 >= document.documentMode
      , zn = null
      , Zl = null
      , jr = null
      , ei = !1;
    function Ho(e, t, n) {
        var r = n.window === n ? n.document : n.nodeType === 9 ? n : n.ownerDocument;
        ei || zn == null || zn !== ts(r) || (r = zn,
        "selectionStart" in r && Xl(r) ? r = {
            start: r.selectionStart,
            end: r.selectionEnd
        } : (r = (r.ownerDocument && r.ownerDocument.defaultView || window).getSelection(),
        r = {
            anchorNode: r.anchorNode,
            anchorOffset: r.anchorOffset,
            focusNode: r.focusNode,
            focusOffset: r.focusOffset
        }),
        jr && Nr(jr, r) || (jr = r,
        r = Ns(Zl, "onSelect"),
        0 < r.length && (t = new Hl("onSelect","select",null,t,n),
        e.push({
            event: t,
            listeners: r
        }),
        t.target = zn)))
    }
    function vs(e, t) {
        var n = {};
        return n[e.toLowerCase()] = t.toLowerCase(),
        n["Webkit" + e] = "webkit" + t,
        n["Moz" + e] = "moz" + t,
        n
    }
    var Mn = {
        animationend: vs("Animation", "AnimationEnd"),
        animationiteration: vs("Animation", "AnimationIteration"),
        animationstart: vs("Animation", "AnimationStart"),
        transitionend: vs("Transition", "TransitionEnd")
    }
      , ti = {}
      , Ko = {};
    g && (Ko = document.createElement("div").style,
    "AnimationEvent" in window || (delete Mn.animationend.animation,
    delete Mn.animationiteration.animation,
    delete Mn.animationstart.animation),
    "TransitionEvent" in window || delete Mn.transitionend.transition);
    function ws(e) {
        if (ti[e])
            return ti[e];
        if (!Mn[e])
            return e;
        var t = Mn[e], n;
        for (n in t)
            if (t.hasOwnProperty(n) && n in Ko)
                return ti[e] = t[n];
        return e
    }
    var Wo = ws("animationend")
      , qo = ws("animationiteration")
      , Yo = ws("animationstart")
      , Qo = ws("transitionend")
      , Go = new Map
      , Jo = "abort auxClick cancel canPlay canPlayThrough click close contextMenu copy cut drag dragEnd dragEnter dragExit dragLeave dragOver dragStart drop durationChange emptied encrypted ended error gotPointerCapture input invalid keyDown keyPress keyUp load loadedData loadedMetadata loadStart lostPointerCapture mouseDown mouseMove mouseOut mouseOver mouseUp paste pause play playing pointerCancel pointerDown pointerMove pointerOut pointerOver pointerUp progress rateChange reset resize seeked seeking stalled submit suspend timeUpdate touchCancel touchEnd touchStart volumeChange scroll toggle touchMove waiting wheel".split(" ");
    function Kt(e, t) {
        Go.set(e, t),
        f(t, [e])
    }
    for (var ni = 0; ni < Jo.length; ni++) {
        var ri = Jo[ni]
          , Ip = ri.toLowerCase()
          , Fp = ri[0].toUpperCase() + ri.slice(1);
        Kt(Ip, "on" + Fp)
    }
    Kt(Wo, "onAnimationEnd"),
    Kt(qo, "onAnimationIteration"),
    Kt(Yo, "onAnimationStart"),
    Kt("dblclick", "onDoubleClick"),
    Kt("focusin", "onFocus"),
    Kt("focusout", "onBlur"),
    Kt(Qo, "onTransitionEnd"),
    h("onMouseEnter", ["mouseout", "mouseover"]),
    h("onMouseLeave", ["mouseout", "mouseover"]),
    h("onPointerEnter", ["pointerout", "pointerover"]),
    h("onPointerLeave", ["pointerout", "pointerover"]),
    f("onChange", "change click focusin focusout input keydown keyup selectionchange".split(" ")),
    f("onSelect", "focusout contextmenu dragend focusin keydown keyup mousedown mouseup selectionchange".split(" ")),
    f("onBeforeInput", ["compositionend", "keypress", "textInput", "paste"]),
    f("onCompositionEnd", "compositionend focusout keydown keypress keyup mousedown".split(" ")),
    f("onCompositionStart", "compositionstart focusout keydown keypress keyup mousedown".split(" ")),
    f("onCompositionUpdate", "compositionupdate focusout keydown keypress keyup mousedown".split(" "));
    var kr = "abort canplay canplaythrough durationchange emptied encrypted ended error loadeddata loadedmetadata loadstart pause play playing progress ratechange resize seeked seeking stalled suspend timeupdate volumechange waiting".split(" ")
      , Up = new Set("cancel close invalid load scroll toggle".split(" ").concat(kr));
    function Xo(e, t, n) {
        var r = e.type || "unknown-event";
        e.currentTarget = n,
        If(r, t, void 0, e),
        e.currentTarget = null
    }
    function Zo(e, t) {
        t = (t & 4) !== 0;
        for (var n = 0; n < e.length; n++) {
            var r = e[n]
              , o = r.event;
            r = r.listeners;
            e: {
                var c = void 0;
                if (t)
                    for (var p = r.length - 1; 0 <= p; p--) {
                        var y = r[p]
                          , N = y.instance
                          , L = y.currentTarget;
                        if (y = y.listener,
                        N !== c && o.isPropagationStopped())
                            break e;
                        Xo(o, y, L),
                        c = N
                    }
                else
                    for (p = 0; p < r.length; p++) {
                        if (y = r[p],
                        N = y.instance,
                        L = y.currentTarget,
                        y = y.listener,
                        N !== c && o.isPropagationStopped())
                            break e;
                        Xo(o, y, L),
                        c = N
                    }
            }
        }
        if (ss)
            throw e = zl,
            ss = !1,
            zl = null,
            e
    }
    function be(e, t) {
        var n = t[di];
        n === void 0 && (n = t[di] = new Set);
        var r = e + "__bubble";
        n.has(r) || (eu(t, e, 2, !1),
        n.add(r))
    }
    function si(e, t, n) {
        var r = 0;
        t && (r |= 4),
        eu(n, e, r, t)
    }
    var bs = "_reactListening" + Math.random().toString(36).slice(2);
    function Sr(e) {
        if (!e[bs]) {
            e[bs] = !0,
            u.forEach(function(n) {
                n !== "selectionchange" && (Up.has(n) || si(n, !1, e),
                si(n, !0, e))
            });
            var t = e.nodeType === 9 ? e : e.ownerDocument;
            t === null || t[bs] || (t[bs] = !0,
            si("selectionchange", !1, t))
        }
    }
    function eu(e, t, n, r) {
        switch (jo(t)) {
        case 1:
            var o = tp;
            break;
        case 4:
            o = np;
            break;
        default:
            o = Ul
        }
        n = o.bind(null, t, n, e),
        o = void 0,
        !Tl || t !== "touchstart" && t !== "touchmove" && t !== "wheel" || (o = !0),
        r ? o !== void 0 ? e.addEventListener(t, n, {
            capture: !0,
            passive: o
        }) : e.addEventListener(t, n, !0) : o !== void 0 ? e.addEventListener(t, n, {
            passive: o
        }) : e.addEventListener(t, n, !1)
    }
    function li(e, t, n, r, o) {
        var c = r;
        if ((t & 1) === 0 && (t & 2) === 0 && r !== null)
            e: for (; ; ) {
                if (r === null)
                    return;
                var p = r.tag;
                if (p === 3 || p === 4) {
                    var y = r.stateNode.containerInfo;
                    if (y === o || y.nodeType === 8 && y.parentNode === o)
                        break;
                    if (p === 4)
                        for (p = r.return; p !== null; ) {
                            var N = p.tag;
                            if ((N === 3 || N === 4) && (N = p.stateNode.containerInfo,
                            N === o || N.nodeType === 8 && N.parentNode === o))
                                return;
                            p = p.return
                        }
                    for (; y !== null; ) {
                        if (p = fn(y),
                        p === null)
                            return;
                        if (N = p.tag,
                        N === 5 || N === 6) {
                            r = c = p;
                            continue e
                        }
                        y = y.parentNode
                    }
                }
                r = r.return
            }
        so(function() {
            var L = c
              , M = _l(n)
              , A = [];
            e: {
                var z = Go.get(e);
                if (z !== void 0) {
                    var B = Hl
                      , q = e;
                    switch (e) {
                    case "keypress":
                        if (ms(n) === 0)
                            break e;
                    case "keydown":
                    case "keyup":
                        B = xp;
                        break;
                    case "focusin":
                        q = "focus",
                        B = ql;
                        break;
                    case "focusout":
                        q = "blur",
                        B = ql;
                        break;
                    case "beforeblur":
                    case "afterblur":
                        B = ql;
                        break;
                    case "click":
                        if (n.button === 2)
                            break e;
                    case "auxclick":
                    case "dblclick":
                    case "mousedown":
                    case "mousemove":
                    case "mouseup":
                    case "mouseout":
                    case "mouseover":
                    case "contextmenu":
                        B = Co;
                        break;
                    case "drag":
                    case "dragend":
                    case "dragenter":
                    case "dragexit":
                    case "dragleave":
                    case "dragover":
                    case "dragstart":
                    case "drop":
                        B = lp;
                        break;
                    case "touchcancel":
                    case "touchend":
                    case "touchmove":
                    case "touchstart":
                        B = wp;
                        break;
                    case Wo:
                    case qo:
                    case Yo:
                        B = op;
                        break;
                    case Qo:
                        B = Np;
                        break;
                    case "scroll":
                        B = rp;
                        break;
                    case "wheel":
                        B = kp;
                        break;
                    case "copy":
                    case "cut":
                    case "paste":
                        B = cp;
                        break;
                    case "gotpointercapture":
                    case "lostpointercapture":
                    case "pointercancel":
                    case "pointerdown":
                    case "pointermove":
                    case "pointerout":
                    case "pointerover":
                    case "pointerup":
                        B = Po
                    }
                    var Q = (t & 4) !== 0
                      , Re = !Q && e === "scroll"
                      , S = Q ? z !== null ? z + "Capture" : null : z;
                    Q = [];
                    for (var j = L, C; j !== null; ) {
                        C = j;
                        var D = C.stateNode;
                        if (C.tag === 5 && D !== null && (C = D,
                        S !== null && (D = ar(j, S),
                        D != null && Q.push(Cr(j, D, C)))),
                        Re)
                            break;
                        j = j.return
                    }
                    0 < Q.length && (z = new B(z,q,null,n,M),
                    A.push({
                        event: z,
                        listeners: Q
                    }))
                }
            }
            if ((t & 7) === 0) {
                e: {
                    if (z = e === "mouseover" || e === "pointerover",
                    B = e === "mouseout" || e === "pointerout",
                    z && n !== Ll && (q = n.relatedTarget || n.fromElement) && (fn(q) || q[Rt]))
                        break e;
                    if ((B || z) && (z = M.window === M ? M : (z = M.ownerDocument) ? z.defaultView || z.parentWindow : window,
                    B ? (q = n.relatedTarget || n.toElement,
                    B = L,
                    q = q ? fn(q) : null,
                    q !== null && (Re = dn(q),
                    q !== Re || q.tag !== 5 && q.tag !== 6) && (q = null)) : (B = null,
                    q = L),
                    B !== q)) {
                        if (Q = Co,
                        D = "onMouseLeave",
                        S = "onMouseEnter",
                        j = "mouse",
                        (e === "pointerout" || e === "pointerover") && (Q = Po,
                        D = "onPointerLeave",
                        S = "onPointerEnter",
                        j = "pointer"),
                        Re = B == null ? z : $n(B),
                        C = q == null ? z : $n(q),
                        z = new Q(D,j + "leave",B,n,M),
                        z.target = Re,
                        z.relatedTarget = C,
                        D = null,
                        fn(M) === L && (Q = new Q(S,j + "enter",q,n,M),
                        Q.target = C,
                        Q.relatedTarget = Re,
                        D = Q),
                        Re = D,
                        B && q)
                            t: {
                                for (Q = B,
                                S = q,
                                j = 0,
                                C = Q; C; C = An(C))
                                    j++;
                                for (C = 0,
                                D = S; D; D = An(D))
                                    C++;
                                for (; 0 < j - C; )
                                    Q = An(Q),
                                    j--;
                                for (; 0 < C - j; )
                                    S = An(S),
                                    C--;
                                for (; j--; ) {
                                    if (Q === S || S !== null && Q === S.alternate)
                                        break t;
                                    Q = An(Q),
                                    S = An(S)
                                }
                                Q = null
                            }
                        else
                            Q = null;
                        B !== null && tu(A, z, B, Q, !1),
                        q !== null && Re !== null && tu(A, Re, q, Q, !0)
                    }
                }
                e: {
                    if (z = L ? $n(L) : window,
                    B = z.nodeName && z.nodeName.toLowerCase(),
                    B === "select" || B === "input" && z.type === "file")
                        var G = Rp;
                    else if (zo(z))
                        if (Ao)
                            G = Mp;
                        else {
                            G = Tp;
                            var X = Op
                        }
                    else
                        (B = z.nodeName) && B.toLowerCase() === "input" && (z.type === "checkbox" || z.type === "radio") && (G = zp);
                    if (G && (G = G(e, L))) {
                        Mo(A, G, n, M);
                        break e
                    }
                    X && X(e, z, L),
                    e === "focusout" && (X = z._wrapperState) && X.controlled && z.type === "number" && kl(z, "number", z.value)
                }
                switch (X = L ? $n(L) : window,
                e) {
                case "focusin":
                    (zo(X) || X.contentEditable === "true") && (zn = X,
                    Zl = L,
                    jr = null);
                    break;
                case "focusout":
                    jr = Zl = zn = null;
                    break;
                case "mousedown":
                    ei = !0;
                    break;
                case "contextmenu":
                case "mouseup":
                case "dragend":
                    ei = !1,
                    Ho(A, n, M);
                    break;
                case "selectionchange":
                    if ($p)
                        break;
                case "keydown":
                case "keyup":
                    Ho(A, n, M)
                }
                var Z;
                if (Ql)
                    e: {
                        switch (e) {
                        case "compositionstart":
                            var ne = "onCompositionStart";
                            break e;
                        case "compositionend":
                            ne = "onCompositionEnd";
                            break e;
                        case "compositionupdate":
                            ne = "onCompositionUpdate";
                            break e
                        }
                        ne = void 0
                    }
                else
                    Tn ? Oo(e, n) && (ne = "onCompositionEnd") : e === "keydown" && n.keyCode === 229 && (ne = "onCompositionStart");
                ne && (Lo && n.locale !== "ko" && (Tn || ne !== "onCompositionStart" ? ne === "onCompositionEnd" && Tn && (Z = ko()) : (Ht = M,
                Vl = "value" in Ht ? Ht.value : Ht.textContent,
                Tn = !0)),
                X = Ns(L, ne),
                0 < X.length && (ne = new Eo(ne,e,null,n,M),
                A.push({
                    event: ne,
                    listeners: X
                }),
                Z ? ne.data = Z : (Z = To(n),
                Z !== null && (ne.data = Z)))),
                (Z = Cp ? Ep(e, n) : Pp(e, n)) && (L = Ns(L, "onBeforeInput"),
                0 < L.length && (M = new Eo("onBeforeInput","beforeinput",null,n,M),
                A.push({
                    event: M,
                    listeners: L
                }),
                M.data = Z))
            }
            Zo(A, t)
        })
    }
    function Cr(e, t, n) {
        return {
            instance: e,
            listener: t,
            currentTarget: n
        }
    }
    function Ns(e, t) {
        for (var n = t + "Capture", r = []; e !== null; ) {
            var o = e
              , c = o.stateNode;
            o.tag === 5 && c !== null && (o = c,
            c = ar(e, n),
            c != null && r.unshift(Cr(e, c, o)),
            c = ar(e, t),
            c != null && r.push(Cr(e, c, o))),
            e = e.return
        }
        return r
    }
    function An(e) {
        if (e === null)
            return null;
        do
            e = e.return;
        while (e && e.tag !== 5);
        return e || null
    }
    function tu(e, t, n, r, o) {
        for (var c = t._reactName, p = []; n !== null && n !== r; ) {
            var y = n
              , N = y.alternate
              , L = y.stateNode;
            if (N !== null && N === r)
                break;
            y.tag === 5 && L !== null && (y = L,
            o ? (N = ar(n, c),
            N != null && p.unshift(Cr(n, N, y))) : o || (N = ar(n, c),
            N != null && p.push(Cr(n, N, y)))),
            n = n.return
        }
        p.length !== 0 && e.push({
            event: t,
            listeners: p
        })
    }
    var Bp = /\r\n?/g
      , Vp = /\u0000|\uFFFD/g;
    function nu(e) {
        return (typeof e == "string" ? e : "" + e).replace(Bp, `
`).replace(Vp, "")
    }
    function js(e, t, n) {
        if (t = nu(t),
        nu(e) !== t && n)
            throw Error(l(425))
    }
    function ks() {}
    var ii = null
      , ai = null;
    function oi(e, t) {
        return e === "textarea" || e === "noscript" || typeof t.children == "string" || typeof t.children == "number" || typeof t.dangerouslySetInnerHTML == "object" && t.dangerouslySetInnerHTML !== null && t.dangerouslySetInnerHTML.__html != null
    }
    var ui = typeof setTimeout == "function" ? setTimeout : void 0
      , Hp = typeof clearTimeout == "function" ? clearTimeout : void 0
      , ru = typeof Promise == "function" ? Promise : void 0
      , Kp = typeof queueMicrotask == "function" ? queueMicrotask : typeof ru < "u" ? function(e) {
        return ru.resolve(null).then(e).catch(Wp)
    }
    : ui;
    function Wp(e) {
        setTimeout(function() {
            throw e
        })
    }
    function ci(e, t) {
        var n = t
          , r = 0;
        do {
            var o = n.nextSibling;
            if (e.removeChild(n),
            o && o.nodeType === 8)
                if (n = o.data,
                n === "/$") {
                    if (r === 0) {
                        e.removeChild(o),
                        gr(t);
                        return
                    }
                    r--
                } else
                    n !== "$" && n !== "$?" && n !== "$!" || r++;
            n = o
        } while (n);
        gr(t)
    }
    function Wt(e) {
        for (; e != null; e = e.nextSibling) {
            var t = e.nodeType;
            if (t === 1 || t === 3)
                break;
            if (t === 8) {
                if (t = e.data,
                t === "$" || t === "$!" || t === "$?")
                    break;
                if (t === "/$")
                    return null
            }
        }
        return e
    }
    function su(e) {
        e = e.previousSibling;
        for (var t = 0; e; ) {
            if (e.nodeType === 8) {
                var n = e.data;
                if (n === "$" || n === "$!" || n === "$?") {
                    if (t === 0)
                        return e;
                    t--
                } else
                    n === "/$" && t++
            }
            e = e.previousSibling
        }
        return null
    }
    var Dn = Math.random().toString(36).slice(2)
      , kt = "__reactFiber$" + Dn
      , Er = "__reactProps$" + Dn
      , Rt = "__reactContainer$" + Dn
      , di = "__reactEvents$" + Dn
      , qp = "__reactListeners$" + Dn
      , Yp = "__reactHandles$" + Dn;
    function fn(e) {
        var t = e[kt];
        if (t)
            return t;
        for (var n = e.parentNode; n; ) {
            if (t = n[Rt] || n[kt]) {
                if (n = t.alternate,
                t.child !== null || n !== null && n.child !== null)
                    for (e = su(e); e !== null; ) {
                        if (n = e[kt])
                            return n;
                        e = su(e)
                    }
                return t
            }
            e = n,
            n = e.parentNode
        }
        return null
    }
    function Pr(e) {
        return e = e[kt] || e[Rt],
        !e || e.tag !== 5 && e.tag !== 6 && e.tag !== 13 && e.tag !== 3 ? null : e
    }
    function $n(e) {
        if (e.tag === 5 || e.tag === 6)
            return e.stateNode;
        throw Error(l(33))
    }
    function Ss(e) {
        return e[Er] || null
    }
    var fi = []
      , In = -1;
    function qt(e) {
        return {
            current: e
        }
    }
    function Ne(e) {
        0 > In || (e.current = fi[In],
        fi[In] = null,
        In--)
    }
    function we(e, t) {
        In++,
        fi[In] = e.current,
        e.current = t
    }
    var Yt = {}
      , Ke = qt(Yt)
      , Xe = qt(!1)
      , pn = Yt;
    function Fn(e, t) {
        var n = e.type.contextTypes;
        if (!n)
            return Yt;
        var r = e.stateNode;
        if (r && r.__reactInternalMemoizedUnmaskedChildContext === t)
            return r.__reactInternalMemoizedMaskedChildContext;
        var o = {}, c;
        for (c in n)
            o[c] = t[c];
        return r && (e = e.stateNode,
        e.__reactInternalMemoizedUnmaskedChildContext = t,
        e.__reactInternalMemoizedMaskedChildContext = o),
        o
    }
    function Ze(e) {
        return e = e.childContextTypes,
        e != null
    }
    function Cs() {
        Ne(Xe),
        Ne(Ke)
    }
    function lu(e, t, n) {
        if (Ke.current !== Yt)
            throw Error(l(168));
        we(Ke, t),
        we(Xe, n)
    }
    function iu(e, t, n) {
        var r = e.stateNode;
        if (t = t.childContextTypes,
        typeof r.getChildContext != "function")
            return n;
        r = r.getChildContext();
        for (var o in r)
            if (!(o in t))
                throw Error(l(108, ve(e) || "Unknown", o));
        return U({}, n, r)
    }
    function Es(e) {
        return e = (e = e.stateNode) && e.__reactInternalMemoizedMergedChildContext || Yt,
        pn = Ke.current,
        we(Ke, e),
        we(Xe, Xe.current),
        !0
    }
    function au(e, t, n) {
        var r = e.stateNode;
        if (!r)
            throw Error(l(169));
        n ? (e = iu(e, t, pn),
        r.__reactInternalMemoizedMergedChildContext = e,
        Ne(Xe),
        Ne(Ke),
        we(Ke, e)) : Ne(Xe),
        we(Xe, n)
    }
    var Ot = null
      , Ps = !1
      , pi = !1;
    function ou(e) {
        Ot === null ? Ot = [e] : Ot.push(e)
    }
    function Qp(e) {
        Ps = !0,
        ou(e)
    }
    function Qt() {
        if (!pi && Ot !== null) {
            pi = !0;
            var e = 0
              , t = xe;
            try {
                var n = Ot;
                for (xe = 1; e < n.length; e++) {
                    var r = n[e];
                    do
                        r = r(!0);
                    while (r !== null)
                }
                Ot = null,
                Ps = !1
            } catch (o) {
                throw Ot !== null && (Ot = Ot.slice(e + 1)),
                uo(Ml, Qt),
                o
            } finally {
                xe = t,
                pi = !1
            }
        }
        return null
    }
    var Un = []
      , Bn = 0
      , Ls = null
      , _s = 0
      , ut = []
      , ct = 0
      , hn = null
      , Tt = 1
      , zt = "";
    function mn(e, t) {
        Un[Bn++] = _s,
        Un[Bn++] = Ls,
        Ls = e,
        _s = t
    }
    function uu(e, t, n) {
        ut[ct++] = Tt,
        ut[ct++] = zt,
        ut[ct++] = hn,
        hn = e;
        var r = Tt;
        e = zt;
        var o = 32 - gt(r) - 1;
        r &= ~(1 << o),
        n += 1;
        var c = 32 - gt(t) + o;
        if (30 < c) {
            var p = o - o % 5;
            c = (r & (1 << p) - 1).toString(32),
            r >>= p,
            o -= p,
            Tt = 1 << 32 - gt(t) + o | n << o | r,
            zt = c + e
        } else
            Tt = 1 << c | n << o | r,
            zt = e
    }
    function hi(e) {
        e.return !== null && (mn(e, 1),
        uu(e, 1, 0))
    }
    function mi(e) {
        for (; e === Ls; )
            Ls = Un[--Bn],
            Un[Bn] = null,
            _s = Un[--Bn],
            Un[Bn] = null;
        for (; e === hn; )
            hn = ut[--ct],
            ut[ct] = null,
            zt = ut[--ct],
            ut[ct] = null,
            Tt = ut[--ct],
            ut[ct] = null
    }
    var it = null
      , at = null
      , Se = !1
      , yt = null;
    function cu(e, t) {
        var n = ht(5, null, null, 0);
        n.elementType = "DELETED",
        n.stateNode = t,
        n.return = e,
        t = e.deletions,
        t === null ? (e.deletions = [n],
        e.flags |= 16) : t.push(n)
    }
    function du(e, t) {
        switch (e.tag) {
        case 5:
            var n = e.type;
            return t = t.nodeType !== 1 || n.toLowerCase() !== t.nodeName.toLowerCase() ? null : t,
            t !== null ? (e.stateNode = t,
            it = e,
            at = Wt(t.firstChild),
            !0) : !1;
        case 6:
            return t = e.pendingProps === "" || t.nodeType !== 3 ? null : t,
            t !== null ? (e.stateNode = t,
            it = e,
            at = null,
            !0) : !1;
        case 13:
            return t = t.nodeType !== 8 ? null : t,
            t !== null ? (n = hn !== null ? {
                id: Tt,
                overflow: zt
            } : null,
            e.memoizedState = {
                dehydrated: t,
                treeContext: n,
                retryLane: 1073741824
            },
            n = ht(18, null, null, 0),
            n.stateNode = t,
            n.return = e,
            e.child = n,
            it = e,
            at = null,
            !0) : !1;
        default:
            return !1
        }
    }
    function gi(e) {
        return (e.mode & 1) !== 0 && (e.flags & 128) === 0
    }
    function xi(e) {
        if (Se) {
            var t = at;
            if (t) {
                var n = t;
                if (!du(e, t)) {
                    if (gi(e))
                        throw Error(l(418));
                    t = Wt(n.nextSibling);
                    var r = it;
                    t && du(e, t) ? cu(r, n) : (e.flags = e.flags & -4097 | 2,
                    Se = !1,
                    it = e)
                }
            } else {
                if (gi(e))
                    throw Error(l(418));
                e.flags = e.flags & -4097 | 2,
                Se = !1,
                it = e
            }
        }
    }
    function fu(e) {
        for (e = e.return; e !== null && e.tag !== 5 && e.tag !== 3 && e.tag !== 13; )
            e = e.return;
        it = e
    }
    function Rs(e) {
        if (e !== it)
            return !1;
        if (!Se)
            return fu(e),
            Se = !0,
            !1;
        var t;
        if ((t = e.tag !== 3) && !(t = e.tag !== 5) && (t = e.type,
        t = t !== "head" && t !== "body" && !oi(e.type, e.memoizedProps)),
        t && (t = at)) {
            if (gi(e))
                throw pu(),
                Error(l(418));
            for (; t; )
                cu(e, t),
                t = Wt(t.nextSibling)
        }
        if (fu(e),
        e.tag === 13) {
            if (e = e.memoizedState,
            e = e !== null ? e.dehydrated : null,
            !e)
                throw Error(l(317));
            e: {
                for (e = e.nextSibling,
                t = 0; e; ) {
                    if (e.nodeType === 8) {
                        var n = e.data;
                        if (n === "/$") {
                            if (t === 0) {
                                at = Wt(e.nextSibling);
                                break e
                            }
                            t--
                        } else
                            n !== "$" && n !== "$!" && n !== "$?" || t++
                    }
                    e = e.nextSibling
                }
                at = null
            }
        } else
            at = it ? Wt(e.stateNode.nextSibling) : null;
        return !0
    }
    function pu() {
        for (var e = at; e; )
            e = Wt(e.nextSibling)
    }
    function Vn() {
        at = it = null,
        Se = !1
    }
    function yi(e) {
        yt === null ? yt = [e] : yt.push(e)
    }
    var Gp = H.ReactCurrentBatchConfig;
    function Lr(e, t, n) {
        if (e = n.ref,
        e !== null && typeof e != "function" && typeof e != "object") {
            if (n._owner) {
                if (n = n._owner,
                n) {
                    if (n.tag !== 1)
                        throw Error(l(309));
                    var r = n.stateNode
                }
                if (!r)
                    throw Error(l(147, e));
                var o = r
                  , c = "" + e;
                return t !== null && t.ref !== null && typeof t.ref == "function" && t.ref._stringRef === c ? t.ref : (t = function(p) {
                    var y = o.refs;
                    p === null ? delete y[c] : y[c] = p
                }
                ,
                t._stringRef = c,
                t)
            }
            if (typeof e != "string")
                throw Error(l(284));
            if (!n._owner)
                throw Error(l(290, e))
        }
        return e
    }
    function Os(e, t) {
        throw e = Object.prototype.toString.call(t),
        Error(l(31, e === "[object Object]" ? "object with keys {" + Object.keys(t).join(", ") + "}" : e))
    }
    function hu(e) {
        var t = e._init;
        return t(e._payload)
    }
    function mu(e) {
        function t(S, j) {
            if (e) {
                var C = S.deletions;
                C === null ? (S.deletions = [j],
                S.flags |= 16) : C.push(j)
            }
        }
        function n(S, j) {
            if (!e)
                return null;
            for (; j !== null; )
                t(S, j),
                j = j.sibling;
            return null
        }
        function r(S, j) {
            for (S = new Map; j !== null; )
                j.key !== null ? S.set(j.key, j) : S.set(j.index, j),
                j = j.sibling;
            return S
        }
        function o(S, j) {
            return S = rn(S, j),
            S.index = 0,
            S.sibling = null,
            S
        }
        function c(S, j, C) {
            return S.index = C,
            e ? (C = S.alternate,
            C !== null ? (C = C.index,
            C < j ? (S.flags |= 2,
            j) : C) : (S.flags |= 2,
            j)) : (S.flags |= 1048576,
            j)
        }
        function p(S) {
            return e && S.alternate === null && (S.flags |= 2),
            S
        }
        function y(S, j, C, D) {
            return j === null || j.tag !== 6 ? (j = ua(C, S.mode, D),
            j.return = S,
            j) : (j = o(j, C),
            j.return = S,
            j)
        }
        function N(S, j, C, D) {
            var G = C.type;
            return G === te ? M(S, j, C.props.children, D, C.key) : j !== null && (j.elementType === G || typeof G == "object" && G !== null && G.$$typeof === Oe && hu(G) === j.type) ? (D = o(j, C.props),
            D.ref = Lr(S, j, C),
            D.return = S,
            D) : (D = nl(C.type, C.key, C.props, null, S.mode, D),
            D.ref = Lr(S, j, C),
            D.return = S,
            D)
        }
        function L(S, j, C, D) {
            return j === null || j.tag !== 4 || j.stateNode.containerInfo !== C.containerInfo || j.stateNode.implementation !== C.implementation ? (j = ca(C, S.mode, D),
            j.return = S,
            j) : (j = o(j, C.children || []),
            j.return = S,
            j)
        }
        function M(S, j, C, D, G) {
            return j === null || j.tag !== 7 ? (j = jn(C, S.mode, D, G),
            j.return = S,
            j) : (j = o(j, C),
            j.return = S,
            j)
        }
        function A(S, j, C) {
            if (typeof j == "string" && j !== "" || typeof j == "number")
                return j = ua("" + j, S.mode, C),
                j.return = S,
                j;
            if (typeof j == "object" && j !== null) {
                switch (j.$$typeof) {
                case se:
                    return C = nl(j.type, j.key, j.props, null, S.mode, C),
                    C.ref = Lr(S, null, j),
                    C.return = S,
                    C;
                case K:
                    return j = ca(j, S.mode, C),
                    j.return = S,
                    j;
                case Oe:
                    var D = j._init;
                    return A(S, D(j._payload), C)
                }
                if (sr(j) || Y(j))
                    return j = jn(j, S.mode, C, null),
                    j.return = S,
                    j;
                Os(S, j)
            }
            return null
        }
        function z(S, j, C, D) {
            var G = j !== null ? j.key : null;
            if (typeof C == "string" && C !== "" || typeof C == "number")
                return G !== null ? null : y(S, j, "" + C, D);
            if (typeof C == "object" && C !== null) {
                switch (C.$$typeof) {
                case se:
                    return C.key === G ? N(S, j, C, D) : null;
                case K:
                    return C.key === G ? L(S, j, C, D) : null;
                case Oe:
                    return G = C._init,
                    z(S, j, G(C._payload), D)
                }
                if (sr(C) || Y(C))
                    return G !== null ? null : M(S, j, C, D, null);
                Os(S, C)
            }
            return null
        }
        function B(S, j, C, D, G) {
            if (typeof D == "string" && D !== "" || typeof D == "number")
                return S = S.get(C) || null,
                y(j, S, "" + D, G);
            if (typeof D == "object" && D !== null) {
                switch (D.$$typeof) {
                case se:
                    return S = S.get(D.key === null ? C : D.key) || null,
                    N(j, S, D, G);
                case K:
                    return S = S.get(D.key === null ? C : D.key) || null,
                    L(j, S, D, G);
                case Oe:
                    var X = D._init;
                    return B(S, j, C, X(D._payload), G)
                }
                if (sr(D) || Y(D))
                    return S = S.get(C) || null,
                    M(j, S, D, G, null);
                Os(j, D)
            }
            return null
        }
        function q(S, j, C, D) {
            for (var G = null, X = null, Z = j, ne = j = 0, Fe = null; Z !== null && ne < C.length; ne++) {
                Z.index > ne ? (Fe = Z,
                Z = null) : Fe = Z.sibling;
                var he = z(S, Z, C[ne], D);
                if (he === null) {
                    Z === null && (Z = Fe);
                    break
                }
                e && Z && he.alternate === null && t(S, Z),
                j = c(he, j, ne),
                X === null ? G = he : X.sibling = he,
                X = he,
                Z = Fe
            }
            if (ne === C.length)
                return n(S, Z),
                Se && mn(S, ne),
                G;
            if (Z === null) {
                for (; ne < C.length; ne++)
                    Z = A(S, C[ne], D),
                    Z !== null && (j = c(Z, j, ne),
                    X === null ? G = Z : X.sibling = Z,
                    X = Z);
                return Se && mn(S, ne),
                G
            }
            for (Z = r(S, Z); ne < C.length; ne++)
                Fe = B(Z, S, ne, C[ne], D),
                Fe !== null && (e && Fe.alternate !== null && Z.delete(Fe.key === null ? ne : Fe.key),
                j = c(Fe, j, ne),
                X === null ? G = Fe : X.sibling = Fe,
                X = Fe);
            return e && Z.forEach(function(sn) {
                return t(S, sn)
            }),
            Se && mn(S, ne),
            G
        }
        function Q(S, j, C, D) {
            var G = Y(C);
            if (typeof G != "function")
                throw Error(l(150));
            if (C = G.call(C),
            C == null)
                throw Error(l(151));
            for (var X = G = null, Z = j, ne = j = 0, Fe = null, he = C.next(); Z !== null && !he.done; ne++,
            he = C.next()) {
                Z.index > ne ? (Fe = Z,
                Z = null) : Fe = Z.sibling;
                var sn = z(S, Z, he.value, D);
                if (sn === null) {
                    Z === null && (Z = Fe);
                    break
                }
                e && Z && sn.alternate === null && t(S, Z),
                j = c(sn, j, ne),
                X === null ? G = sn : X.sibling = sn,
                X = sn,
                Z = Fe
            }
            if (he.done)
                return n(S, Z),
                Se && mn(S, ne),
                G;
            if (Z === null) {
                for (; !he.done; ne++,
                he = C.next())
                    he = A(S, he.value, D),
                    he !== null && (j = c(he, j, ne),
                    X === null ? G = he : X.sibling = he,
                    X = he);
                return Se && mn(S, ne),
                G
            }
            for (Z = r(S, Z); !he.done; ne++,
            he = C.next())
                he = B(Z, S, ne, he.value, D),
                he !== null && (e && he.alternate !== null && Z.delete(he.key === null ? ne : he.key),
                j = c(he, j, ne),
                X === null ? G = he : X.sibling = he,
                X = he);
            return e && Z.forEach(function(Lh) {
                return t(S, Lh)
            }),
            Se && mn(S, ne),
            G
        }
        function Re(S, j, C, D) {
            if (typeof C == "object" && C !== null && C.type === te && C.key === null && (C = C.props.children),
            typeof C == "object" && C !== null) {
                switch (C.$$typeof) {
                case se:
                    e: {
                        for (var G = C.key, X = j; X !== null; ) {
                            if (X.key === G) {
                                if (G = C.type,
                                G === te) {
                                    if (X.tag === 7) {
                                        n(S, X.sibling),
                                        j = o(X, C.props.children),
                                        j.return = S,
                                        S = j;
                                        break e
                                    }
                                } else if (X.elementType === G || typeof G == "object" && G !== null && G.$$typeof === Oe && hu(G) === X.type) {
                                    n(S, X.sibling),
                                    j = o(X, C.props),
                                    j.ref = Lr(S, X, C),
                                    j.return = S,
                                    S = j;
                                    break e
                                }
                                n(S, X);
                                break
                            } else
                                t(S, X);
                            X = X.sibling
                        }
                        C.type === te ? (j = jn(C.props.children, S.mode, D, C.key),
                        j.return = S,
                        S = j) : (D = nl(C.type, C.key, C.props, null, S.mode, D),
                        D.ref = Lr(S, j, C),
                        D.return = S,
                        S = D)
                    }
                    return p(S);
                case K:
                    e: {
                        for (X = C.key; j !== null; ) {
                            if (j.key === X)
                                if (j.tag === 4 && j.stateNode.containerInfo === C.containerInfo && j.stateNode.implementation === C.implementation) {
                                    n(S, j.sibling),
                                    j = o(j, C.children || []),
                                    j.return = S,
                                    S = j;
                                    break e
                                } else {
                                    n(S, j);
                                    break
                                }
                            else
                                t(S, j);
                            j = j.sibling
                        }
                        j = ca(C, S.mode, D),
                        j.return = S,
                        S = j
                    }
                    return p(S);
                case Oe:
                    return X = C._init,
                    Re(S, j, X(C._payload), D)
                }
                if (sr(C))
                    return q(S, j, C, D);
                if (Y(C))
                    return Q(S, j, C, D);
                Os(S, C)
            }
            return typeof C == "string" && C !== "" || typeof C == "number" ? (C = "" + C,
            j !== null && j.tag === 6 ? (n(S, j.sibling),
            j = o(j, C),
            j.return = S,
            S = j) : (n(S, j),
            j = ua(C, S.mode, D),
            j.return = S,
            S = j),
            p(S)) : n(S, j)
        }
        return Re
    }
    var Hn = mu(!0)
      , gu = mu(!1)
      , Ts = qt(null)
      , zs = null
      , Kn = null
      , vi = null;
    function wi() {
        vi = Kn = zs = null
    }
    function bi(e) {
        var t = Ts.current;
        Ne(Ts),
        e._currentValue = t
    }
    function Ni(e, t, n) {
        for (; e !== null; ) {
            var r = e.alternate;
            if ((e.childLanes & t) !== t ? (e.childLanes |= t,
            r !== null && (r.childLanes |= t)) : r !== null && (r.childLanes & t) !== t && (r.childLanes |= t),
            e === n)
                break;
            e = e.return
        }
    }
    function Wn(e, t) {
        zs = e,
        vi = Kn = null,
        e = e.dependencies,
        e !== null && e.firstContext !== null && ((e.lanes & t) !== 0 && (et = !0),
        e.firstContext = null)
    }
    function dt(e) {
        var t = e._currentValue;
        if (vi !== e)
            if (e = {
                context: e,
                memoizedValue: t,
                next: null
            },
            Kn === null) {
                if (zs === null)
                    throw Error(l(308));
                Kn = e,
                zs.dependencies = {
                    lanes: 0,
                    firstContext: e
                }
            } else
                Kn = Kn.next = e;
        return t
    }
    var gn = null;
    function ji(e) {
        gn === null ? gn = [e] : gn.push(e)
    }
    function xu(e, t, n, r) {
        var o = t.interleaved;
        return o === null ? (n.next = n,
        ji(t)) : (n.next = o.next,
        o.next = n),
        t.interleaved = n,
        Mt(e, r)
    }
    function Mt(e, t) {
        e.lanes |= t;
        var n = e.alternate;
        for (n !== null && (n.lanes |= t),
        n = e,
        e = e.return; e !== null; )
            e.childLanes |= t,
            n = e.alternate,
            n !== null && (n.childLanes |= t),
            n = e,
            e = e.return;
        return n.tag === 3 ? n.stateNode : null
    }
    var Gt = !1;
    function ki(e) {
        e.updateQueue = {
            baseState: e.memoizedState,
            firstBaseUpdate: null,
            lastBaseUpdate: null,
            shared: {
                pending: null,
                interleaved: null,
                lanes: 0
            },
            effects: null
        }
    }
    function yu(e, t) {
        e = e.updateQueue,
        t.updateQueue === e && (t.updateQueue = {
            baseState: e.baseState,
            firstBaseUpdate: e.firstBaseUpdate,
            lastBaseUpdate: e.lastBaseUpdate,
            shared: e.shared,
            effects: e.effects
        })
    }
    function At(e, t) {
        return {
            eventTime: e,
            lane: t,
            tag: 0,
            payload: null,
            callback: null,
            next: null
        }
    }
    function Jt(e, t, n) {
        var r = e.updateQueue;
        if (r === null)
            return null;
        if (r = r.shared,
        (de & 2) !== 0) {
            var o = r.pending;
            return o === null ? t.next = t : (t.next = o.next,
            o.next = t),
            r.pending = t,
            Mt(e, n)
        }
        return o = r.interleaved,
        o === null ? (t.next = t,
        ji(r)) : (t.next = o.next,
        o.next = t),
        r.interleaved = t,
        Mt(e, n)
    }
    function Ms(e, t, n) {
        if (t = t.updateQueue,
        t !== null && (t = t.shared,
        (n & 4194240) !== 0)) {
            var r = t.lanes;
            r &= e.pendingLanes,
            n |= r,
            t.lanes = n,
            $l(e, n)
        }
    }
    function vu(e, t) {
        var n = e.updateQueue
          , r = e.alternate;
        if (r !== null && (r = r.updateQueue,
        n === r)) {
            var o = null
              , c = null;
            if (n = n.firstBaseUpdate,
            n !== null) {
                do {
                    var p = {
                        eventTime: n.eventTime,
                        lane: n.lane,
                        tag: n.tag,
                        payload: n.payload,
                        callback: n.callback,
                        next: null
                    };
                    c === null ? o = c = p : c = c.next = p,
                    n = n.next
                } while (n !== null);
                c === null ? o = c = t : c = c.next = t
            } else
                o = c = t;
            n = {
                baseState: r.baseState,
                firstBaseUpdate: o,
                lastBaseUpdate: c,
                shared: r.shared,
                effects: r.effects
            },
            e.updateQueue = n;
            return
        }
        e = n.lastBaseUpdate,
        e === null ? n.firstBaseUpdate = t : e.next = t,
        n.lastBaseUpdate = t
    }
    function As(e, t, n, r) {
        var o = e.updateQueue;
        Gt = !1;
        var c = o.firstBaseUpdate
          , p = o.lastBaseUpdate
          , y = o.shared.pending;
        if (y !== null) {
            o.shared.pending = null;
            var N = y
              , L = N.next;
            N.next = null,
            p === null ? c = L : p.next = L,
            p = N;
            var M = e.alternate;
            M !== null && (M = M.updateQueue,
            y = M.lastBaseUpdate,
            y !== p && (y === null ? M.firstBaseUpdate = L : y.next = L,
            M.lastBaseUpdate = N))
        }
        if (c !== null) {
            var A = o.baseState;
            p = 0,
            M = L = N = null,
            y = c;
            do {
                var z = y.lane
                  , B = y.eventTime;
                if ((r & z) === z) {
                    M !== null && (M = M.next = {
                        eventTime: B,
                        lane: 0,
                        tag: y.tag,
                        payload: y.payload,
                        callback: y.callback,
                        next: null
                    });
                    e: {
                        var q = e
                          , Q = y;
                        switch (z = t,
                        B = n,
                        Q.tag) {
                        case 1:
                            if (q = Q.payload,
                            typeof q == "function") {
                                A = q.call(B, A, z);
                                break e
                            }
                            A = q;
                            break e;
                        case 3:
                            q.flags = q.flags & -65537 | 128;
                        case 0:
                            if (q = Q.payload,
                            z = typeof q == "function" ? q.call(B, A, z) : q,
                            z == null)
                                break e;
                            A = U({}, A, z);
                            break e;
                        case 2:
                            Gt = !0
                        }
                    }
                    y.callback !== null && y.lane !== 0 && (e.flags |= 64,
                    z = o.effects,
                    z === null ? o.effects = [y] : z.push(y))
                } else
                    B = {
                        eventTime: B,
                        lane: z,
                        tag: y.tag,
                        payload: y.payload,
                        callback: y.callback,
                        next: null
                    },
                    M === null ? (L = M = B,
                    N = A) : M = M.next = B,
                    p |= z;
                if (y = y.next,
                y === null) {
                    if (y = o.shared.pending,
                    y === null)
                        break;
                    z = y,
                    y = z.next,
                    z.next = null,
                    o.lastBaseUpdate = z,
                    o.shared.pending = null
                }
            } while (!0);
            if (M === null && (N = A),
            o.baseState = N,
            o.firstBaseUpdate = L,
            o.lastBaseUpdate = M,
            t = o.shared.interleaved,
            t !== null) {
                o = t;
                do
                    p |= o.lane,
                    o = o.next;
                while (o !== t)
            } else
                c === null && (o.shared.lanes = 0);
            vn |= p,
            e.lanes = p,
            e.memoizedState = A
        }
    }
    function wu(e, t, n) {
        if (e = t.effects,
        t.effects = null,
        e !== null)
            for (t = 0; t < e.length; t++) {
                var r = e[t]
                  , o = r.callback;
                if (o !== null) {
                    if (r.callback = null,
                    r = n,
                    typeof o != "function")
                        throw Error(l(191, o));
                    o.call(r)
                }
            }
    }
    var _r = {}
      , St = qt(_r)
      , Rr = qt(_r)
      , Or = qt(_r);
    function xn(e) {
        if (e === _r)
            throw Error(l(174));
        return e
    }
    function Si(e, t) {
        switch (we(Or, t),
        we(Rr, e),
        we(St, _r),
        e = t.nodeType,
        e) {
        case 9:
        case 11:
            t = (t = t.documentElement) ? t.namespaceURI : Cl(null, "");
            break;
        default:
            e = e === 8 ? t.parentNode : t,
            t = e.namespaceURI || null,
            e = e.tagName,
            t = Cl(t, e)
        }
        Ne(St),
        we(St, t)
    }
    function qn() {
        Ne(St),
        Ne(Rr),
        Ne(Or)
    }
    function bu(e) {
        xn(Or.current);
        var t = xn(St.current)
          , n = Cl(t, e.type);
        t !== n && (we(Rr, e),
        we(St, n))
    }
    function Ci(e) {
        Rr.current === e && (Ne(St),
        Ne(Rr))
    }
    var Ce = qt(0);
    function Ds(e) {
        for (var t = e; t !== null; ) {
            if (t.tag === 13) {
                var n = t.memoizedState;
                if (n !== null && (n = n.dehydrated,
                n === null || n.data === "$?" || n.data === "$!"))
                    return t
            } else if (t.tag === 19 && t.memoizedProps.revealOrder !== void 0) {
                if ((t.flags & 128) !== 0)
                    return t
            } else if (t.child !== null) {
                t.child.return = t,
                t = t.child;
                continue
            }
            if (t === e)
                break;
            for (; t.sibling === null; ) {
                if (t.return === null || t.return === e)
                    return null;
                t = t.return
            }
            t.sibling.return = t.return,
            t = t.sibling
        }
        return null
    }
    var Ei = [];
    function Pi() {
        for (var e = 0; e < Ei.length; e++)
            Ei[e]._workInProgressVersionPrimary = null;
        Ei.length = 0
    }
    var $s = H.ReactCurrentDispatcher
      , Li = H.ReactCurrentBatchConfig
      , yn = 0
      , Ee = null
      , Me = null
      , $e = null
      , Is = !1
      , Tr = !1
      , zr = 0
      , Jp = 0;
    function We() {
        throw Error(l(321))
    }
    function _i(e, t) {
        if (t === null)
            return !1;
        for (var n = 0; n < t.length && n < e.length; n++)
            if (!xt(e[n], t[n]))
                return !1;
        return !0
    }
    function Ri(e, t, n, r, o, c) {
        if (yn = c,
        Ee = t,
        t.memoizedState = null,
        t.updateQueue = null,
        t.lanes = 0,
        $s.current = e === null || e.memoizedState === null ? th : nh,
        e = n(r, o),
        Tr) {
            c = 0;
            do {
                if (Tr = !1,
                zr = 0,
                25 <= c)
                    throw Error(l(301));
                c += 1,
                $e = Me = null,
                t.updateQueue = null,
                $s.current = rh,
                e = n(r, o)
            } while (Tr)
        }
        if ($s.current = Bs,
        t = Me !== null && Me.next !== null,
        yn = 0,
        $e = Me = Ee = null,
        Is = !1,
        t)
            throw Error(l(300));
        return e
    }
    function Oi() {
        var e = zr !== 0;
        return zr = 0,
        e
    }
    function Ct() {
        var e = {
            memoizedState: null,
            baseState: null,
            baseQueue: null,
            queue: null,
            next: null
        };
        return $e === null ? Ee.memoizedState = $e = e : $e = $e.next = e,
        $e
    }
    function ft() {
        if (Me === null) {
            var e = Ee.alternate;
            e = e !== null ? e.memoizedState : null
        } else
            e = Me.next;
        var t = $e === null ? Ee.memoizedState : $e.next;
        if (t !== null)
            $e = t,
            Me = e;
        else {
            if (e === null)
                throw Error(l(310));
            Me = e,
            e = {
                memoizedState: Me.memoizedState,
                baseState: Me.baseState,
                baseQueue: Me.baseQueue,
                queue: Me.queue,
                next: null
            },
            $e === null ? Ee.memoizedState = $e = e : $e = $e.next = e
        }
        return $e
    }
    function Mr(e, t) {
        return typeof t == "function" ? t(e) : t
    }
    function Ti(e) {
        var t = ft()
          , n = t.queue;
        if (n === null)
            throw Error(l(311));
        n.lastRenderedReducer = e;
        var r = Me
          , o = r.baseQueue
          , c = n.pending;
        if (c !== null) {
            if (o !== null) {
                var p = o.next;
                o.next = c.next,
                c.next = p
            }
            r.baseQueue = o = c,
            n.pending = null
        }
        if (o !== null) {
            c = o.next,
            r = r.baseState;
            var y = p = null
              , N = null
              , L = c;
            do {
                var M = L.lane;
                if ((yn & M) === M)
                    N !== null && (N = N.next = {
                        lane: 0,
                        action: L.action,
                        hasEagerState: L.hasEagerState,
                        eagerState: L.eagerState,
                        next: null
                    }),
                    r = L.hasEagerState ? L.eagerState : e(r, L.action);
                else {
                    var A = {
                        lane: M,
                        action: L.action,
                        hasEagerState: L.hasEagerState,
                        eagerState: L.eagerState,
                        next: null
                    };
                    N === null ? (y = N = A,
                    p = r) : N = N.next = A,
                    Ee.lanes |= M,
                    vn |= M
                }
                L = L.next
            } while (L !== null && L !== c);
            N === null ? p = r : N.next = y,
            xt(r, t.memoizedState) || (et = !0),
            t.memoizedState = r,
            t.baseState = p,
            t.baseQueue = N,
            n.lastRenderedState = r
        }
        if (e = n.interleaved,
        e !== null) {
            o = e;
            do
                c = o.lane,
                Ee.lanes |= c,
                vn |= c,
                o = o.next;
            while (o !== e)
        } else
            o === null && (n.lanes = 0);
        return [t.memoizedState, n.dispatch]
    }
    function zi(e) {
        var t = ft()
          , n = t.queue;
        if (n === null)
            throw Error(l(311));
        n.lastRenderedReducer = e;
        var r = n.dispatch
          , o = n.pending
          , c = t.memoizedState;
        if (o !== null) {
            n.pending = null;
            var p = o = o.next;
            do
                c = e(c, p.action),
                p = p.next;
            while (p !== o);
            xt(c, t.memoizedState) || (et = !0),
            t.memoizedState = c,
            t.baseQueue === null && (t.baseState = c),
            n.lastRenderedState = c
        }
        return [c, r]
    }
    function Nu() {}
    function ju(e, t) {
        var n = Ee
          , r = ft()
          , o = t()
          , c = !xt(r.memoizedState, o);
        if (c && (r.memoizedState = o,
        et = !0),
        r = r.queue,
        Mi(Cu.bind(null, n, r, e), [e]),
        r.getSnapshot !== t || c || $e !== null && $e.memoizedState.tag & 1) {
            if (n.flags |= 2048,
            Ar(9, Su.bind(null, n, r, o, t), void 0, null),
            Ie === null)
                throw Error(l(349));
            (yn & 30) !== 0 || ku(n, t, o)
        }
        return o
    }
    function ku(e, t, n) {
        e.flags |= 16384,
        e = {
            getSnapshot: t,
            value: n
        },
        t = Ee.updateQueue,
        t === null ? (t = {
            lastEffect: null,
            stores: null
        },
        Ee.updateQueue = t,
        t.stores = [e]) : (n = t.stores,
        n === null ? t.stores = [e] : n.push(e))
    }
    function Su(e, t, n, r) {
        t.value = n,
        t.getSnapshot = r,
        Eu(t) && Pu(e)
    }
    function Cu(e, t, n) {
        return n(function() {
            Eu(t) && Pu(e)
        })
    }
    function Eu(e) {
        var t = e.getSnapshot;
        e = e.value;
        try {
            var n = t();
            return !xt(e, n)
        } catch {
            return !0
        }
    }
    function Pu(e) {
        var t = Mt(e, 1);
        t !== null && Nt(t, e, 1, -1)
    }
    function Lu(e) {
        var t = Ct();
        return typeof e == "function" && (e = e()),
        t.memoizedState = t.baseState = e,
        e = {
            pending: null,
            interleaved: null,
            lanes: 0,
            dispatch: null,
            lastRenderedReducer: Mr,
            lastRenderedState: e
        },
        t.queue = e,
        e = e.dispatch = eh.bind(null, Ee, e),
        [t.memoizedState, e]
    }
    function Ar(e, t, n, r) {
        return e = {
            tag: e,
            create: t,
            destroy: n,
            deps: r,
            next: null
        },
        t = Ee.updateQueue,
        t === null ? (t = {
            lastEffect: null,
            stores: null
        },
        Ee.updateQueue = t,
        t.lastEffect = e.next = e) : (n = t.lastEffect,
        n === null ? t.lastEffect = e.next = e : (r = n.next,
        n.next = e,
        e.next = r,
        t.lastEffect = e)),
        e
    }
    function _u() {
        return ft().memoizedState
    }
    function Fs(e, t, n, r) {
        var o = Ct();
        Ee.flags |= e,
        o.memoizedState = Ar(1 | t, n, void 0, r === void 0 ? null : r)
    }
    function Us(e, t, n, r) {
        var o = ft();
        r = r === void 0 ? null : r;
        var c = void 0;
        if (Me !== null) {
            var p = Me.memoizedState;
            if (c = p.destroy,
            r !== null && _i(r, p.deps)) {
                o.memoizedState = Ar(t, n, c, r);
                return
            }
        }
        Ee.flags |= e,
        o.memoizedState = Ar(1 | t, n, c, r)
    }
    function Ru(e, t) {
        return Fs(8390656, 8, e, t)
    }
    function Mi(e, t) {
        return Us(2048, 8, e, t)
    }
    function Ou(e, t) {
        return Us(4, 2, e, t)
    }
    function Tu(e, t) {
        return Us(4, 4, e, t)
    }
    function zu(e, t) {
        if (typeof t == "function")
            return e = e(),
            t(e),
            function() {
                t(null)
            }
            ;
        if (t != null)
            return e = e(),
            t.current = e,
            function() {
                t.current = null
            }
    }
    function Mu(e, t, n) {
        return n = n != null ? n.concat([e]) : null,
        Us(4, 4, zu.bind(null, t, e), n)
    }
    function Ai() {}
    function Au(e, t) {
        var n = ft();
        t = t === void 0 ? null : t;
        var r = n.memoizedState;
        return r !== null && t !== null && _i(t, r[1]) ? r[0] : (n.memoizedState = [e, t],
        e)
    }
    function Du(e, t) {
        var n = ft();
        t = t === void 0 ? null : t;
        var r = n.memoizedState;
        return r !== null && t !== null && _i(t, r[1]) ? r[0] : (e = e(),
        n.memoizedState = [e, t],
        e)
    }
    function $u(e, t, n) {
        return (yn & 21) === 0 ? (e.baseState && (e.baseState = !1,
        et = !0),
        e.memoizedState = n) : (xt(n, t) || (n = ho(),
        Ee.lanes |= n,
        vn |= n,
        e.baseState = !0),
        t)
    }
    function Xp(e, t) {
        var n = xe;
        xe = n !== 0 && 4 > n ? n : 4,
        e(!0);
        var r = Li.transition;
        Li.transition = {};
        try {
            e(!1),
            t()
        } finally {
            xe = n,
            Li.transition = r
        }
    }
    function Iu() {
        return ft().memoizedState
    }
    function Zp(e, t, n) {
        var r = tn(e);
        if (n = {
            lane: r,
            action: n,
            hasEagerState: !1,
            eagerState: null,
            next: null
        },
        Fu(e))
            Uu(t, n);
        else if (n = xu(e, t, n, r),
        n !== null) {
            var o = Ge();
            Nt(n, e, r, o),
            Bu(n, t, r)
        }
    }
    function eh(e, t, n) {
        var r = tn(e)
          , o = {
            lane: r,
            action: n,
            hasEagerState: !1,
            eagerState: null,
            next: null
        };
        if (Fu(e))
            Uu(t, o);
        else {
            var c = e.alternate;
            if (e.lanes === 0 && (c === null || c.lanes === 0) && (c = t.lastRenderedReducer,
            c !== null))
                try {
                    var p = t.lastRenderedState
                      , y = c(p, n);
                    if (o.hasEagerState = !0,
                    o.eagerState = y,
                    xt(y, p)) {
                        var N = t.interleaved;
                        N === null ? (o.next = o,
                        ji(t)) : (o.next = N.next,
                        N.next = o),
                        t.interleaved = o;
                        return
                    }
                } catch {} finally {}
            n = xu(e, t, o, r),
            n !== null && (o = Ge(),
            Nt(n, e, r, o),
            Bu(n, t, r))
        }
    }
    function Fu(e) {
        var t = e.alternate;
        return e === Ee || t !== null && t === Ee
    }
    function Uu(e, t) {
        Tr = Is = !0;
        var n = e.pending;
        n === null ? t.next = t : (t.next = n.next,
        n.next = t),
        e.pending = t
    }
    function Bu(e, t, n) {
        if ((n & 4194240) !== 0) {
            var r = t.lanes;
            r &= e.pendingLanes,
            n |= r,
            t.lanes = n,
            $l(e, n)
        }
    }
    var Bs = {
        readContext: dt,
        useCallback: We,
        useContext: We,
        useEffect: We,
        useImperativeHandle: We,
        useInsertionEffect: We,
        useLayoutEffect: We,
        useMemo: We,
        useReducer: We,
        useRef: We,
        useState: We,
        useDebugValue: We,
        useDeferredValue: We,
        useTransition: We,
        useMutableSource: We,
        useSyncExternalStore: We,
        useId: We,
        unstable_isNewReconciler: !1
    }
      , th = {
        readContext: dt,
        useCallback: function(e, t) {
            return Ct().memoizedState = [e, t === void 0 ? null : t],
            e
        },
        useContext: dt,
        useEffect: Ru,
        useImperativeHandle: function(e, t, n) {
            return n = n != null ? n.concat([e]) : null,
            Fs(4194308, 4, zu.bind(null, t, e), n)
        },
        useLayoutEffect: function(e, t) {
            return Fs(4194308, 4, e, t)
        },
        useInsertionEffect: function(e, t) {
            return Fs(4, 2, e, t)
        },
        useMemo: function(e, t) {
            var n = Ct();
            return t = t === void 0 ? null : t,
            e = e(),
            n.memoizedState = [e, t],
            e
        },
        useReducer: function(e, t, n) {
            var r = Ct();
            return t = n !== void 0 ? n(t) : t,
            r.memoizedState = r.baseState = t,
            e = {
                pending: null,
                interleaved: null,
                lanes: 0,
                dispatch: null,
                lastRenderedReducer: e,
                lastRenderedState: t
            },
            r.queue = e,
            e = e.dispatch = Zp.bind(null, Ee, e),
            [r.memoizedState, e]
        },
        useRef: function(e) {
            var t = Ct();
            return e = {
                current: e
            },
            t.memoizedState = e
        },
        useState: Lu,
        useDebugValue: Ai,
        useDeferredValue: function(e) {
            return Ct().memoizedState = e
        },
        useTransition: function() {
            var e = Lu(!1)
              , t = e[0];
            return e = Xp.bind(null, e[1]),
            Ct().memoizedState = e,
            [t, e]
        },
        useMutableSource: function() {},
        useSyncExternalStore: function(e, t, n) {
            var r = Ee
              , o = Ct();
            if (Se) {
                if (n === void 0)
                    throw Error(l(407));
                n = n()
            } else {
                if (n = t(),
                Ie === null)
                    throw Error(l(349));
                (yn & 30) !== 0 || ku(r, t, n)
            }
            o.memoizedState = n;
            var c = {
                value: n,
                getSnapshot: t
            };
            return o.queue = c,
            Ru(Cu.bind(null, r, c, e), [e]),
            r.flags |= 2048,
            Ar(9, Su.bind(null, r, c, n, t), void 0, null),
            n
        },
        useId: function() {
            var e = Ct()
              , t = Ie.identifierPrefix;
            if (Se) {
                var n = zt
                  , r = Tt;
                n = (r & ~(1 << 32 - gt(r) - 1)).toString(32) + n,
                t = ":" + t + "R" + n,
                n = zr++,
                0 < n && (t += "H" + n.toString(32)),
                t += ":"
            } else
                n = Jp++,
                t = ":" + t + "r" + n.toString(32) + ":";
            return e.memoizedState = t
        },
        unstable_isNewReconciler: !1
    }
      , nh = {
        readContext: dt,
        useCallback: Au,
        useContext: dt,
        useEffect: Mi,
        useImperativeHandle: Mu,
        useInsertionEffect: Ou,
        useLayoutEffect: Tu,
        useMemo: Du,
        useReducer: Ti,
        useRef: _u,
        useState: function() {
            return Ti(Mr)
        },
        useDebugValue: Ai,
        useDeferredValue: function(e) {
            var t = ft();
            return $u(t, Me.memoizedState, e)
        },
        useTransition: function() {
            var e = Ti(Mr)[0]
              , t = ft().memoizedState;
            return [e, t]
        },
        useMutableSource: Nu,
        useSyncExternalStore: ju,
        useId: Iu,
        unstable_isNewReconciler: !1
    }
      , rh = {
        readContext: dt,
        useCallback: Au,
        useContext: dt,
        useEffect: Mi,
        useImperativeHandle: Mu,
        useInsertionEffect: Ou,
        useLayoutEffect: Tu,
        useMemo: Du,
        useReducer: zi,
        useRef: _u,
        useState: function() {
            return zi(Mr)
        },
        useDebugValue: Ai,
        useDeferredValue: function(e) {
            var t = ft();
            return Me === null ? t.memoizedState = e : $u(t, Me.memoizedState, e)
        },
        useTransition: function() {
            var e = zi(Mr)[0]
              , t = ft().memoizedState;
            return [e, t]
        },
        useMutableSource: Nu,
        useSyncExternalStore: ju,
        useId: Iu,
        unstable_isNewReconciler: !1
    };
    function vt(e, t) {
        if (e && e.defaultProps) {
            t = U({}, t),
            e = e.defaultProps;
            for (var n in e)
                t[n] === void 0 && (t[n] = e[n]);
            return t
        }
        return t
    }
    function Di(e, t, n, r) {
        t = e.memoizedState,
        n = n(r, t),
        n = n == null ? t : U({}, t, n),
        e.memoizedState = n,
        e.lanes === 0 && (e.updateQueue.baseState = n)
    }
    var Vs = {
        isMounted: function(e) {
            return (e = e._reactInternals) ? dn(e) === e : !1
        },
        enqueueSetState: function(e, t, n) {
            e = e._reactInternals;
            var r = Ge()
              , o = tn(e)
              , c = At(r, o);
            c.payload = t,
            n != null && (c.callback = n),
            t = Jt(e, c, o),
            t !== null && (Nt(t, e, o, r),
            Ms(t, e, o))
        },
        enqueueReplaceState: function(e, t, n) {
            e = e._reactInternals;
            var r = Ge()
              , o = tn(e)
              , c = At(r, o);
            c.tag = 1,
            c.payload = t,
            n != null && (c.callback = n),
            t = Jt(e, c, o),
            t !== null && (Nt(t, e, o, r),
            Ms(t, e, o))
        },
        enqueueForceUpdate: function(e, t) {
            e = e._reactInternals;
            var n = Ge()
              , r = tn(e)
              , o = At(n, r);
            o.tag = 2,
            t != null && (o.callback = t),
            t = Jt(e, o, r),
            t !== null && (Nt(t, e, r, n),
            Ms(t, e, r))
        }
    };
    function Vu(e, t, n, r, o, c, p) {
        return e = e.stateNode,
        typeof e.shouldComponentUpdate == "function" ? e.shouldComponentUpdate(r, c, p) : t.prototype && t.prototype.isPureReactComponent ? !Nr(n, r) || !Nr(o, c) : !0
    }
    function Hu(e, t, n) {
        var r = !1
          , o = Yt
          , c = t.contextType;
        return typeof c == "object" && c !== null ? c = dt(c) : (o = Ze(t) ? pn : Ke.current,
        r = t.contextTypes,
        c = (r = r != null) ? Fn(e, o) : Yt),
        t = new t(n,c),
        e.memoizedState = t.state !== null && t.state !== void 0 ? t.state : null,
        t.updater = Vs,
        e.stateNode = t,
        t._reactInternals = e,
        r && (e = e.stateNode,
        e.__reactInternalMemoizedUnmaskedChildContext = o,
        e.__reactInternalMemoizedMaskedChildContext = c),
        t
    }
    function Ku(e, t, n, r) {
        e = t.state,
        typeof t.componentWillReceiveProps == "function" && t.componentWillReceiveProps(n, r),
        typeof t.UNSAFE_componentWillReceiveProps == "function" && t.UNSAFE_componentWillReceiveProps(n, r),
        t.state !== e && Vs.enqueueReplaceState(t, t.state, null)
    }
    function $i(e, t, n, r) {
        var o = e.stateNode;
        o.props = n,
        o.state = e.memoizedState,
        o.refs = {},
        ki(e);
        var c = t.contextType;
        typeof c == "object" && c !== null ? o.context = dt(c) : (c = Ze(t) ? pn : Ke.current,
        o.context = Fn(e, c)),
        o.state = e.memoizedState,
        c = t.getDerivedStateFromProps,
        typeof c == "function" && (Di(e, t, c, n),
        o.state = e.memoizedState),
        typeof t.getDerivedStateFromProps == "function" || typeof o.getSnapshotBeforeUpdate == "function" || typeof o.UNSAFE_componentWillMount != "function" && typeof o.componentWillMount != "function" || (t = o.state,
        typeof o.componentWillMount == "function" && o.componentWillMount(),
        typeof o.UNSAFE_componentWillMount == "function" && o.UNSAFE_componentWillMount(),
        t !== o.state && Vs.enqueueReplaceState(o, o.state, null),
        As(e, n, o, r),
        o.state = e.memoizedState),
        typeof o.componentDidMount == "function" && (e.flags |= 4194308)
    }
    function Yn(e, t) {
        try {
            var n = ""
              , r = t;
            do
                n += fe(r),
                r = r.return;
            while (r);
            var o = n
        } catch (c) {
            o = `
Error generating stack: ` + c.message + `
` + c.stack
        }
        return {
            value: e,
            source: t,
            stack: o,
            digest: null
        }
    }
    function Ii(e, t, n) {
        return {
            value: e,
            source: null,
            stack: n ?? null,
            digest: t ?? null
        }
    }
    function Fi(e, t) {
        try {
            console.error(t.value)
        } catch (n) {
            setTimeout(function() {
                throw n
            })
        }
    }
    var sh = typeof WeakMap == "function" ? WeakMap : Map;
    function Wu(e, t, n) {
        n = At(-1, n),
        n.tag = 3,
        n.payload = {
            element: null
        };
        var r = t.value;
        return n.callback = function() {
            Gs || (Gs = !0,
            ta = r),
            Fi(e, t)
        }
        ,
        n
    }
    function qu(e, t, n) {
        n = At(-1, n),
        n.tag = 3;
        var r = e.type.getDerivedStateFromError;
        if (typeof r == "function") {
            var o = t.value;
            n.payload = function() {
                return r(o)
            }
            ,
            n.callback = function() {
                Fi(e, t)
            }
        }
        var c = e.stateNode;
        return c !== null && typeof c.componentDidCatch == "function" && (n.callback = function() {
            Fi(e, t),
            typeof r != "function" && (Zt === null ? Zt = new Set([this]) : Zt.add(this));
            var p = t.stack;
            this.componentDidCatch(t.value, {
                componentStack: p !== null ? p : ""
            })
        }
        ),
        n
    }
    function Yu(e, t, n) {
        var r = e.pingCache;
        if (r === null) {
            r = e.pingCache = new sh;
            var o = new Set;
            r.set(t, o)
        } else
            o = r.get(t),
            o === void 0 && (o = new Set,
            r.set(t, o));
        o.has(n) || (o.add(n),
        e = yh.bind(null, e, t, n),
        t.then(e, e))
    }
    function Qu(e) {
        do {
            var t;
            if ((t = e.tag === 13) && (t = e.memoizedState,
            t = t !== null ? t.dehydrated !== null : !0),
            t)
                return e;
            e = e.return
        } while (e !== null);
        return null
    }
    function Gu(e, t, n, r, o) {
        return (e.mode & 1) === 0 ? (e === t ? e.flags |= 65536 : (e.flags |= 128,
        n.flags |= 131072,
        n.flags &= -52805,
        n.tag === 1 && (n.alternate === null ? n.tag = 17 : (t = At(-1, 1),
        t.tag = 2,
        Jt(n, t, 1))),
        n.lanes |= 1),
        e) : (e.flags |= 65536,
        e.lanes = o,
        e)
    }
    var lh = H.ReactCurrentOwner
      , et = !1;
    function Qe(e, t, n, r) {
        t.child = e === null ? gu(t, null, n, r) : Hn(t, e.child, n, r)
    }
    function Ju(e, t, n, r, o) {
        n = n.render;
        var c = t.ref;
        return Wn(t, o),
        r = Ri(e, t, n, r, c, o),
        n = Oi(),
        e !== null && !et ? (t.updateQueue = e.updateQueue,
        t.flags &= -2053,
        e.lanes &= ~o,
        Dt(e, t, o)) : (Se && n && hi(t),
        t.flags |= 1,
        Qe(e, t, r, o),
        t.child)
    }
    function Xu(e, t, n, r, o) {
        if (e === null) {
            var c = n.type;
            return typeof c == "function" && !oa(c) && c.defaultProps === void 0 && n.compare === null && n.defaultProps === void 0 ? (t.tag = 15,
            t.type = c,
            Zu(e, t, c, r, o)) : (e = nl(n.type, null, r, t, t.mode, o),
            e.ref = t.ref,
            e.return = t,
            t.child = e)
        }
        if (c = e.child,
        (e.lanes & o) === 0) {
            var p = c.memoizedProps;
            if (n = n.compare,
            n = n !== null ? n : Nr,
            n(p, r) && e.ref === t.ref)
                return Dt(e, t, o)
        }
        return t.flags |= 1,
        e = rn(c, r),
        e.ref = t.ref,
        e.return = t,
        t.child = e
    }
    function Zu(e, t, n, r, o) {
        if (e !== null) {
            var c = e.memoizedProps;
            if (Nr(c, r) && e.ref === t.ref)
                if (et = !1,
                t.pendingProps = r = c,
                (e.lanes & o) !== 0)
                    (e.flags & 131072) !== 0 && (et = !0);
                else
                    return t.lanes = e.lanes,
                    Dt(e, t, o)
        }
        return Ui(e, t, n, r, o)
    }
    function ec(e, t, n) {
        var r = t.pendingProps
          , o = r.children
          , c = e !== null ? e.memoizedState : null;
        if (r.mode === "hidden")
            if ((t.mode & 1) === 0)
                t.memoizedState = {
                    baseLanes: 0,
                    cachePool: null,
                    transitions: null
                },
                we(Gn, ot),
                ot |= n;
            else {
                if ((n & 1073741824) === 0)
                    return e = c !== null ? c.baseLanes | n : n,
                    t.lanes = t.childLanes = 1073741824,
                    t.memoizedState = {
                        baseLanes: e,
                        cachePool: null,
                        transitions: null
                    },
                    t.updateQueue = null,
                    we(Gn, ot),
                    ot |= e,
                    null;
                t.memoizedState = {
                    baseLanes: 0,
                    cachePool: null,
                    transitions: null
                },
                r = c !== null ? c.baseLanes : n,
                we(Gn, ot),
                ot |= r
            }
        else
            c !== null ? (r = c.baseLanes | n,
            t.memoizedState = null) : r = n,
            we(Gn, ot),
            ot |= r;
        return Qe(e, t, o, n),
        t.child
    }
    function tc(e, t) {
        var n = t.ref;
        (e === null && n !== null || e !== null && e.ref !== n) && (t.flags |= 512,
        t.flags |= 2097152)
    }
    function Ui(e, t, n, r, o) {
        var c = Ze(n) ? pn : Ke.current;
        return c = Fn(t, c),
        Wn(t, o),
        n = Ri(e, t, n, r, c, o),
        r = Oi(),
        e !== null && !et ? (t.updateQueue = e.updateQueue,
        t.flags &= -2053,
        e.lanes &= ~o,
        Dt(e, t, o)) : (Se && r && hi(t),
        t.flags |= 1,
        Qe(e, t, n, o),
        t.child)
    }
    function nc(e, t, n, r, o) {
        if (Ze(n)) {
            var c = !0;
            Es(t)
        } else
            c = !1;
        if (Wn(t, o),
        t.stateNode === null)
            Ks(e, t),
            Hu(t, n, r),
            $i(t, n, r, o),
            r = !0;
        else if (e === null) {
            var p = t.stateNode
              , y = t.memoizedProps;
            p.props = y;
            var N = p.context
              , L = n.contextType;
            typeof L == "object" && L !== null ? L = dt(L) : (L = Ze(n) ? pn : Ke.current,
            L = Fn(t, L));
            var M = n.getDerivedStateFromProps
              , A = typeof M == "function" || typeof p.getSnapshotBeforeUpdate == "function";
            A || typeof p.UNSAFE_componentWillReceiveProps != "function" && typeof p.componentWillReceiveProps != "function" || (y !== r || N !== L) && Ku(t, p, r, L),
            Gt = !1;
            var z = t.memoizedState;
            p.state = z,
            As(t, r, p, o),
            N = t.memoizedState,
            y !== r || z !== N || Xe.current || Gt ? (typeof M == "function" && (Di(t, n, M, r),
            N = t.memoizedState),
            (y = Gt || Vu(t, n, y, r, z, N, L)) ? (A || typeof p.UNSAFE_componentWillMount != "function" && typeof p.componentWillMount != "function" || (typeof p.componentWillMount == "function" && p.componentWillMount(),
            typeof p.UNSAFE_componentWillMount == "function" && p.UNSAFE_componentWillMount()),
            typeof p.componentDidMount == "function" && (t.flags |= 4194308)) : (typeof p.componentDidMount == "function" && (t.flags |= 4194308),
            t.memoizedProps = r,
            t.memoizedState = N),
            p.props = r,
            p.state = N,
            p.context = L,
            r = y) : (typeof p.componentDidMount == "function" && (t.flags |= 4194308),
            r = !1)
        } else {
            p = t.stateNode,
            yu(e, t),
            y = t.memoizedProps,
            L = t.type === t.elementType ? y : vt(t.type, y),
            p.props = L,
            A = t.pendingProps,
            z = p.context,
            N = n.contextType,
            typeof N == "object" && N !== null ? N = dt(N) : (N = Ze(n) ? pn : Ke.current,
            N = Fn(t, N));
            var B = n.getDerivedStateFromProps;
            (M = typeof B == "function" || typeof p.getSnapshotBeforeUpdate == "function") || typeof p.UNSAFE_componentWillReceiveProps != "function" && typeof p.componentWillReceiveProps != "function" || (y !== A || z !== N) && Ku(t, p, r, N),
            Gt = !1,
            z = t.memoizedState,
            p.state = z,
            As(t, r, p, o);
            var q = t.memoizedState;
            y !== A || z !== q || Xe.current || Gt ? (typeof B == "function" && (Di(t, n, B, r),
            q = t.memoizedState),
            (L = Gt || Vu(t, n, L, r, z, q, N) || !1) ? (M || typeof p.UNSAFE_componentWillUpdate != "function" && typeof p.componentWillUpdate != "function" || (typeof p.componentWillUpdate == "function" && p.componentWillUpdate(r, q, N),
            typeof p.UNSAFE_componentWillUpdate == "function" && p.UNSAFE_componentWillUpdate(r, q, N)),
            typeof p.componentDidUpdate == "function" && (t.flags |= 4),
            typeof p.getSnapshotBeforeUpdate == "function" && (t.flags |= 1024)) : (typeof p.componentDidUpdate != "function" || y === e.memoizedProps && z === e.memoizedState || (t.flags |= 4),
            typeof p.getSnapshotBeforeUpdate != "function" || y === e.memoizedProps && z === e.memoizedState || (t.flags |= 1024),
            t.memoizedProps = r,
            t.memoizedState = q),
            p.props = r,
            p.state = q,
            p.context = N,
            r = L) : (typeof p.componentDidUpdate != "function" || y === e.memoizedProps && z === e.memoizedState || (t.flags |= 4),
            typeof p.getSnapshotBeforeUpdate != "function" || y === e.memoizedProps && z === e.memoizedState || (t.flags |= 1024),
            r = !1)
        }
        return Bi(e, t, n, r, c, o)
    }
    function Bi(e, t, n, r, o, c) {
        tc(e, t);
        var p = (t.flags & 128) !== 0;
        if (!r && !p)
            return o && au(t, n, !1),
            Dt(e, t, c);
        r = t.stateNode,
        lh.current = t;
        var y = p && typeof n.getDerivedStateFromError != "function" ? null : r.render();
        return t.flags |= 1,
        e !== null && p ? (t.child = Hn(t, e.child, null, c),
        t.child = Hn(t, null, y, c)) : Qe(e, t, y, c),
        t.memoizedState = r.state,
        o && au(t, n, !0),
        t.child
    }
    function rc(e) {
        var t = e.stateNode;
        t.pendingContext ? lu(e, t.pendingContext, t.pendingContext !== t.context) : t.context && lu(e, t.context, !1),
        Si(e, t.containerInfo)
    }
    function sc(e, t, n, r, o) {
        return Vn(),
        yi(o),
        t.flags |= 256,
        Qe(e, t, n, r),
        t.child
    }
    var Vi = {
        dehydrated: null,
        treeContext: null,
        retryLane: 0
    };
    function Hi(e) {
        return {
            baseLanes: e,
            cachePool: null,
            transitions: null
        }
    }
    function lc(e, t, n) {
        var r = t.pendingProps, o = Ce.current, c = !1, p = (t.flags & 128) !== 0, y;
        if ((y = p) || (y = e !== null && e.memoizedState === null ? !1 : (o & 2) !== 0),
        y ? (c = !0,
        t.flags &= -129) : (e === null || e.memoizedState !== null) && (o |= 1),
        we(Ce, o & 1),
        e === null)
            return xi(t),
            e = t.memoizedState,
            e !== null && (e = e.dehydrated,
            e !== null) ? ((t.mode & 1) === 0 ? t.lanes = 1 : e.data === "$!" ? t.lanes = 8 : t.lanes = 1073741824,
            null) : (p = r.children,
            e = r.fallback,
            c ? (r = t.mode,
            c = t.child,
            p = {
                mode: "hidden",
                children: p
            },
            (r & 1) === 0 && c !== null ? (c.childLanes = 0,
            c.pendingProps = p) : c = rl(p, r, 0, null),
            e = jn(e, r, n, null),
            c.return = t,
            e.return = t,
            c.sibling = e,
            t.child = c,
            t.child.memoizedState = Hi(n),
            t.memoizedState = Vi,
            e) : Ki(t, p));
        if (o = e.memoizedState,
        o !== null && (y = o.dehydrated,
        y !== null))
            return ih(e, t, p, r, y, o, n);
        if (c) {
            c = r.fallback,
            p = t.mode,
            o = e.child,
            y = o.sibling;
            var N = {
                mode: "hidden",
                children: r.children
            };
            return (p & 1) === 0 && t.child !== o ? (r = t.child,
            r.childLanes = 0,
            r.pendingProps = N,
            t.deletions = null) : (r = rn(o, N),
            r.subtreeFlags = o.subtreeFlags & 14680064),
            y !== null ? c = rn(y, c) : (c = jn(c, p, n, null),
            c.flags |= 2),
            c.return = t,
            r.return = t,
            r.sibling = c,
            t.child = r,
            r = c,
            c = t.child,
            p = e.child.memoizedState,
            p = p === null ? Hi(n) : {
                baseLanes: p.baseLanes | n,
                cachePool: null,
                transitions: p.transitions
            },
            c.memoizedState = p,
            c.childLanes = e.childLanes & ~n,
            t.memoizedState = Vi,
            r
        }
        return c = e.child,
        e = c.sibling,
        r = rn(c, {
            mode: "visible",
            children: r.children
        }),
        (t.mode & 1) === 0 && (r.lanes = n),
        r.return = t,
        r.sibling = null,
        e !== null && (n = t.deletions,
        n === null ? (t.deletions = [e],
        t.flags |= 16) : n.push(e)),
        t.child = r,
        t.memoizedState = null,
        r
    }
    function Ki(e, t) {
        return t = rl({
            mode: "visible",
            children: t
        }, e.mode, 0, null),
        t.return = e,
        e.child = t
    }
    function Hs(e, t, n, r) {
        return r !== null && yi(r),
        Hn(t, e.child, null, n),
        e = Ki(t, t.pendingProps.children),
        e.flags |= 2,
        t.memoizedState = null,
        e
    }
    function ih(e, t, n, r, o, c, p) {
        if (n)
            return t.flags & 256 ? (t.flags &= -257,
            r = Ii(Error(l(422))),
            Hs(e, t, p, r)) : t.memoizedState !== null ? (t.child = e.child,
            t.flags |= 128,
            null) : (c = r.fallback,
            o = t.mode,
            r = rl({
                mode: "visible",
                children: r.children
            }, o, 0, null),
            c = jn(c, o, p, null),
            c.flags |= 2,
            r.return = t,
            c.return = t,
            r.sibling = c,
            t.child = r,
            (t.mode & 1) !== 0 && Hn(t, e.child, null, p),
            t.child.memoizedState = Hi(p),
            t.memoizedState = Vi,
            c);
        if ((t.mode & 1) === 0)
            return Hs(e, t, p, null);
        if (o.data === "$!") {
            if (r = o.nextSibling && o.nextSibling.dataset,
            r)
                var y = r.dgst;
            return r = y,
            c = Error(l(419)),
            r = Ii(c, r, void 0),
            Hs(e, t, p, r)
        }
        if (y = (p & e.childLanes) !== 0,
        et || y) {
            if (r = Ie,
            r !== null) {
                switch (p & -p) {
                case 4:
                    o = 2;
                    break;
                case 16:
                    o = 8;
                    break;
                case 64:
                case 128:
                case 256:
                case 512:
                case 1024:
                case 2048:
                case 4096:
                case 8192:
                case 16384:
                case 32768:
                case 65536:
                case 131072:
                case 262144:
                case 524288:
                case 1048576:
                case 2097152:
                case 4194304:
                case 8388608:
                case 16777216:
                case 33554432:
                case 67108864:
                    o = 32;
                    break;
                case 536870912:
                    o = 268435456;
                    break;
                default:
                    o = 0
                }
                o = (o & (r.suspendedLanes | p)) !== 0 ? 0 : o,
                o !== 0 && o !== c.retryLane && (c.retryLane = o,
                Mt(e, o),
                Nt(r, e, o, -1))
            }
            return aa(),
            r = Ii(Error(l(421))),
            Hs(e, t, p, r)
        }
        return o.data === "$?" ? (t.flags |= 128,
        t.child = e.child,
        t = vh.bind(null, e),
        o._reactRetry = t,
        null) : (e = c.treeContext,
        at = Wt(o.nextSibling),
        it = t,
        Se = !0,
        yt = null,
        e !== null && (ut[ct++] = Tt,
        ut[ct++] = zt,
        ut[ct++] = hn,
        Tt = e.id,
        zt = e.overflow,
        hn = t),
        t = Ki(t, r.children),
        t.flags |= 4096,
        t)
    }
    function ic(e, t, n) {
        e.lanes |= t;
        var r = e.alternate;
        r !== null && (r.lanes |= t),
        Ni(e.return, t, n)
    }
    function Wi(e, t, n, r, o) {
        var c = e.memoizedState;
        c === null ? e.memoizedState = {
            isBackwards: t,
            rendering: null,
            renderingStartTime: 0,
            last: r,
            tail: n,
            tailMode: o
        } : (c.isBackwards = t,
        c.rendering = null,
        c.renderingStartTime = 0,
        c.last = r,
        c.tail = n,
        c.tailMode = o)
    }
    function ac(e, t, n) {
        var r = t.pendingProps
          , o = r.revealOrder
          , c = r.tail;
        if (Qe(e, t, r.children, n),
        r = Ce.current,
        (r & 2) !== 0)
            r = r & 1 | 2,
            t.flags |= 128;
        else {
            if (e !== null && (e.flags & 128) !== 0)
                e: for (e = t.child; e !== null; ) {
                    if (e.tag === 13)
                        e.memoizedState !== null && ic(e, n, t);
                    else if (e.tag === 19)
                        ic(e, n, t);
                    else if (e.child !== null) {
                        e.child.return = e,
                        e = e.child;
                        continue
                    }
                    if (e === t)
                        break e;
                    for (; e.sibling === null; ) {
                        if (e.return === null || e.return === t)
                            break e;
                        e = e.return
                    }
                    e.sibling.return = e.return,
                    e = e.sibling
                }
            r &= 1
        }
        if (we(Ce, r),
        (t.mode & 1) === 0)
            t.memoizedState = null;
        else
            switch (o) {
            case "forwards":
                for (n = t.child,
                o = null; n !== null; )
                    e = n.alternate,
                    e !== null && Ds(e) === null && (o = n),
                    n = n.sibling;
                n = o,
                n === null ? (o = t.child,
                t.child = null) : (o = n.sibling,
                n.sibling = null),
                Wi(t, !1, o, n, c);
                break;
            case "backwards":
                for (n = null,
                o = t.child,
                t.child = null; o !== null; ) {
                    if (e = o.alternate,
                    e !== null && Ds(e) === null) {
                        t.child = o;
                        break
                    }
                    e = o.sibling,
                    o.sibling = n,
                    n = o,
                    o = e
                }
                Wi(t, !0, n, null, c);
                break;
            case "together":
                Wi(t, !1, null, null, void 0);
                break;
            default:
                t.memoizedState = null
            }
        return t.child
    }
    function Ks(e, t) {
        (t.mode & 1) === 0 && e !== null && (e.alternate = null,
        t.alternate = null,
        t.flags |= 2)
    }
    function Dt(e, t, n) {
        if (e !== null && (t.dependencies = e.dependencies),
        vn |= t.lanes,
        (n & t.childLanes) === 0)
            return null;
        if (e !== null && t.child !== e.child)
            throw Error(l(153));
        if (t.child !== null) {
            for (e = t.child,
            n = rn(e, e.pendingProps),
            t.child = n,
            n.return = t; e.sibling !== null; )
                e = e.sibling,
                n = n.sibling = rn(e, e.pendingProps),
                n.return = t;
            n.sibling = null
        }
        return t.child
    }
    function ah(e, t, n) {
        switch (t.tag) {
        case 3:
            rc(t),
            Vn();
            break;
        case 5:
            bu(t);
            break;
        case 1:
            Ze(t.type) && Es(t);
            break;
        case 4:
            Si(t, t.stateNode.containerInfo);
            break;
        case 10:
            var r = t.type._context
              , o = t.memoizedProps.value;
            we(Ts, r._currentValue),
            r._currentValue = o;
            break;
        case 13:
            if (r = t.memoizedState,
            r !== null)
                return r.dehydrated !== null ? (we(Ce, Ce.current & 1),
                t.flags |= 128,
                null) : (n & t.child.childLanes) !== 0 ? lc(e, t, n) : (we(Ce, Ce.current & 1),
                e = Dt(e, t, n),
                e !== null ? e.sibling : null);
            we(Ce, Ce.current & 1);
            break;
        case 19:
            if (r = (n & t.childLanes) !== 0,
            (e.flags & 128) !== 0) {
                if (r)
                    return ac(e, t, n);
                t.flags |= 128
            }
            if (o = t.memoizedState,
            o !== null && (o.rendering = null,
            o.tail = null,
            o.lastEffect = null),
            we(Ce, Ce.current),
            r)
                break;
            return null;
        case 22:
        case 23:
            return t.lanes = 0,
            ec(e, t, n)
        }
        return Dt(e, t, n)
    }
    var oc, qi, uc, cc;
    oc = function(e, t) {
        for (var n = t.child; n !== null; ) {
            if (n.tag === 5 || n.tag === 6)
                e.appendChild(n.stateNode);
            else if (n.tag !== 4 && n.child !== null) {
                n.child.return = n,
                n = n.child;
                continue
            }
            if (n === t)
                break;
            for (; n.sibling === null; ) {
                if (n.return === null || n.return === t)
                    return;
                n = n.return
            }
            n.sibling.return = n.return,
            n = n.sibling
        }
    }
    ,
    qi = function() {}
    ,
    uc = function(e, t, n, r) {
        var o = e.memoizedProps;
        if (o !== r) {
            e = t.stateNode,
            xn(St.current);
            var c = null;
            switch (n) {
            case "input":
                o = Nl(e, o),
                r = Nl(e, r),
                c = [];
                break;
            case "select":
                o = U({}, o, {
                    value: void 0
                }),
                r = U({}, r, {
                    value: void 0
                }),
                c = [];
                break;
            case "textarea":
                o = Sl(e, o),
                r = Sl(e, r),
                c = [];
                break;
            default:
                typeof o.onClick != "function" && typeof r.onClick == "function" && (e.onclick = ks)
            }
            El(n, r);
            var p;
            n = null;
            for (L in o)
                if (!r.hasOwnProperty(L) && o.hasOwnProperty(L) && o[L] != null)
                    if (L === "style") {
                        var y = o[L];
                        for (p in y)
                            y.hasOwnProperty(p) && (n || (n = {}),
                            n[p] = "")
                    } else
                        L !== "dangerouslySetInnerHTML" && L !== "children" && L !== "suppressContentEditableWarning" && L !== "suppressHydrationWarning" && L !== "autoFocus" && (d.hasOwnProperty(L) ? c || (c = []) : (c = c || []).push(L, null));
            for (L in r) {
                var N = r[L];
                if (y = o != null ? o[L] : void 0,
                r.hasOwnProperty(L) && N !== y && (N != null || y != null))
                    if (L === "style")
                        if (y) {
                            for (p in y)
                                !y.hasOwnProperty(p) || N && N.hasOwnProperty(p) || (n || (n = {}),
                                n[p] = "");
                            for (p in N)
                                N.hasOwnProperty(p) && y[p] !== N[p] && (n || (n = {}),
                                n[p] = N[p])
                        } else
                            n || (c || (c = []),
                            c.push(L, n)),
                            n = N;
                    else
                        L === "dangerouslySetInnerHTML" ? (N = N ? N.__html : void 0,
                        y = y ? y.__html : void 0,
                        N != null && y !== N && (c = c || []).push(L, N)) : L === "children" ? typeof N != "string" && typeof N != "number" || (c = c || []).push(L, "" + N) : L !== "suppressContentEditableWarning" && L !== "suppressHydrationWarning" && (d.hasOwnProperty(L) ? (N != null && L === "onScroll" && be("scroll", e),
                        c || y === N || (c = [])) : (c = c || []).push(L, N))
            }
            n && (c = c || []).push("style", n);
            var L = c;
            (t.updateQueue = L) && (t.flags |= 4)
        }
    }
    ,
    cc = function(e, t, n, r) {
        n !== r && (t.flags |= 4)
    }
    ;
    function Dr(e, t) {
        if (!Se)
            switch (e.tailMode) {
            case "hidden":
                t = e.tail;
                for (var n = null; t !== null; )
                    t.alternate !== null && (n = t),
                    t = t.sibling;
                n === null ? e.tail = null : n.sibling = null;
                break;
            case "collapsed":
                n = e.tail;
                for (var r = null; n !== null; )
                    n.alternate !== null && (r = n),
                    n = n.sibling;
                r === null ? t || e.tail === null ? e.tail = null : e.tail.sibling = null : r.sibling = null
            }
    }
    function qe(e) {
        var t = e.alternate !== null && e.alternate.child === e.child
          , n = 0
          , r = 0;
        if (t)
            for (var o = e.child; o !== null; )
                n |= o.lanes | o.childLanes,
                r |= o.subtreeFlags & 14680064,
                r |= o.flags & 14680064,
                o.return = e,
                o = o.sibling;
        else
            for (o = e.child; o !== null; )
                n |= o.lanes | o.childLanes,
                r |= o.subtreeFlags,
                r |= o.flags,
                o.return = e,
                o = o.sibling;
        return e.subtreeFlags |= r,
        e.childLanes = n,
        t
    }
    function oh(e, t, n) {
        var r = t.pendingProps;
        switch (mi(t),
        t.tag) {
        case 2:
        case 16:
        case 15:
        case 0:
        case 11:
        case 7:
        case 8:
        case 12:
        case 9:
        case 14:
            return qe(t),
            null;
        case 1:
            return Ze(t.type) && Cs(),
            qe(t),
            null;
        case 3:
            return r = t.stateNode,
            qn(),
            Ne(Xe),
            Ne(Ke),
            Pi(),
            r.pendingContext && (r.context = r.pendingContext,
            r.pendingContext = null),
            (e === null || e.child === null) && (Rs(t) ? t.flags |= 4 : e === null || e.memoizedState.isDehydrated && (t.flags & 256) === 0 || (t.flags |= 1024,
            yt !== null && (sa(yt),
            yt = null))),
            qi(e, t),
            qe(t),
            null;
        case 5:
            Ci(t);
            var o = xn(Or.current);
            if (n = t.type,
            e !== null && t.stateNode != null)
                uc(e, t, n, r, o),
                e.ref !== t.ref && (t.flags |= 512,
                t.flags |= 2097152);
            else {
                if (!r) {
                    if (t.stateNode === null)
                        throw Error(l(166));
                    return qe(t),
                    null
                }
                if (e = xn(St.current),
                Rs(t)) {
                    r = t.stateNode,
                    n = t.type;
                    var c = t.memoizedProps;
                    switch (r[kt] = t,
                    r[Er] = c,
                    e = (t.mode & 1) !== 0,
                    n) {
                    case "dialog":
                        be("cancel", r),
                        be("close", r);
                        break;
                    case "iframe":
                    case "object":
                    case "embed":
                        be("load", r);
                        break;
                    case "video":
                    case "audio":
                        for (o = 0; o < kr.length; o++)
                            be(kr[o], r);
                        break;
                    case "source":
                        be("error", r);
                        break;
                    case "img":
                    case "image":
                    case "link":
                        be("error", r),
                        be("load", r);
                        break;
                    case "details":
                        be("toggle", r);
                        break;
                    case "input":
                        Va(r, c),
                        be("invalid", r);
                        break;
                    case "select":
                        r._wrapperState = {
                            wasMultiple: !!c.multiple
                        },
                        be("invalid", r);
                        break;
                    case "textarea":
                        Wa(r, c),
                        be("invalid", r)
                    }
                    El(n, c),
                    o = null;
                    for (var p in c)
                        if (c.hasOwnProperty(p)) {
                            var y = c[p];
                            p === "children" ? typeof y == "string" ? r.textContent !== y && (c.suppressHydrationWarning !== !0 && js(r.textContent, y, e),
                            o = ["children", y]) : typeof y == "number" && r.textContent !== "" + y && (c.suppressHydrationWarning !== !0 && js(r.textContent, y, e),
                            o = ["children", "" + y]) : d.hasOwnProperty(p) && y != null && p === "onScroll" && be("scroll", r)
                        }
                    switch (n) {
                    case "input":
                        es(r),
                        Ka(r, c, !0);
                        break;
                    case "textarea":
                        es(r),
                        Ya(r);
                        break;
                    case "select":
                    case "option":
                        break;
                    default:
                        typeof c.onClick == "function" && (r.onclick = ks)
                    }
                    r = o,
                    t.updateQueue = r,
                    r !== null && (t.flags |= 4)
                } else {
                    p = o.nodeType === 9 ? o : o.ownerDocument,
                    e === "http://www.w3.org/1999/xhtml" && (e = Qa(n)),
                    e === "http://www.w3.org/1999/xhtml" ? n === "script" ? (e = p.createElement("div"),
                    e.innerHTML = "<script><\/script>",
                    e = e.removeChild(e.firstChild)) : typeof r.is == "string" ? e = p.createElement(n, {
                        is: r.is
                    }) : (e = p.createElement(n),
                    n === "select" && (p = e,
                    r.multiple ? p.multiple = !0 : r.size && (p.size = r.size))) : e = p.createElementNS(e, n),
                    e[kt] = t,
                    e[Er] = r,
                    oc(e, t, !1, !1),
                    t.stateNode = e;
                    e: {
                        switch (p = Pl(n, r),
                        n) {
                        case "dialog":
                            be("cancel", e),
                            be("close", e),
                            o = r;
                            break;
                        case "iframe":
                        case "object":
                        case "embed":
                            be("load", e),
                            o = r;
                            break;
                        case "video":
                        case "audio":
                            for (o = 0; o < kr.length; o++)
                                be(kr[o], e);
                            o = r;
                            break;
                        case "source":
                            be("error", e),
                            o = r;
                            break;
                        case "img":
                        case "image":
                        case "link":
                            be("error", e),
                            be("load", e),
                            o = r;
                            break;
                        case "details":
                            be("toggle", e),
                            o = r;
                            break;
                        case "input":
                            Va(e, r),
                            o = Nl(e, r),
                            be("invalid", e);
                            break;
                        case "option":
                            o = r;
                            break;
                        case "select":
                            e._wrapperState = {
                                wasMultiple: !!r.multiple
                            },
                            o = U({}, r, {
                                value: void 0
                            }),
                            be("invalid", e);
                            break;
                        case "textarea":
                            Wa(e, r),
                            o = Sl(e, r),
                            be("invalid", e);
                            break;
                        default:
                            o = r
                        }
                        El(n, o),
                        y = o;
                        for (c in y)
                            if (y.hasOwnProperty(c)) {
                                var N = y[c];
                                c === "style" ? Xa(e, N) : c === "dangerouslySetInnerHTML" ? (N = N ? N.__html : void 0,
                                N != null && Ga(e, N)) : c === "children" ? typeof N == "string" ? (n !== "textarea" || N !== "") && lr(e, N) : typeof N == "number" && lr(e, "" + N) : c !== "suppressContentEditableWarning" && c !== "suppressHydrationWarning" && c !== "autoFocus" && (d.hasOwnProperty(c) ? N != null && c === "onScroll" && be("scroll", e) : N != null && V(e, c, N, p))
                            }
                        switch (n) {
                        case "input":
                            es(e),
                            Ka(e, r, !1);
                            break;
                        case "textarea":
                            es(e),
                            Ya(e);
                            break;
                        case "option":
                            r.value != null && e.setAttribute("value", "" + ge(r.value));
                            break;
                        case "select":
                            e.multiple = !!r.multiple,
                            c = r.value,
                            c != null ? Pn(e, !!r.multiple, c, !1) : r.defaultValue != null && Pn(e, !!r.multiple, r.defaultValue, !0);
                            break;
                        default:
                            typeof o.onClick == "function" && (e.onclick = ks)
                        }
                        switch (n) {
                        case "button":
                        case "input":
                        case "select":
                        case "textarea":
                            r = !!r.autoFocus;
                            break e;
                        case "img":
                            r = !0;
                            break e;
                        default:
                            r = !1
                        }
                    }
                    r && (t.flags |= 4)
                }
                t.ref !== null && (t.flags |= 512,
                t.flags |= 2097152)
            }
            return qe(t),
            null;
        case 6:
            if (e && t.stateNode != null)
                cc(e, t, e.memoizedProps, r);
            else {
                if (typeof r != "string" && t.stateNode === null)
                    throw Error(l(166));
                if (n = xn(Or.current),
                xn(St.current),
                Rs(t)) {
                    if (r = t.stateNode,
                    n = t.memoizedProps,
                    r[kt] = t,
                    (c = r.nodeValue !== n) && (e = it,
                    e !== null))
                        switch (e.tag) {
                        case 3:
                            js(r.nodeValue, n, (e.mode & 1) !== 0);
                            break;
                        case 5:
                            e.memoizedProps.suppressHydrationWarning !== !0 && js(r.nodeValue, n, (e.mode & 1) !== 0)
                        }
                    c && (t.flags |= 4)
                } else
                    r = (n.nodeType === 9 ? n : n.ownerDocument).createTextNode(r),
                    r[kt] = t,
                    t.stateNode = r
            }
            return qe(t),
            null;
        case 13:
            if (Ne(Ce),
            r = t.memoizedState,
            e === null || e.memoizedState !== null && e.memoizedState.dehydrated !== null) {
                if (Se && at !== null && (t.mode & 1) !== 0 && (t.flags & 128) === 0)
                    pu(),
                    Vn(),
                    t.flags |= 98560,
                    c = !1;
                else if (c = Rs(t),
                r !== null && r.dehydrated !== null) {
                    if (e === null) {
                        if (!c)
                            throw Error(l(318));
                        if (c = t.memoizedState,
                        c = c !== null ? c.dehydrated : null,
                        !c)
                            throw Error(l(317));
                        c[kt] = t
                    } else
                        Vn(),
                        (t.flags & 128) === 0 && (t.memoizedState = null),
                        t.flags |= 4;
                    qe(t),
                    c = !1
                } else
                    yt !== null && (sa(yt),
                    yt = null),
                    c = !0;
                if (!c)
                    return t.flags & 65536 ? t : null
            }
            return (t.flags & 128) !== 0 ? (t.lanes = n,
            t) : (r = r !== null,
            r !== (e !== null && e.memoizedState !== null) && r && (t.child.flags |= 8192,
            (t.mode & 1) !== 0 && (e === null || (Ce.current & 1) !== 0 ? Ae === 0 && (Ae = 3) : aa())),
            t.updateQueue !== null && (t.flags |= 4),
            qe(t),
            null);
        case 4:
            return qn(),
            qi(e, t),
            e === null && Sr(t.stateNode.containerInfo),
            qe(t),
            null;
        case 10:
            return bi(t.type._context),
            qe(t),
            null;
        case 17:
            return Ze(t.type) && Cs(),
            qe(t),
            null;
        case 19:
            if (Ne(Ce),
            c = t.memoizedState,
            c === null)
                return qe(t),
                null;
            if (r = (t.flags & 128) !== 0,
            p = c.rendering,
            p === null)
                if (r)
                    Dr(c, !1);
                else {
                    if (Ae !== 0 || e !== null && (e.flags & 128) !== 0)
                        for (e = t.child; e !== null; ) {
                            if (p = Ds(e),
                            p !== null) {
                                for (t.flags |= 128,
                                Dr(c, !1),
                                r = p.updateQueue,
                                r !== null && (t.updateQueue = r,
                                t.flags |= 4),
                                t.subtreeFlags = 0,
                                r = n,
                                n = t.child; n !== null; )
                                    c = n,
                                    e = r,
                                    c.flags &= 14680066,
                                    p = c.alternate,
                                    p === null ? (c.childLanes = 0,
                                    c.lanes = e,
                                    c.child = null,
                                    c.subtreeFlags = 0,
                                    c.memoizedProps = null,
                                    c.memoizedState = null,
                                    c.updateQueue = null,
                                    c.dependencies = null,
                                    c.stateNode = null) : (c.childLanes = p.childLanes,
                                    c.lanes = p.lanes,
                                    c.child = p.child,
                                    c.subtreeFlags = 0,
                                    c.deletions = null,
                                    c.memoizedProps = p.memoizedProps,
                                    c.memoizedState = p.memoizedState,
                                    c.updateQueue = p.updateQueue,
                                    c.type = p.type,
                                    e = p.dependencies,
                                    c.dependencies = e === null ? null : {
                                        lanes: e.lanes,
                                        firstContext: e.firstContext
                                    }),
                                    n = n.sibling;
                                return we(Ce, Ce.current & 1 | 2),
                                t.child
                            }
                            e = e.sibling
                        }
                    c.tail !== null && _e() > Jn && (t.flags |= 128,
                    r = !0,
                    Dr(c, !1),
                    t.lanes = 4194304)
                }
            else {
                if (!r)
                    if (e = Ds(p),
                    e !== null) {
                        if (t.flags |= 128,
                        r = !0,
                        n = e.updateQueue,
                        n !== null && (t.updateQueue = n,
                        t.flags |= 4),
                        Dr(c, !0),
                        c.tail === null && c.tailMode === "hidden" && !p.alternate && !Se)
                            return qe(t),
                            null
                    } else
                        2 * _e() - c.renderingStartTime > Jn && n !== 1073741824 && (t.flags |= 128,
                        r = !0,
                        Dr(c, !1),
                        t.lanes = 4194304);
                c.isBackwards ? (p.sibling = t.child,
                t.child = p) : (n = c.last,
                n !== null ? n.sibling = p : t.child = p,
                c.last = p)
            }
            return c.tail !== null ? (t = c.tail,
            c.rendering = t,
            c.tail = t.sibling,
            c.renderingStartTime = _e(),
            t.sibling = null,
            n = Ce.current,
            we(Ce, r ? n & 1 | 2 : n & 1),
            t) : (qe(t),
            null);
        case 22:
        case 23:
            return ia(),
            r = t.memoizedState !== null,
            e !== null && e.memoizedState !== null !== r && (t.flags |= 8192),
            r && (t.mode & 1) !== 0 ? (ot & 1073741824) !== 0 && (qe(t),
            t.subtreeFlags & 6 && (t.flags |= 8192)) : qe(t),
            null;
        case 24:
            return null;
        case 25:
            return null
        }
        throw Error(l(156, t.tag))
    }
    function uh(e, t) {
        switch (mi(t),
        t.tag) {
        case 1:
            return Ze(t.type) && Cs(),
            e = t.flags,
            e & 65536 ? (t.flags = e & -65537 | 128,
            t) : null;
        case 3:
            return qn(),
            Ne(Xe),
            Ne(Ke),
            Pi(),
            e = t.flags,
            (e & 65536) !== 0 && (e & 128) === 0 ? (t.flags = e & -65537 | 128,
            t) : null;
        case 5:
            return Ci(t),
            null;
        case 13:
            if (Ne(Ce),
            e = t.memoizedState,
            e !== null && e.dehydrated !== null) {
                if (t.alternate === null)
                    throw Error(l(340));
                Vn()
            }
            return e = t.flags,
            e & 65536 ? (t.flags = e & -65537 | 128,
            t) : null;
        case 19:
            return Ne(Ce),
            null;
        case 4:
            return qn(),
            null;
        case 10:
            return bi(t.type._context),
            null;
        case 22:
        case 23:
            return ia(),
            null;
        case 24:
            return null;
        default:
            return null
        }
    }
    var Ws = !1
      , Ye = !1
      , ch = typeof WeakSet == "function" ? WeakSet : Set
      , W = null;
    function Qn(e, t) {
        var n = e.ref;
        if (n !== null)
            if (typeof n == "function")
                try {
                    n(null)
                } catch (r) {
                    Le(e, t, r)
                }
            else
                n.current = null
    }
    function Yi(e, t, n) {
        try {
            n()
        } catch (r) {
            Le(e, t, r)
        }
    }
    var dc = !1;
    function dh(e, t) {
        if (ii = fs,
        e = Vo(),
        Xl(e)) {
            if ("selectionStart" in e)
                var n = {
                    start: e.selectionStart,
                    end: e.selectionEnd
                };
            else
                e: {
                    n = (n = e.ownerDocument) && n.defaultView || window;
                    var r = n.getSelection && n.getSelection();
                    if (r && r.rangeCount !== 0) {
                        n = r.anchorNode;
                        var o = r.anchorOffset
                          , c = r.focusNode;
                        r = r.focusOffset;
                        try {
                            n.nodeType,
                            c.nodeType
                        } catch {
                            n = null;
                            break e
                        }
                        var p = 0
                          , y = -1
                          , N = -1
                          , L = 0
                          , M = 0
                          , A = e
                          , z = null;
                        t: for (; ; ) {
                            for (var B; A !== n || o !== 0 && A.nodeType !== 3 || (y = p + o),
                            A !== c || r !== 0 && A.nodeType !== 3 || (N = p + r),
                            A.nodeType === 3 && (p += A.nodeValue.length),
                            (B = A.firstChild) !== null; )
                                z = A,
                                A = B;
                            for (; ; ) {
                                if (A === e)
                                    break t;
                                if (z === n && ++L === o && (y = p),
                                z === c && ++M === r && (N = p),
                                (B = A.nextSibling) !== null)
                                    break;
                                A = z,
                                z = A.parentNode
                            }
                            A = B
                        }
                        n = y === -1 || N === -1 ? null : {
                            start: y,
                            end: N
                        }
                    } else
                        n = null
                }
            n = n || {
                start: 0,
                end: 0
            }
        } else
            n = null;
        for (ai = {
            focusedElem: e,
            selectionRange: n
        },
        fs = !1,
        W = t; W !== null; )
            if (t = W,
            e = t.child,
            (t.subtreeFlags & 1028) !== 0 && e !== null)
                e.return = t,
                W = e;
            else
                for (; W !== null; ) {
                    t = W;
                    try {
                        var q = t.alternate;
                        if ((t.flags & 1024) !== 0)
                            switch (t.tag) {
                            case 0:
                            case 11:
                            case 15:
                                break;
                            case 1:
                                if (q !== null) {
                                    var Q = q.memoizedProps
                                      , Re = q.memoizedState
                                      , S = t.stateNode
                                      , j = S.getSnapshotBeforeUpdate(t.elementType === t.type ? Q : vt(t.type, Q), Re);
                                    S.__reactInternalSnapshotBeforeUpdate = j
                                }
                                break;
                            case 3:
                                var C = t.stateNode.containerInfo;
                                C.nodeType === 1 ? C.textContent = "" : C.nodeType === 9 && C.documentElement && C.removeChild(C.documentElement);
                                break;
                            case 5:
                            case 6:
                            case 4:
                            case 17:
                                break;
                            default:
                                throw Error(l(163))
                            }
                    } catch (D) {
                        Le(t, t.return, D)
                    }
                    if (e = t.sibling,
                    e !== null) {
                        e.return = t.return,
                        W = e;
                        break
                    }
                    W = t.return
                }
        return q = dc,
        dc = !1,
        q
    }
    function $r(e, t, n) {
        var r = t.updateQueue;
        if (r = r !== null ? r.lastEffect : null,
        r !== null) {
            var o = r = r.next;
            do {
                if ((o.tag & e) === e) {
                    var c = o.destroy;
                    o.destroy = void 0,
                    c !== void 0 && Yi(t, n, c)
                }
                o = o.next
            } while (o !== r)
        }
    }
    function qs(e, t) {
        if (t = t.updateQueue,
        t = t !== null ? t.lastEffect : null,
        t !== null) {
            var n = t = t.next;
            do {
                if ((n.tag & e) === e) {
                    var r = n.create;
                    n.destroy = r()
                }
                n = n.next
            } while (n !== t)
        }
    }
    function Qi(e) {
        var t = e.ref;
        if (t !== null) {
            var n = e.stateNode;
            switch (e.tag) {
            case 5:
                e = n;
                break;
            default:
                e = n
            }
            typeof t == "function" ? t(e) : t.current = e
        }
    }
    function fc(e) {
        var t = e.alternate;
        t !== null && (e.alternate = null,
        fc(t)),
        e.child = null,
        e.deletions = null,
        e.sibling = null,
        e.tag === 5 && (t = e.stateNode,
        t !== null && (delete t[kt],
        delete t[Er],
        delete t[di],
        delete t[qp],
        delete t[Yp])),
        e.stateNode = null,
        e.return = null,
        e.dependencies = null,
        e.memoizedProps = null,
        e.memoizedState = null,
        e.pendingProps = null,
        e.stateNode = null,
        e.updateQueue = null
    }
    function pc(e) {
        return e.tag === 5 || e.tag === 3 || e.tag === 4
    }
    function hc(e) {
        e: for (; ; ) {
            for (; e.sibling === null; ) {
                if (e.return === null || pc(e.return))
                    return null;
                e = e.return
            }
            for (e.sibling.return = e.return,
            e = e.sibling; e.tag !== 5 && e.tag !== 6 && e.tag !== 18; ) {
                if (e.flags & 2 || e.child === null || e.tag === 4)
                    continue e;
                e.child.return = e,
                e = e.child
            }
            if (!(e.flags & 2))
                return e.stateNode
        }
    }
    function Gi(e, t, n) {
        var r = e.tag;
        if (r === 5 || r === 6)
            e = e.stateNode,
            t ? n.nodeType === 8 ? n.parentNode.insertBefore(e, t) : n.insertBefore(e, t) : (n.nodeType === 8 ? (t = n.parentNode,
            t.insertBefore(e, n)) : (t = n,
            t.appendChild(e)),
            n = n._reactRootContainer,
            n != null || t.onclick !== null || (t.onclick = ks));
        else if (r !== 4 && (e = e.child,
        e !== null))
            for (Gi(e, t, n),
            e = e.sibling; e !== null; )
                Gi(e, t, n),
                e = e.sibling
    }
    function Ji(e, t, n) {
        var r = e.tag;
        if (r === 5 || r === 6)
            e = e.stateNode,
            t ? n.insertBefore(e, t) : n.appendChild(e);
        else if (r !== 4 && (e = e.child,
        e !== null))
            for (Ji(e, t, n),
            e = e.sibling; e !== null; )
                Ji(e, t, n),
                e = e.sibling
    }
    var Be = null
      , wt = !1;
    function Xt(e, t, n) {
        for (n = n.child; n !== null; )
            mc(e, t, n),
            n = n.sibling
    }
    function mc(e, t, n) {
        if (jt && typeof jt.onCommitFiberUnmount == "function")
            try {
                jt.onCommitFiberUnmount(is, n)
            } catch {}
        switch (n.tag) {
        case 5:
            Ye || Qn(n, t);
        case 6:
            var r = Be
              , o = wt;
            Be = null,
            Xt(e, t, n),
            Be = r,
            wt = o,
            Be !== null && (wt ? (e = Be,
            n = n.stateNode,
            e.nodeType === 8 ? e.parentNode.removeChild(n) : e.removeChild(n)) : Be.removeChild(n.stateNode));
            break;
        case 18:
            Be !== null && (wt ? (e = Be,
            n = n.stateNode,
            e.nodeType === 8 ? ci(e.parentNode, n) : e.nodeType === 1 && ci(e, n),
            gr(e)) : ci(Be, n.stateNode));
            break;
        case 4:
            r = Be,
            o = wt,
            Be = n.stateNode.containerInfo,
            wt = !0,
            Xt(e, t, n),
            Be = r,
            wt = o;
            break;
        case 0:
        case 11:
        case 14:
        case 15:
            if (!Ye && (r = n.updateQueue,
            r !== null && (r = r.lastEffect,
            r !== null))) {
                o = r = r.next;
                do {
                    var c = o
                      , p = c.destroy;
                    c = c.tag,
                    p !== void 0 && ((c & 2) !== 0 || (c & 4) !== 0) && Yi(n, t, p),
                    o = o.next
                } while (o !== r)
            }
            Xt(e, t, n);
            break;
        case 1:
            if (!Ye && (Qn(n, t),
            r = n.stateNode,
            typeof r.componentWillUnmount == "function"))
                try {
                    r.props = n.memoizedProps,
                    r.state = n.memoizedState,
                    r.componentWillUnmount()
                } catch (y) {
                    Le(n, t, y)
                }
            Xt(e, t, n);
            break;
        case 21:
            Xt(e, t, n);
            break;
        case 22:
            n.mode & 1 ? (Ye = (r = Ye) || n.memoizedState !== null,
            Xt(e, t, n),
            Ye = r) : Xt(e, t, n);
            break;
        default:
            Xt(e, t, n)
        }
    }
    function gc(e) {
        var t = e.updateQueue;
        if (t !== null) {
            e.updateQueue = null;
            var n = e.stateNode;
            n === null && (n = e.stateNode = new ch),
            t.forEach(function(r) {
                var o = wh.bind(null, e, r);
                n.has(r) || (n.add(r),
                r.then(o, o))
            })
        }
    }
    function bt(e, t) {
        var n = t.deletions;
        if (n !== null)
            for (var r = 0; r < n.length; r++) {
                var o = n[r];
                try {
                    var c = e
                      , p = t
                      , y = p;
                    e: for (; y !== null; ) {
                        switch (y.tag) {
                        case 5:
                            Be = y.stateNode,
                            wt = !1;
                            break e;
                        case 3:
                            Be = y.stateNode.containerInfo,
                            wt = !0;
                            break e;
                        case 4:
                            Be = y.stateNode.containerInfo,
                            wt = !0;
                            break e
                        }
                        y = y.return
                    }
                    if (Be === null)
                        throw Error(l(160));
                    mc(c, p, o),
                    Be = null,
                    wt = !1;
                    var N = o.alternate;
                    N !== null && (N.return = null),
                    o.return = null
                } catch (L) {
                    Le(o, t, L)
                }
            }
        if (t.subtreeFlags & 12854)
            for (t = t.child; t !== null; )
                xc(t, e),
                t = t.sibling
    }
    function xc(e, t) {
        var n = e.alternate
          , r = e.flags;
        switch (e.tag) {
        case 0:
        case 11:
        case 14:
        case 15:
            if (bt(t, e),
            Et(e),
            r & 4) {
                try {
                    $r(3, e, e.return),
                    qs(3, e)
                } catch (Q) {
                    Le(e, e.return, Q)
                }
                try {
                    $r(5, e, e.return)
                } catch (Q) {
                    Le(e, e.return, Q)
                }
            }
            break;
        case 1:
            bt(t, e),
            Et(e),
            r & 512 && n !== null && Qn(n, n.return);
            break;
        case 5:
            if (bt(t, e),
            Et(e),
            r & 512 && n !== null && Qn(n, n.return),
            e.flags & 32) {
                var o = e.stateNode;
                try {
                    lr(o, "")
                } catch (Q) {
                    Le(e, e.return, Q)
                }
            }
            if (r & 4 && (o = e.stateNode,
            o != null)) {
                var c = e.memoizedProps
                  , p = n !== null ? n.memoizedProps : c
                  , y = e.type
                  , N = e.updateQueue;
                if (e.updateQueue = null,
                N !== null)
                    try {
                        y === "input" && c.type === "radio" && c.name != null && Ha(o, c),
                        Pl(y, p);
                        var L = Pl(y, c);
                        for (p = 0; p < N.length; p += 2) {
                            var M = N[p]
                              , A = N[p + 1];
                            M === "style" ? Xa(o, A) : M === "dangerouslySetInnerHTML" ? Ga(o, A) : M === "children" ? lr(o, A) : V(o, M, A, L)
                        }
                        switch (y) {
                        case "input":
                            jl(o, c);
                            break;
                        case "textarea":
                            qa(o, c);
                            break;
                        case "select":
                            var z = o._wrapperState.wasMultiple;
                            o._wrapperState.wasMultiple = !!c.multiple;
                            var B = c.value;
                            B != null ? Pn(o, !!c.multiple, B, !1) : z !== !!c.multiple && (c.defaultValue != null ? Pn(o, !!c.multiple, c.defaultValue, !0) : Pn(o, !!c.multiple, c.multiple ? [] : "", !1))
                        }
                        o[Er] = c
                    } catch (Q) {
                        Le(e, e.return, Q)
                    }
            }
            break;
        case 6:
            if (bt(t, e),
            Et(e),
            r & 4) {
                if (e.stateNode === null)
                    throw Error(l(162));
                o = e.stateNode,
                c = e.memoizedProps;
                try {
                    o.nodeValue = c
                } catch (Q) {
                    Le(e, e.return, Q)
                }
            }
            break;
        case 3:
            if (bt(t, e),
            Et(e),
            r & 4 && n !== null && n.memoizedState.isDehydrated)
                try {
                    gr(t.containerInfo)
                } catch (Q) {
                    Le(e, e.return, Q)
                }
            break;
        case 4:
            bt(t, e),
            Et(e);
            break;
        case 13:
            bt(t, e),
            Et(e),
            o = e.child,
            o.flags & 8192 && (c = o.memoizedState !== null,
            o.stateNode.isHidden = c,
            !c || o.alternate !== null && o.alternate.memoizedState !== null || (ea = _e())),
            r & 4 && gc(e);
            break;
        case 22:
            if (M = n !== null && n.memoizedState !== null,
            e.mode & 1 ? (Ye = (L = Ye) || M,
            bt(t, e),
            Ye = L) : bt(t, e),
            Et(e),
            r & 8192) {
                if (L = e.memoizedState !== null,
                (e.stateNode.isHidden = L) && !M && (e.mode & 1) !== 0)
                    for (W = e,
                    M = e.child; M !== null; ) {
                        for (A = W = M; W !== null; ) {
                            switch (z = W,
                            B = z.child,
                            z.tag) {
                            case 0:
                            case 11:
                            case 14:
                            case 15:
                                $r(4, z, z.return);
                                break;
                            case 1:
                                Qn(z, z.return);
                                var q = z.stateNode;
                                if (typeof q.componentWillUnmount == "function") {
                                    r = z,
                                    n = z.return;
                                    try {
                                        t = r,
                                        q.props = t.memoizedProps,
                                        q.state = t.memoizedState,
                                        q.componentWillUnmount()
                                    } catch (Q) {
                                        Le(r, n, Q)
                                    }
                                }
                                break;
                            case 5:
                                Qn(z, z.return);
                                break;
                            case 22:
                                if (z.memoizedState !== null) {
                                    wc(A);
                                    continue
                                }
                            }
                            B !== null ? (B.return = z,
                            W = B) : wc(A)
                        }
                        M = M.sibling
                    }
                e: for (M = null,
                A = e; ; ) {
                    if (A.tag === 5) {
                        if (M === null) {
                            M = A;
                            try {
                                o = A.stateNode,
                                L ? (c = o.style,
                                typeof c.setProperty == "function" ? c.setProperty("display", "none", "important") : c.display = "none") : (y = A.stateNode,
                                N = A.memoizedProps.style,
                                p = N != null && N.hasOwnProperty("display") ? N.display : null,
                                y.style.display = Ja("display", p))
                            } catch (Q) {
                                Le(e, e.return, Q)
                            }
                        }
                    } else if (A.tag === 6) {
                        if (M === null)
                            try {
                                A.stateNode.nodeValue = L ? "" : A.memoizedProps
                            } catch (Q) {
                                Le(e, e.return, Q)
                            }
                    } else if ((A.tag !== 22 && A.tag !== 23 || A.memoizedState === null || A === e) && A.child !== null) {
                        A.child.return = A,
                        A = A.child;
                        continue
                    }
                    if (A === e)
                        break e;
                    for (; A.sibling === null; ) {
                        if (A.return === null || A.return === e)
                            break e;
                        M === A && (M = null),
                        A = A.return
                    }
                    M === A && (M = null),
                    A.sibling.return = A.return,
                    A = A.sibling
                }
            }
            break;
        case 19:
            bt(t, e),
            Et(e),
            r & 4 && gc(e);
            break;
        case 21:
            break;
        default:
            bt(t, e),
            Et(e)
        }
    }
    function Et(e) {
        var t = e.flags;
        if (t & 2) {
            try {
                e: {
                    for (var n = e.return; n !== null; ) {
                        if (pc(n)) {
                            var r = n;
                            break e
                        }
                        n = n.return
                    }
                    throw Error(l(160))
                }
                switch (r.tag) {
                case 5:
                    var o = r.stateNode;
                    r.flags & 32 && (lr(o, ""),
                    r.flags &= -33);
                    var c = hc(e);
                    Ji(e, c, o);
                    break;
                case 3:
                case 4:
                    var p = r.stateNode.containerInfo
                      , y = hc(e);
                    Gi(e, y, p);
                    break;
                default:
                    throw Error(l(161))
                }
            } catch (N) {
                Le(e, e.return, N)
            }
            e.flags &= -3
        }
        t & 4096 && (e.flags &= -4097)
    }
    function fh(e, t, n) {
        W = e,
        yc(e)
    }
    function yc(e, t, n) {
        for (var r = (e.mode & 1) !== 0; W !== null; ) {
            var o = W
              , c = o.child;
            if (o.tag === 22 && r) {
                var p = o.memoizedState !== null || Ws;
                if (!p) {
                    var y = o.alternate
                      , N = y !== null && y.memoizedState !== null || Ye;
                    y = Ws;
                    var L = Ye;
                    if (Ws = p,
                    (Ye = N) && !L)
                        for (W = o; W !== null; )
                            p = W,
                            N = p.child,
                            p.tag === 22 && p.memoizedState !== null ? bc(o) : N !== null ? (N.return = p,
                            W = N) : bc(o);
                    for (; c !== null; )
                        W = c,
                        yc(c),
                        c = c.sibling;
                    W = o,
                    Ws = y,
                    Ye = L
                }
                vc(e)
            } else
                (o.subtreeFlags & 8772) !== 0 && c !== null ? (c.return = o,
                W = c) : vc(e)
        }
    }
    function vc(e) {
        for (; W !== null; ) {
            var t = W;
            if ((t.flags & 8772) !== 0) {
                var n = t.alternate;
                try {
                    if ((t.flags & 8772) !== 0)
                        switch (t.tag) {
                        case 0:
                        case 11:
                        case 15:
                            Ye || qs(5, t);
                            break;
                        case 1:
                            var r = t.stateNode;
                            if (t.flags & 4 && !Ye)
                                if (n === null)
                                    r.componentDidMount();
                                else {
                                    var o = t.elementType === t.type ? n.memoizedProps : vt(t.type, n.memoizedProps);
                                    r.componentDidUpdate(o, n.memoizedState, r.__reactInternalSnapshotBeforeUpdate)
                                }
                            var c = t.updateQueue;
                            c !== null && wu(t, c, r);
                            break;
                        case 3:
                            var p = t.updateQueue;
                            if (p !== null) {
                                if (n = null,
                                t.child !== null)
                                    switch (t.child.tag) {
                                    case 5:
                                        n = t.child.stateNode;
                                        break;
                                    case 1:
                                        n = t.child.stateNode
                                    }
                                wu(t, p, n)
                            }
                            break;
                        case 5:
                            var y = t.stateNode;
                            if (n === null && t.flags & 4) {
                                n = y;
                                var N = t.memoizedProps;
                                switch (t.type) {
                                case "button":
                                case "input":
                                case "select":
                                case "textarea":
                                    N.autoFocus && n.focus();
                                    break;
                                case "img":
                                    N.src && (n.src = N.src)
                                }
                            }
                            break;
                        case 6:
                            break;
                        case 4:
                            break;
                        case 12:
                            break;
                        case 13:
                            if (t.memoizedState === null) {
                                var L = t.alternate;
                                if (L !== null) {
                                    var M = L.memoizedState;
                                    if (M !== null) {
                                        var A = M.dehydrated;
                                        A !== null && gr(A)
                                    }
                                }
                            }
                            break;
                        case 19:
                        case 17:
                        case 21:
                        case 22:
                        case 23:
                        case 25:
                            break;
                        default:
                            throw Error(l(163))
                        }
                    Ye || t.flags & 512 && Qi(t)
                } catch (z) {
                    Le(t, t.return, z)
                }
            }
            if (t === e) {
                W = null;
                break
            }
            if (n = t.sibling,
            n !== null) {
                n.return = t.return,
                W = n;
                break
            }
            W = t.return
        }
    }
    function wc(e) {
        for (; W !== null; ) {
            var t = W;
            if (t === e) {
                W = null;
                break
            }
            var n = t.sibling;
            if (n !== null) {
                n.return = t.return,
                W = n;
                break
            }
            W = t.return
        }
    }
    function bc(e) {
        for (; W !== null; ) {
            var t = W;
            try {
                switch (t.tag) {
                case 0:
                case 11:
                case 15:
                    var n = t.return;
                    try {
                        qs(4, t)
                    } catch (N) {
                        Le(t, n, N)
                    }
                    break;
                case 1:
                    var r = t.stateNode;
                    if (typeof r.componentDidMount == "function") {
                        var o = t.return;
                        try {
                            r.componentDidMount()
                        } catch (N) {
                            Le(t, o, N)
                        }
                    }
                    var c = t.return;
                    try {
                        Qi(t)
                    } catch (N) {
                        Le(t, c, N)
                    }
                    break;
                case 5:
                    var p = t.return;
                    try {
                        Qi(t)
                    } catch (N) {
                        Le(t, p, N)
                    }
                }
            } catch (N) {
                Le(t, t.return, N)
            }
            if (t === e) {
                W = null;
                break
            }
            var y = t.sibling;
            if (y !== null) {
                y.return = t.return,
                W = y;
                break
            }
            W = t.return
        }
    }
    var ph = Math.ceil
      , Ys = H.ReactCurrentDispatcher
      , Xi = H.ReactCurrentOwner
      , pt = H.ReactCurrentBatchConfig
      , de = 0
      , Ie = null
      , Te = null
      , Ve = 0
      , ot = 0
      , Gn = qt(0)
      , Ae = 0
      , Ir = null
      , vn = 0
      , Qs = 0
      , Zi = 0
      , Fr = null
      , tt = null
      , ea = 0
      , Jn = 1 / 0
      , $t = null
      , Gs = !1
      , ta = null
      , Zt = null
      , Js = !1
      , en = null
      , Xs = 0
      , Ur = 0
      , na = null
      , Zs = -1
      , el = 0;
    function Ge() {
        return (de & 6) !== 0 ? _e() : Zs !== -1 ? Zs : Zs = _e()
    }
    function tn(e) {
        return (e.mode & 1) === 0 ? 1 : (de & 2) !== 0 && Ve !== 0 ? Ve & -Ve : Gp.transition !== null ? (el === 0 && (el = ho()),
        el) : (e = xe,
        e !== 0 || (e = window.event,
        e = e === void 0 ? 16 : jo(e.type)),
        e)
    }
    function Nt(e, t, n, r) {
        if (50 < Ur)
            throw Ur = 0,
            na = null,
            Error(l(185));
        dr(e, n, r),
        ((de & 2) === 0 || e !== Ie) && (e === Ie && ((de & 2) === 0 && (Qs |= n),
        Ae === 4 && nn(e, Ve)),
        nt(e, r),
        n === 1 && de === 0 && (t.mode & 1) === 0 && (Jn = _e() + 500,
        Ps && Qt()))
    }
    function nt(e, t) {
        var n = e.callbackNode;
        Gf(e, t);
        var r = us(e, e === Ie ? Ve : 0);
        if (r === 0)
            n !== null && co(n),
            e.callbackNode = null,
            e.callbackPriority = 0;
        else if (t = r & -r,
        e.callbackPriority !== t) {
            if (n != null && co(n),
            t === 1)
                e.tag === 0 ? Qp(jc.bind(null, e)) : ou(jc.bind(null, e)),
                Kp(function() {
                    (de & 6) === 0 && Qt()
                }),
                n = null;
            else {
                switch (mo(r)) {
                case 1:
                    n = Ml;
                    break;
                case 4:
                    n = fo;
                    break;
                case 16:
                    n = ls;
                    break;
                case 536870912:
                    n = po;
                    break;
                default:
                    n = ls
                }
                n = Rc(n, Nc.bind(null, e))
            }
            e.callbackPriority = t,
            e.callbackNode = n
        }
    }
    function Nc(e, t) {
        if (Zs = -1,
        el = 0,
        (de & 6) !== 0)
            throw Error(l(327));
        var n = e.callbackNode;
        if (Xn() && e.callbackNode !== n)
            return null;
        var r = us(e, e === Ie ? Ve : 0);
        if (r === 0)
            return null;
        if ((r & 30) !== 0 || (r & e.expiredLanes) !== 0 || t)
            t = tl(e, r);
        else {
            t = r;
            var o = de;
            de |= 2;
            var c = Sc();
            (Ie !== e || Ve !== t) && ($t = null,
            Jn = _e() + 500,
            bn(e, t));
            do
                try {
                    gh();
                    break
                } catch (y) {
                    kc(e, y)
                }
            while (!0);
            wi(),
            Ys.current = c,
            de = o,
            Te !== null ? t = 0 : (Ie = null,
            Ve = 0,
            t = Ae)
        }
        if (t !== 0) {
            if (t === 2 && (o = Al(e),
            o !== 0 && (r = o,
            t = ra(e, o))),
            t === 1)
                throw n = Ir,
                bn(e, 0),
                nn(e, r),
                nt(e, _e()),
                n;
            if (t === 6)
                nn(e, r);
            else {
                if (o = e.current.alternate,
                (r & 30) === 0 && !hh(o) && (t = tl(e, r),
                t === 2 && (c = Al(e),
                c !== 0 && (r = c,
                t = ra(e, c))),
                t === 1))
                    throw n = Ir,
                    bn(e, 0),
                    nn(e, r),
                    nt(e, _e()),
                    n;
                switch (e.finishedWork = o,
                e.finishedLanes = r,
                t) {
                case 0:
                case 1:
                    throw Error(l(345));
                case 2:
                    Nn(e, tt, $t);
                    break;
                case 3:
                    if (nn(e, r),
                    (r & 130023424) === r && (t = ea + 500 - _e(),
                    10 < t)) {
                        if (us(e, 0) !== 0)
                            break;
                        if (o = e.suspendedLanes,
                        (o & r) !== r) {
                            Ge(),
                            e.pingedLanes |= e.suspendedLanes & o;
                            break
                        }
                        e.timeoutHandle = ui(Nn.bind(null, e, tt, $t), t);
                        break
                    }
                    Nn(e, tt, $t);
                    break;
                case 4:
                    if (nn(e, r),
                    (r & 4194240) === r)
                        break;
                    for (t = e.eventTimes,
                    o = -1; 0 < r; ) {
                        var p = 31 - gt(r);
                        c = 1 << p,
                        p = t[p],
                        p > o && (o = p),
                        r &= ~c
                    }
                    if (r = o,
                    r = _e() - r,
                    r = (120 > r ? 120 : 480 > r ? 480 : 1080 > r ? 1080 : 1920 > r ? 1920 : 3e3 > r ? 3e3 : 4320 > r ? 4320 : 1960 * ph(r / 1960)) - r,
                    10 < r) {
                        e.timeoutHandle = ui(Nn.bind(null, e, tt, $t), r);
                        break
                    }
                    Nn(e, tt, $t);
                    break;
                case 5:
                    Nn(e, tt, $t);
                    break;
                default:
                    throw Error(l(329))
                }
            }
        }
        return nt(e, _e()),
        e.callbackNode === n ? Nc.bind(null, e) : null
    }
    function ra(e, t) {
        var n = Fr;
        return e.current.memoizedState.isDehydrated && (bn(e, t).flags |= 256),
        e = tl(e, t),
        e !== 2 && (t = tt,
        tt = n,
        t !== null && sa(t)),
        e
    }
    function sa(e) {
        tt === null ? tt = e : tt.push.apply(tt, e)
    }
    function hh(e) {
        for (var t = e; ; ) {
            if (t.flags & 16384) {
                var n = t.updateQueue;
                if (n !== null && (n = n.stores,
                n !== null))
                    for (var r = 0; r < n.length; r++) {
                        var o = n[r]
                          , c = o.getSnapshot;
                        o = o.value;
                        try {
                            if (!xt(c(), o))
                                return !1
                        } catch {
                            return !1
                        }
                    }
            }
            if (n = t.child,
            t.subtreeFlags & 16384 && n !== null)
                n.return = t,
                t = n;
            else {
                if (t === e)
                    break;
                for (; t.sibling === null; ) {
                    if (t.return === null || t.return === e)
                        return !0;
                    t = t.return
                }
                t.sibling.return = t.return,
                t = t.sibling
            }
        }
        return !0
    }
    function nn(e, t) {
        for (t &= ~Zi,
        t &= ~Qs,
        e.suspendedLanes |= t,
        e.pingedLanes &= ~t,
        e = e.expirationTimes; 0 < t; ) {
            var n = 31 - gt(t)
              , r = 1 << n;
            e[n] = -1,
            t &= ~r
        }
    }
    function jc(e) {
        if ((de & 6) !== 0)
            throw Error(l(327));
        Xn();
        var t = us(e, 0);
        if ((t & 1) === 0)
            return nt(e, _e()),
            null;
        var n = tl(e, t);
        if (e.tag !== 0 && n === 2) {
            var r = Al(e);
            r !== 0 && (t = r,
            n = ra(e, r))
        }
        if (n === 1)
            throw n = Ir,
            bn(e, 0),
            nn(e, t),
            nt(e, _e()),
            n;
        if (n === 6)
            throw Error(l(345));
        return e.finishedWork = e.current.alternate,
        e.finishedLanes = t,
        Nn(e, tt, $t),
        nt(e, _e()),
        null
    }
    function la(e, t) {
        var n = de;
        de |= 1;
        try {
            return e(t)
        } finally {
            de = n,
            de === 0 && (Jn = _e() + 500,
            Ps && Qt())
        }
    }
    function wn(e) {
        en !== null && en.tag === 0 && (de & 6) === 0 && Xn();
        var t = de;
        de |= 1;
        var n = pt.transition
          , r = xe;
        try {
            if (pt.transition = null,
            xe = 1,
            e)
                return e()
        } finally {
            xe = r,
            pt.transition = n,
            de = t,
            (de & 6) === 0 && Qt()
        }
    }
    function ia() {
        ot = Gn.current,
        Ne(Gn)
    }
    function bn(e, t) {
        e.finishedWork = null,
        e.finishedLanes = 0;
        var n = e.timeoutHandle;
        if (n !== -1 && (e.timeoutHandle = -1,
        Hp(n)),
        Te !== null)
            for (n = Te.return; n !== null; ) {
                var r = n;
                switch (mi(r),
                r.tag) {
                case 1:
                    r = r.type.childContextTypes,
                    r != null && Cs();
                    break;
                case 3:
                    qn(),
                    Ne(Xe),
                    Ne(Ke),
                    Pi();
                    break;
                case 5:
                    Ci(r);
                    break;
                case 4:
                    qn();
                    break;
                case 13:
                    Ne(Ce);
                    break;
                case 19:
                    Ne(Ce);
                    break;
                case 10:
                    bi(r.type._context);
                    break;
                case 22:
                case 23:
                    ia()
                }
                n = n.return
            }
        if (Ie = e,
        Te = e = rn(e.current, null),
        Ve = ot = t,
        Ae = 0,
        Ir = null,
        Zi = Qs = vn = 0,
        tt = Fr = null,
        gn !== null) {
            for (t = 0; t < gn.length; t++)
                if (n = gn[t],
                r = n.interleaved,
                r !== null) {
                    n.interleaved = null;
                    var o = r.next
                      , c = n.pending;
                    if (c !== null) {
                        var p = c.next;
                        c.next = o,
                        r.next = p
                    }
                    n.pending = r
                }
            gn = null
        }
        return e
    }
    function kc(e, t) {
        do {
            var n = Te;
            try {
                if (wi(),
                $s.current = Bs,
                Is) {
                    for (var r = Ee.memoizedState; r !== null; ) {
                        var o = r.queue;
                        o !== null && (o.pending = null),
                        r = r.next
                    }
                    Is = !1
                }
                if (yn = 0,
                $e = Me = Ee = null,
                Tr = !1,
                zr = 0,
                Xi.current = null,
                n === null || n.return === null) {
                    Ae = 1,
                    Ir = t,
                    Te = null;
                    break
                }
                e: {
                    var c = e
                      , p = n.return
                      , y = n
                      , N = t;
                    if (t = Ve,
                    y.flags |= 32768,
                    N !== null && typeof N == "object" && typeof N.then == "function") {
                        var L = N
                          , M = y
                          , A = M.tag;
                        if ((M.mode & 1) === 0 && (A === 0 || A === 11 || A === 15)) {
                            var z = M.alternate;
                            z ? (M.updateQueue = z.updateQueue,
                            M.memoizedState = z.memoizedState,
                            M.lanes = z.lanes) : (M.updateQueue = null,
                            M.memoizedState = null)
                        }
                        var B = Qu(p);
                        if (B !== null) {
                            B.flags &= -257,
                            Gu(B, p, y, c, t),
                            B.mode & 1 && Yu(c, L, t),
                            t = B,
                            N = L;
                            var q = t.updateQueue;
                            if (q === null) {
                                var Q = new Set;
                                Q.add(N),
                                t.updateQueue = Q
                            } else
                                q.add(N);
                            break e
                        } else {
                            if ((t & 1) === 0) {
                                Yu(c, L, t),
                                aa();
                                break e
                            }
                            N = Error(l(426))
                        }
                    } else if (Se && y.mode & 1) {
                        var Re = Qu(p);
                        if (Re !== null) {
                            (Re.flags & 65536) === 0 && (Re.flags |= 256),
                            Gu(Re, p, y, c, t),
                            yi(Yn(N, y));
                            break e
                        }
                    }
                    c = N = Yn(N, y),
                    Ae !== 4 && (Ae = 2),
                    Fr === null ? Fr = [c] : Fr.push(c),
                    c = p;
                    do {
                        switch (c.tag) {
                        case 3:
                            c.flags |= 65536,
                            t &= -t,
                            c.lanes |= t;
                            var S = Wu(c, N, t);
                            vu(c, S);
                            break e;
                        case 1:
                            y = N;
                            var j = c.type
                              , C = c.stateNode;
                            if ((c.flags & 128) === 0 && (typeof j.getDerivedStateFromError == "function" || C !== null && typeof C.componentDidCatch == "function" && (Zt === null || !Zt.has(C)))) {
                                c.flags |= 65536,
                                t &= -t,
                                c.lanes |= t;
                                var D = qu(c, y, t);
                                vu(c, D);
                                break e
                            }
                        }
                        c = c.return
                    } while (c !== null)
                }
                Ec(n)
            } catch (G) {
                t = G,
                Te === n && n !== null && (Te = n = n.return);
                continue
            }
            break
        } while (!0)
    }
    function Sc() {
        var e = Ys.current;
        return Ys.current = Bs,
        e === null ? Bs : e
    }
    function aa() {
        (Ae === 0 || Ae === 3 || Ae === 2) && (Ae = 4),
        Ie === null || (vn & 268435455) === 0 && (Qs & 268435455) === 0 || nn(Ie, Ve)
    }
    function tl(e, t) {
        var n = de;
        de |= 2;
        var r = Sc();
        (Ie !== e || Ve !== t) && ($t = null,
        bn(e, t));
        do
            try {
                mh();
                break
            } catch (o) {
                kc(e, o)
            }
        while (!0);
        if (wi(),
        de = n,
        Ys.current = r,
        Te !== null)
            throw Error(l(261));
        return Ie = null,
        Ve = 0,
        Ae
    }
    function mh() {
        for (; Te !== null; )
            Cc(Te)
    }
    function gh() {
        for (; Te !== null && !Uf(); )
            Cc(Te)
    }
    function Cc(e) {
        var t = _c(e.alternate, e, ot);
        e.memoizedProps = e.pendingProps,
        t === null ? Ec(e) : Te = t,
        Xi.current = null
    }
    function Ec(e) {
        var t = e;
        do {
            var n = t.alternate;
            if (e = t.return,
            (t.flags & 32768) === 0) {
                if (n = oh(n, t, ot),
                n !== null) {
                    Te = n;
                    return
                }
            } else {
                if (n = uh(n, t),
                n !== null) {
                    n.flags &= 32767,
                    Te = n;
                    return
                }
                if (e !== null)
                    e.flags |= 32768,
                    e.subtreeFlags = 0,
                    e.deletions = null;
                else {
                    Ae = 6,
                    Te = null;
                    return
                }
            }
            if (t = t.sibling,
            t !== null) {
                Te = t;
                return
            }
            Te = t = e
        } while (t !== null);
        Ae === 0 && (Ae = 5)
    }
    function Nn(e, t, n) {
        var r = xe
          , o = pt.transition;
        try {
            pt.transition = null,
            xe = 1,
            xh(e, t, n, r)
        } finally {
            pt.transition = o,
            xe = r
        }
        return null
    }
    function xh(e, t, n, r) {
        do
            Xn();
        while (en !== null);
        if ((de & 6) !== 0)
            throw Error(l(327));
        n = e.finishedWork;
        var o = e.finishedLanes;
        if (n === null)
            return null;
        if (e.finishedWork = null,
        e.finishedLanes = 0,
        n === e.current)
            throw Error(l(177));
        e.callbackNode = null,
        e.callbackPriority = 0;
        var c = n.lanes | n.childLanes;
        if (Jf(e, c),
        e === Ie && (Te = Ie = null,
        Ve = 0),
        (n.subtreeFlags & 2064) === 0 && (n.flags & 2064) === 0 || Js || (Js = !0,
        Rc(ls, function() {
            return Xn(),
            null
        })),
        c = (n.flags & 15990) !== 0,
        (n.subtreeFlags & 15990) !== 0 || c) {
            c = pt.transition,
            pt.transition = null;
            var p = xe;
            xe = 1;
            var y = de;
            de |= 4,
            Xi.current = null,
            dh(e, n),
            xc(n, e),
            Dp(ai),
            fs = !!ii,
            ai = ii = null,
            e.current = n,
            fh(n),
            Bf(),
            de = y,
            xe = p,
            pt.transition = c
        } else
            e.current = n;
        if (Js && (Js = !1,
        en = e,
        Xs = o),
        c = e.pendingLanes,
        c === 0 && (Zt = null),
        Kf(n.stateNode),
        nt(e, _e()),
        t !== null)
            for (r = e.onRecoverableError,
            n = 0; n < t.length; n++)
                o = t[n],
                r(o.value, {
                    componentStack: o.stack,
                    digest: o.digest
                });
        if (Gs)
            throw Gs = !1,
            e = ta,
            ta = null,
            e;
        return (Xs & 1) !== 0 && e.tag !== 0 && Xn(),
        c = e.pendingLanes,
        (c & 1) !== 0 ? e === na ? Ur++ : (Ur = 0,
        na = e) : Ur = 0,
        Qt(),
        null
    }
    function Xn() {
        if (en !== null) {
            var e = mo(Xs)
              , t = pt.transition
              , n = xe;
            try {
                if (pt.transition = null,
                xe = 16 > e ? 16 : e,
                en === null)
                    var r = !1;
                else {
                    if (e = en,
                    en = null,
                    Xs = 0,
                    (de & 6) !== 0)
                        throw Error(l(331));
                    var o = de;
                    for (de |= 4,
                    W = e.current; W !== null; ) {
                        var c = W
                          , p = c.child;
                        if ((W.flags & 16) !== 0) {
                            var y = c.deletions;
                            if (y !== null) {
                                for (var N = 0; N < y.length; N++) {
                                    var L = y[N];
                                    for (W = L; W !== null; ) {
                                        var M = W;
                                        switch (M.tag) {
                                        case 0:
                                        case 11:
                                        case 15:
                                            $r(8, M, c)
                                        }
                                        var A = M.child;
                                        if (A !== null)
                                            A.return = M,
                                            W = A;
                                        else
                                            for (; W !== null; ) {
                                                M = W;
                                                var z = M.sibling
                                                  , B = M.return;
                                                if (fc(M),
                                                M === L) {
                                                    W = null;
                                                    break
                                                }
                                                if (z !== null) {
                                                    z.return = B,
                                                    W = z;
                                                    break
                                                }
                                                W = B
                                            }
                                    }
                                }
                                var q = c.alternate;
                                if (q !== null) {
                                    var Q = q.child;
                                    if (Q !== null) {
                                        q.child = null;
                                        do {
                                            var Re = Q.sibling;
                                            Q.sibling = null,
                                            Q = Re
                                        } while (Q !== null)
                                    }
                                }
                                W = c
                            }
                        }
                        if ((c.subtreeFlags & 2064) !== 0 && p !== null)
                            p.return = c,
                            W = p;
                        else
                            e: for (; W !== null; ) {
                                if (c = W,
                                (c.flags & 2048) !== 0)
                                    switch (c.tag) {
                                    case 0:
                                    case 11:
                                    case 15:
                                        $r(9, c, c.return)
                                    }
                                var S = c.sibling;
                                if (S !== null) {
                                    S.return = c.return,
                                    W = S;
                                    break e
                                }
                                W = c.return
                            }
                    }
                    var j = e.current;
                    for (W = j; W !== null; ) {
                        p = W;
                        var C = p.child;
                        if ((p.subtreeFlags & 2064) !== 0 && C !== null)
                            C.return = p,
                            W = C;
                        else
                            e: for (p = j; W !== null; ) {
                                if (y = W,
                                (y.flags & 2048) !== 0)
                                    try {
                                        switch (y.tag) {
                                        case 0:
                                        case 11:
                                        case 15:
                                            qs(9, y)
                                        }
                                    } catch (G) {
                                        Le(y, y.return, G)
                                    }
                                if (y === p) {
                                    W = null;
                                    break e
                                }
                                var D = y.sibling;
                                if (D !== null) {
                                    D.return = y.return,
                                    W = D;
                                    break e
                                }
                                W = y.return
                            }
                    }
                    if (de = o,
                    Qt(),
                    jt && typeof jt.onPostCommitFiberRoot == "function")
                        try {
                            jt.onPostCommitFiberRoot(is, e)
                        } catch {}
                    r = !0
                }
                return r
            } finally {
                xe = n,
                pt.transition = t
            }
        }
        return !1
    }
    function Pc(e, t, n) {
        t = Yn(n, t),
        t = Wu(e, t, 1),
        e = Jt(e, t, 1),
        t = Ge(),
        e !== null && (dr(e, 1, t),
        nt(e, t))
    }
    function Le(e, t, n) {
        if (e.tag === 3)
            Pc(e, e, n);
        else
            for (; t !== null; ) {
                if (t.tag === 3) {
                    Pc(t, e, n);
                    break
                } else if (t.tag === 1) {
                    var r = t.stateNode;
                    if (typeof t.type.getDerivedStateFromError == "function" || typeof r.componentDidCatch == "function" && (Zt === null || !Zt.has(r))) {
                        e = Yn(n, e),
                        e = qu(t, e, 1),
                        t = Jt(t, e, 1),
                        e = Ge(),
                        t !== null && (dr(t, 1, e),
                        nt(t, e));
                        break
                    }
                }
                t = t.return
            }
    }
    function yh(e, t, n) {
        var r = e.pingCache;
        r !== null && r.delete(t),
        t = Ge(),
        e.pingedLanes |= e.suspendedLanes & n,
        Ie === e && (Ve & n) === n && (Ae === 4 || Ae === 3 && (Ve & 130023424) === Ve && 500 > _e() - ea ? bn(e, 0) : Zi |= n),
        nt(e, t)
    }
    function Lc(e, t) {
        t === 0 && ((e.mode & 1) === 0 ? t = 1 : (t = os,
        os <<= 1,
        (os & 130023424) === 0 && (os = 4194304)));
        var n = Ge();
        e = Mt(e, t),
        e !== null && (dr(e, t, n),
        nt(e, n))
    }
    function vh(e) {
        var t = e.memoizedState
          , n = 0;
        t !== null && (n = t.retryLane),
        Lc(e, n)
    }
    function wh(e, t) {
        var n = 0;
        switch (e.tag) {
        case 13:
            var r = e.stateNode
              , o = e.memoizedState;
            o !== null && (n = o.retryLane);
            break;
        case 19:
            r = e.stateNode;
            break;
        default:
            throw Error(l(314))
        }
        r !== null && r.delete(t),
        Lc(e, n)
    }
    var _c;
    _c = function(e, t, n) {
        if (e !== null)
            if (e.memoizedProps !== t.pendingProps || Xe.current)
                et = !0;
            else {
                if ((e.lanes & n) === 0 && (t.flags & 128) === 0)
                    return et = !1,
                    ah(e, t, n);
                et = (e.flags & 131072) !== 0
            }
        else
            et = !1,
            Se && (t.flags & 1048576) !== 0 && uu(t, _s, t.index);
        switch (t.lanes = 0,
        t.tag) {
        case 2:
            var r = t.type;
            Ks(e, t),
            e = t.pendingProps;
            var o = Fn(t, Ke.current);
            Wn(t, n),
            o = Ri(null, t, r, e, o, n);
            var c = Oi();
            return t.flags |= 1,
            typeof o == "object" && o !== null && typeof o.render == "function" && o.$$typeof === void 0 ? (t.tag = 1,
            t.memoizedState = null,
            t.updateQueue = null,
            Ze(r) ? (c = !0,
            Es(t)) : c = !1,
            t.memoizedState = o.state !== null && o.state !== void 0 ? o.state : null,
            ki(t),
            o.updater = Vs,
            t.stateNode = o,
            o._reactInternals = t,
            $i(t, r, e, n),
            t = Bi(null, t, r, !0, c, n)) : (t.tag = 0,
            Se && c && hi(t),
            Qe(null, t, o, n),
            t = t.child),
            t;
        case 16:
            r = t.elementType;
            e: {
                switch (Ks(e, t),
                e = t.pendingProps,
                o = r._init,
                r = o(r._payload),
                t.type = r,
                o = t.tag = Nh(r),
                e = vt(r, e),
                o) {
                case 0:
                    t = Ui(null, t, r, e, n);
                    break e;
                case 1:
                    t = nc(null, t, r, e, n);
                    break e;
                case 11:
                    t = Ju(null, t, r, e, n);
                    break e;
                case 14:
                    t = Xu(null, t, r, vt(r.type, e), n);
                    break e
                }
                throw Error(l(306, r, ""))
            }
            return t;
        case 0:
            return r = t.type,
            o = t.pendingProps,
            o = t.elementType === r ? o : vt(r, o),
            Ui(e, t, r, o, n);
        case 1:
            return r = t.type,
            o = t.pendingProps,
            o = t.elementType === r ? o : vt(r, o),
            nc(e, t, r, o, n);
        case 3:
            e: {
                if (rc(t),
                e === null)
                    throw Error(l(387));
                r = t.pendingProps,
                c = t.memoizedState,
                o = c.element,
                yu(e, t),
                As(t, r, null, n);
                var p = t.memoizedState;
                if (r = p.element,
                c.isDehydrated)
                    if (c = {
                        element: r,
                        isDehydrated: !1,
                        cache: p.cache,
                        pendingSuspenseBoundaries: p.pendingSuspenseBoundaries,
                        transitions: p.transitions
                    },
                    t.updateQueue.baseState = c,
                    t.memoizedState = c,
                    t.flags & 256) {
                        o = Yn(Error(l(423)), t),
                        t = sc(e, t, r, n, o);
                        break e
                    } else if (r !== o) {
                        o = Yn(Error(l(424)), t),
                        t = sc(e, t, r, n, o);
                        break e
                    } else
                        for (at = Wt(t.stateNode.containerInfo.firstChild),
                        it = t,
                        Se = !0,
                        yt = null,
                        n = gu(t, null, r, n),
                        t.child = n; n; )
                            n.flags = n.flags & -3 | 4096,
                            n = n.sibling;
                else {
                    if (Vn(),
                    r === o) {
                        t = Dt(e, t, n);
                        break e
                    }
                    Qe(e, t, r, n)
                }
                t = t.child
            }
            return t;
        case 5:
            return bu(t),
            e === null && xi(t),
            r = t.type,
            o = t.pendingProps,
            c = e !== null ? e.memoizedProps : null,
            p = o.children,
            oi(r, o) ? p = null : c !== null && oi(r, c) && (t.flags |= 32),
            tc(e, t),
            Qe(e, t, p, n),
            t.child;
        case 6:
            return e === null && xi(t),
            null;
        case 13:
            return lc(e, t, n);
        case 4:
            return Si(t, t.stateNode.containerInfo),
            r = t.pendingProps,
            e === null ? t.child = Hn(t, null, r, n) : Qe(e, t, r, n),
            t.child;
        case 11:
            return r = t.type,
            o = t.pendingProps,
            o = t.elementType === r ? o : vt(r, o),
            Ju(e, t, r, o, n);
        case 7:
            return Qe(e, t, t.pendingProps, n),
            t.child;
        case 8:
            return Qe(e, t, t.pendingProps.children, n),
            t.child;
        case 12:
            return Qe(e, t, t.pendingProps.children, n),
            t.child;
        case 10:
            e: {
                if (r = t.type._context,
                o = t.pendingProps,
                c = t.memoizedProps,
                p = o.value,
                we(Ts, r._currentValue),
                r._currentValue = p,
                c !== null)
                    if (xt(c.value, p)) {
                        if (c.children === o.children && !Xe.current) {
                            t = Dt(e, t, n);
                            break e
                        }
                    } else
                        for (c = t.child,
                        c !== null && (c.return = t); c !== null; ) {
                            var y = c.dependencies;
                            if (y !== null) {
                                p = c.child;
                                for (var N = y.firstContext; N !== null; ) {
                                    if (N.context === r) {
                                        if (c.tag === 1) {
                                            N = At(-1, n & -n),
                                            N.tag = 2;
                                            var L = c.updateQueue;
                                            if (L !== null) {
                                                L = L.shared;
                                                var M = L.pending;
                                                M === null ? N.next = N : (N.next = M.next,
                                                M.next = N),
                                                L.pending = N
                                            }
                                        }
                                        c.lanes |= n,
                                        N = c.alternate,
                                        N !== null && (N.lanes |= n),
                                        Ni(c.return, n, t),
                                        y.lanes |= n;
                                        break
                                    }
                                    N = N.next
                                }
                            } else if (c.tag === 10)
                                p = c.type === t.type ? null : c.child;
                            else if (c.tag === 18) {
                                if (p = c.return,
                                p === null)
                                    throw Error(l(341));
                                p.lanes |= n,
                                y = p.alternate,
                                y !== null && (y.lanes |= n),
                                Ni(p, n, t),
                                p = c.sibling
                            } else
                                p = c.child;
                            if (p !== null)
                                p.return = c;
                            else
                                for (p = c; p !== null; ) {
                                    if (p === t) {
                                        p = null;
                                        break
                                    }
                                    if (c = p.sibling,
                                    c !== null) {
                                        c.return = p.return,
                                        p = c;
                                        break
                                    }
                                    p = p.return
                                }
                            c = p
                        }
                Qe(e, t, o.children, n),
                t = t.child
            }
            return t;
        case 9:
            return o = t.type,
            r = t.pendingProps.children,
            Wn(t, n),
            o = dt(o),
            r = r(o),
            t.flags |= 1,
            Qe(e, t, r, n),
            t.child;
        case 14:
            return r = t.type,
            o = vt(r, t.pendingProps),
            o = vt(r.type, o),
            Xu(e, t, r, o, n);
        case 15:
            return Zu(e, t, t.type, t.pendingProps, n);
        case 17:
            return r = t.type,
            o = t.pendingProps,
            o = t.elementType === r ? o : vt(r, o),
            Ks(e, t),
            t.tag = 1,
            Ze(r) ? (e = !0,
            Es(t)) : e = !1,
            Wn(t, n),
            Hu(t, r, o),
            $i(t, r, o, n),
            Bi(null, t, r, !0, e, n);
        case 19:
            return ac(e, t, n);
        case 22:
            return ec(e, t, n)
        }
        throw Error(l(156, t.tag))
    }
    ;
    function Rc(e, t) {
        return uo(e, t)
    }
    function bh(e, t, n, r) {
        this.tag = e,
        this.key = n,
        this.sibling = this.child = this.return = this.stateNode = this.type = this.elementType = null,
        this.index = 0,
        this.ref = null,
        this.pendingProps = t,
        this.dependencies = this.memoizedState = this.updateQueue = this.memoizedProps = null,
        this.mode = r,
        this.subtreeFlags = this.flags = 0,
        this.deletions = null,
        this.childLanes = this.lanes = 0,
        this.alternate = null
    }
    function ht(e, t, n, r) {
        return new bh(e,t,n,r)
    }
    function oa(e) {
        return e = e.prototype,
        !(!e || !e.isReactComponent)
    }
    function Nh(e) {
        if (typeof e == "function")
            return oa(e) ? 1 : 0;
        if (e != null) {
            if (e = e.$$typeof,
            e === me)
                return 11;
            if (e === Pe)
                return 14
        }
        return 2
    }
    function rn(e, t) {
        var n = e.alternate;
        return n === null ? (n = ht(e.tag, t, e.key, e.mode),
        n.elementType = e.elementType,
        n.type = e.type,
        n.stateNode = e.stateNode,
        n.alternate = e,
        e.alternate = n) : (n.pendingProps = t,
        n.type = e.type,
        n.flags = 0,
        n.subtreeFlags = 0,
        n.deletions = null),
        n.flags = e.flags & 14680064,
        n.childLanes = e.childLanes,
        n.lanes = e.lanes,
        n.child = e.child,
        n.memoizedProps = e.memoizedProps,
        n.memoizedState = e.memoizedState,
        n.updateQueue = e.updateQueue,
        t = e.dependencies,
        n.dependencies = t === null ? null : {
            lanes: t.lanes,
            firstContext: t.firstContext
        },
        n.sibling = e.sibling,
        n.index = e.index,
        n.ref = e.ref,
        n
    }
    function nl(e, t, n, r, o, c) {
        var p = 2;
        if (r = e,
        typeof e == "function")
            oa(e) && (p = 1);
        else if (typeof e == "string")
            p = 5;
        else
            e: switch (e) {
            case te:
                return jn(n.children, o, c, t);
            case ee:
                p = 8,
                o |= 8;
                break;
            case J:
                return e = ht(12, n, t, o | 2),
                e.elementType = J,
                e.lanes = c,
                e;
            case De:
                return e = ht(13, n, t, o),
                e.elementType = De,
                e.lanes = c,
                e;
            case je:
                return e = ht(19, n, t, o),
                e.elementType = je,
                e.lanes = c,
                e;
            case ye:
                return rl(n, o, c, t);
            default:
                if (typeof e == "object" && e !== null)
                    switch (e.$$typeof) {
                    case ue:
                        p = 10;
                        break e;
                    case ce:
                        p = 9;
                        break e;
                    case me:
                        p = 11;
                        break e;
                    case Pe:
                        p = 14;
                        break e;
                    case Oe:
                        p = 16,
                        r = null;
                        break e
                    }
                throw Error(l(130, e == null ? e : typeof e, ""))
            }
        return t = ht(p, n, t, o),
        t.elementType = e,
        t.type = r,
        t.lanes = c,
        t
    }
    function jn(e, t, n, r) {
        return e = ht(7, e, r, t),
        e.lanes = n,
        e
    }
    function rl(e, t, n, r) {
        return e = ht(22, e, r, t),
        e.elementType = ye,
        e.lanes = n,
        e.stateNode = {
            isHidden: !1
        },
        e
    }
    function ua(e, t, n) {
        return e = ht(6, e, null, t),
        e.lanes = n,
        e
    }
    function ca(e, t, n) {
        return t = ht(4, e.children !== null ? e.children : [], e.key, t),
        t.lanes = n,
        t.stateNode = {
            containerInfo: e.containerInfo,
            pendingChildren: null,
            implementation: e.implementation
        },
        t
    }
    function jh(e, t, n, r, o) {
        this.tag = t,
        this.containerInfo = e,
        this.finishedWork = this.pingCache = this.current = this.pendingChildren = null,
        this.timeoutHandle = -1,
        this.callbackNode = this.pendingContext = this.context = null,
        this.callbackPriority = 0,
        this.eventTimes = Dl(0),
        this.expirationTimes = Dl(-1),
        this.entangledLanes = this.finishedLanes = this.mutableReadLanes = this.expiredLanes = this.pingedLanes = this.suspendedLanes = this.pendingLanes = 0,
        this.entanglements = Dl(0),
        this.identifierPrefix = r,
        this.onRecoverableError = o,
        this.mutableSourceEagerHydrationData = null
    }
    function da(e, t, n, r, o, c, p, y, N) {
        return e = new jh(e,t,n,y,N),
        t === 1 ? (t = 1,
        c === !0 && (t |= 8)) : t = 0,
        c = ht(3, null, null, t),
        e.current = c,
        c.stateNode = e,
        c.memoizedState = {
            element: r,
            isDehydrated: n,
            cache: null,
            transitions: null,
            pendingSuspenseBoundaries: null
        },
        ki(c),
        e
    }
    function kh(e, t, n) {
        var r = 3 < arguments.length && arguments[3] !== void 0 ? arguments[3] : null;
        return {
            $$typeof: K,
            key: r == null ? null : "" + r,
            children: e,
            containerInfo: t,
            implementation: n
        }
    }
    function Oc(e) {
        if (!e)
            return Yt;
        e = e._reactInternals;
        e: {
            if (dn(e) !== e || e.tag !== 1)
                throw Error(l(170));
            var t = e;
            do {
                switch (t.tag) {
                case 3:
                    t = t.stateNode.context;
                    break e;
                case 1:
                    if (Ze(t.type)) {
                        t = t.stateNode.__reactInternalMemoizedMergedChildContext;
                        break e
                    }
                }
                t = t.return
            } while (t !== null);
            throw Error(l(171))
        }
        if (e.tag === 1) {
            var n = e.type;
            if (Ze(n))
                return iu(e, n, t)
        }
        return t
    }
    function Tc(e, t, n, r, o, c, p, y, N) {
        return e = da(n, r, !0, e, o, c, p, y, N),
        e.context = Oc(null),
        n = e.current,
        r = Ge(),
        o = tn(n),
        c = At(r, o),
        c.callback = t ?? null,
        Jt(n, c, o),
        e.current.lanes = o,
        dr(e, o, r),
        nt(e, r),
        e
    }
    function sl(e, t, n, r) {
        var o = t.current
          , c = Ge()
          , p = tn(o);
        return n = Oc(n),
        t.context === null ? t.context = n : t.pendingContext = n,
        t = At(c, p),
        t.payload = {
            element: e
        },
        r = r === void 0 ? null : r,
        r !== null && (t.callback = r),
        e = Jt(o, t, p),
        e !== null && (Nt(e, o, p, c),
        Ms(e, o, p)),
        p
    }
    function ll(e) {
        if (e = e.current,
        !e.child)
            return null;
        switch (e.child.tag) {
        case 5:
            return e.child.stateNode;
        default:
            return e.child.stateNode
        }
    }
    function zc(e, t) {
        if (e = e.memoizedState,
        e !== null && e.dehydrated !== null) {
            var n = e.retryLane;
            e.retryLane = n !== 0 && n < t ? n : t
        }
    }
    function fa(e, t) {
        zc(e, t),
        (e = e.alternate) && zc(e, t)
    }
    function Sh() {
        return null
    }
    var Mc = typeof reportError == "function" ? reportError : function(e) {
        console.error(e)
    }
    ;
    function pa(e) {
        this._internalRoot = e
    }
    il.prototype.render = pa.prototype.render = function(e) {
        var t = this._internalRoot;
        if (t === null)
            throw Error(l(409));
        sl(e, t, null, null)
    }
    ,
    il.prototype.unmount = pa.prototype.unmount = function() {
        var e = this._internalRoot;
        if (e !== null) {
            this._internalRoot = null;
            var t = e.containerInfo;
            wn(function() {
                sl(null, e, null, null)
            }),
            t[Rt] = null
        }
    }
    ;
    function il(e) {
        this._internalRoot = e
    }
    il.prototype.unstable_scheduleHydration = function(e) {
        if (e) {
            var t = yo();
            e = {
                blockedOn: null,
                target: e,
                priority: t
            };
            for (var n = 0; n < Vt.length && t !== 0 && t < Vt[n].priority; n++)
                ;
            Vt.splice(n, 0, e),
            n === 0 && bo(e)
        }
    }
    ;
    function ha(e) {
        return !(!e || e.nodeType !== 1 && e.nodeType !== 9 && e.nodeType !== 11)
    }
    function al(e) {
        return !(!e || e.nodeType !== 1 && e.nodeType !== 9 && e.nodeType !== 11 && (e.nodeType !== 8 || e.nodeValue !== " react-mount-point-unstable "))
    }
    function Ac() {}
    function Ch(e, t, n, r, o) {
        if (o) {
            if (typeof r == "function") {
                var c = r;
                r = function() {
                    var L = ll(p);
                    c.call(L)
                }
            }
            var p = Tc(t, r, e, 0, null, !1, !1, "", Ac);
            return e._reactRootContainer = p,
            e[Rt] = p.current,
            Sr(e.nodeType === 8 ? e.parentNode : e),
            wn(),
            p
        }
        for (; o = e.lastChild; )
            e.removeChild(o);
        if (typeof r == "function") {
            var y = r;
            r = function() {
                var L = ll(N);
                y.call(L)
            }
        }
        var N = da(e, 0, !1, null, null, !1, !1, "", Ac);
        return e._reactRootContainer = N,
        e[Rt] = N.current,
        Sr(e.nodeType === 8 ? e.parentNode : e),
        wn(function() {
            sl(t, N, n, r)
        }),
        N
    }
    function ol(e, t, n, r, o) {
        var c = n._reactRootContainer;
        if (c) {
            var p = c;
            if (typeof o == "function") {
                var y = o;
                o = function() {
                    var N = ll(p);
                    y.call(N)
                }
            }
            sl(t, p, e, o)
        } else
            p = Ch(n, t, e, o, r);
        return ll(p)
    }
    go = function(e) {
        switch (e.tag) {
        case 3:
            var t = e.stateNode;
            if (t.current.memoizedState.isDehydrated) {
                var n = cr(t.pendingLanes);
                n !== 0 && ($l(t, n | 1),
                nt(t, _e()),
                (de & 6) === 0 && (Jn = _e() + 500,
                Qt()))
            }
            break;
        case 13:
            wn(function() {
                var r = Mt(e, 1);
                if (r !== null) {
                    var o = Ge();
                    Nt(r, e, 1, o)
                }
            }),
            fa(e, 1)
        }
    }
    ,
    Il = function(e) {
        if (e.tag === 13) {
            var t = Mt(e, 134217728);
            if (t !== null) {
                var n = Ge();
                Nt(t, e, 134217728, n)
            }
            fa(e, 134217728)
        }
    }
    ,
    xo = function(e) {
        if (e.tag === 13) {
            var t = tn(e)
              , n = Mt(e, t);
            if (n !== null) {
                var r = Ge();
                Nt(n, e, t, r)
            }
            fa(e, t)
        }
    }
    ,
    yo = function() {
        return xe
    }
    ,
    vo = function(e, t) {
        var n = xe;
        try {
            return xe = e,
            t()
        } finally {
            xe = n
        }
    }
    ,
    Rl = function(e, t, n) {
        switch (t) {
        case "input":
            if (jl(e, n),
            t = n.name,
            n.type === "radio" && t != null) {
                for (n = e; n.parentNode; )
                    n = n.parentNode;
                for (n = n.querySelectorAll("input[name=" + JSON.stringify("" + t) + '][type="radio"]'),
                t = 0; t < n.length; t++) {
                    var r = n[t];
                    if (r !== e && r.form === e.form) {
                        var o = Ss(r);
                        if (!o)
                            throw Error(l(90));
                        Ba(r),
                        jl(r, o)
                    }
                }
            }
            break;
        case "textarea":
            qa(e, n);
            break;
        case "select":
            t = n.value,
            t != null && Pn(e, !!n.multiple, t, !1)
        }
    }
    ,
    no = la,
    ro = wn;
    var Eh = {
        usingClientEntryPoint: !1,
        Events: [Pr, $n, Ss, eo, to, la]
    }
      , Br = {
        findFiberByHostInstance: fn,
        bundleType: 0,
        version: "18.3.1",
        rendererPackageName: "react-dom"
    }
      , Ph = {
        bundleType: Br.bundleType,
        version: Br.version,
        rendererPackageName: Br.rendererPackageName,
        rendererConfig: Br.rendererConfig,
        overrideHookState: null,
        overrideHookStateDeletePath: null,
        overrideHookStateRenamePath: null,
        overrideProps: null,
        overridePropsDeletePath: null,
        overridePropsRenamePath: null,
        setErrorHandler: null,
        setSuspenseHandler: null,
        scheduleUpdate: null,
        currentDispatcherRef: H.ReactCurrentDispatcher,
        findHostInstanceByFiber: function(e) {
            return e = ao(e),
            e === null ? null : e.stateNode
        },
        findFiberByHostInstance: Br.findFiberByHostInstance || Sh,
        findHostInstancesForRefresh: null,
        scheduleRefresh: null,
        scheduleRoot: null,
        setRefreshHandler: null,
        getCurrentFiber: null,
        reconcilerVersion: "18.3.1-next-f1338f8080-20240426"
    };
    if (typeof __REACT_DEVTOOLS_GLOBAL_HOOK__ < "u") {
        var ul = __REACT_DEVTOOLS_GLOBAL_HOOK__;
        if (!ul.isDisabled && ul.supportsFiber)
            try {
                is = ul.inject(Ph),
                jt = ul
            } catch {}
    }
    return rt.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED = Eh,
    rt.createPortal = function(e, t) {
        var n = 2 < arguments.length && arguments[2] !== void 0 ? arguments[2] : null;
        if (!ha(t))
            throw Error(l(200));
        return kh(e, t, null, n)
    }
    ,
    rt.createRoot = function(e, t) {
        if (!ha(e))
            throw Error(l(299));
        var n = !1
          , r = ""
          , o = Mc;
        return t != null && (t.unstable_strictMode === !0 && (n = !0),
        t.identifierPrefix !== void 0 && (r = t.identifierPrefix),
        t.onRecoverableError !== void 0 && (o = t.onRecoverableError)),
        t = da(e, 1, !1, null, null, n, !1, r, o),
        e[Rt] = t.current,
        Sr(e.nodeType === 8 ? e.parentNode : e),
        new pa(t)
    }
    ,
    rt.findDOMNode = function(e) {
        if (e == null)
            return null;
        if (e.nodeType === 1)
            return e;
        var t = e._reactInternals;
        if (t === void 0)
            throw typeof e.render == "function" ? Error(l(188)) : (e = Object.keys(e).join(","),
            Error(l(268, e)));
        return e = ao(t),
        e = e === null ? null : e.stateNode,
        e
    }
    ,
    rt.flushSync = function(e) {
        return wn(e)
    }
    ,
    rt.hydrate = function(e, t, n) {
        if (!al(t))
            throw Error(l(200));
        return ol(null, e, t, !0, n)
    }
    ,
    rt.hydrateRoot = function(e, t, n) {
        if (!ha(e))
            throw Error(l(405));
        var r = n != null && n.hydratedSources || null
          , o = !1
          , c = ""
          , p = Mc;
        if (n != null && (n.unstable_strictMode === !0 && (o = !0),
        n.identifierPrefix !== void 0 && (c = n.identifierPrefix),
        n.onRecoverableError !== void 0 && (p = n.onRecoverableError)),
        t = Tc(t, null, e, 1, n ?? null, o, !1, c, p),
        e[Rt] = t.current,
        Sr(e),
        r)
            for (e = 0; e < r.length; e++)
                n = r[e],
                o = n._getVersion,
                o = o(n._source),
                t.mutableSourceEagerHydrationData == null ? t.mutableSourceEagerHydrationData = [n, o] : t.mutableSourceEagerHydrationData.push(n, o);
        return new il(t)
    }
    ,
    rt.render = function(e, t, n) {
        if (!al(t))
            throw Error(l(200));
        return ol(null, e, t, !1, n)
    }
    ,
    rt.unmountComponentAtNode = function(e) {
        if (!al(e))
            throw Error(l(40));
        return e._reactRootContainer ? (wn(function() {
            ol(null, null, e, !1, function() {
                e._reactRootContainer = null,
                e[Rt] = null
            })
        }),
        !0) : !1
    }
    ,
    rt.unstable_batchedUpdates = la,
    rt.unstable_renderSubtreeIntoContainer = function(e, t, n, r) {
        if (!al(n))
            throw Error(l(200));
        if (e == null || e._reactInternals === void 0)
            throw Error(l(38));
        return ol(e, t, n, !1, r)
    }
    ,
    rt.version = "18.3.1-next-f1338f8080-20240426",
    rt
}
var Hc;
function jd() {
    if (Hc)
        return xa.exports;
    Hc = 1;
    function i() {
        if (!(typeof __REACT_DEVTOOLS_GLOBAL_HOOK__ > "u" || typeof __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE != "function"))
            try {
                __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE(i)
            } catch (s) {
                console.error(s)
            }
    }
    return i(),
    xa.exports = Dh(),
    xa.exports
}
var Kc;
function $h() {
    if (Kc)
        return cl;
    Kc = 1;
    var i = jd();
    return cl.createRoot = i.createRoot,
    cl.hydrateRoot = i.hydrateRoot,
    cl
}
var Ih = $h();
const Fh = Nd(Ih);
jd();
/**
 * @remix-run/router v1.23.4
 *
 * Copyright (c) Remix Software Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.md file in the root directory of this source tree.
 *
 * @license MIT
 */
function qr() {
    return qr = Object.assign ? Object.assign.bind() : function(i) {
        for (var s = 1; s < arguments.length; s++) {
            var l = arguments[s];
            for (var u in l)
                ({}).hasOwnProperty.call(l, u) && (i[u] = l[u])
        }
        return i
    }
    ,
    qr.apply(null, arguments)
}
var ln;
(function(i) {
    i.Pop = "POP",
    i.Push = "PUSH",
    i.Replace = "REPLACE"
}
)(ln || (ln = {}));
const Wc = "popstate";
function Uh(i) {
    i === void 0 && (i = {});
    function s(u, d) {
        let {pathname: f, search: h, hash: g} = u.location;
        return ja("", {
            pathname: f,
            search: h,
            hash: g
        }, d.state && d.state.usr || null, d.state && d.state.key || "default")
    }
    function l(u, d) {
        return typeof d == "string" ? d : fl(d)
    }
    return Vh(s, l, null, i)
}
function ze(i, s) {
    if (i === !1 || i === null || typeof i > "u")
        throw new Error(s)
}
function kd(i, s) {
    if (!i) {
        typeof console < "u" && console.warn(s);
        try {
            throw new Error(s)
        } catch {}
    }
}
function Bh() {
    return Math.random().toString(36).substr(2, 8)
}
function qc(i, s) {
    return {
        usr: i.state,
        key: i.key,
        idx: s
    }
}
function ja(i, s, l, u) {
    return l === void 0 && (l = null),
    qr({
        pathname: typeof i == "string" ? i : i.pathname,
        search: "",
        hash: ""
    }, typeof s == "string" ? nr(s) : s, {
        state: l,
        key: s && s.key || u || Bh()
    })
}
function fl(i) {
    let {pathname: s="/", search: l="", hash: u=""} = i;
    return l && l !== "?" && (s += l.charAt(0) === "?" ? l : "?" + l),
    u && u !== "#" && (s += u.charAt(0) === "#" ? u : "#" + u),
    s
}
function nr(i) {
    let s = {};
    if (i) {
        let l = i.indexOf("#");
        l >= 0 && (s.hash = i.substr(l),
        i = i.substr(0, l));
        let u = i.indexOf("?");
        u >= 0 && (s.search = i.substr(u),
        i = i.substr(0, u)),
        i && (s.pathname = i)
    }
    return s
}
function Vh(i, s, l, u) {
    u === void 0 && (u = {});
    let {window: d=document.defaultView, v5Compat: f=!1} = u
      , h = d.history
      , g = ln.Pop
      , m = null
      , x = b();
    x == null && (x = 0,
    h.replaceState(qr({}, h.state, {
        idx: x
    }), ""));
    function b() {
        return (h.state || {
            idx: null
        }).idx
    }
    function w() {
        g = ln.Pop;
        let P = b()
          , $ = P == null ? null : P - x;
        x = P,
        m && m({
            action: g,
            location: _.location,
            delta: $
        })
    }
    function v(P, $) {
        g = ln.Push;
        let I = ja(_.location, P, $);
        x = b() + 1;
        let V = qc(I, x)
          , H = _.createHref(I);
        try {
            h.pushState(V, "", H)
        } catch (se) {
            if (se instanceof DOMException && se.name === "DataCloneError")
                throw se;
            d.location.assign(H)
        }
        f && m && m({
            action: g,
            location: _.location,
            delta: 1
        })
    }
    function R(P, $) {
        g = ln.Replace;
        let I = ja(_.location, P, $);
        x = b();
        let V = qc(I, x)
          , H = _.createHref(I);
        h.replaceState(V, "", H),
        f && m && m({
            action: g,
            location: _.location,
            delta: 0
        })
    }
    function E(P) {
        let $ = d.location.origin !== "null" ? d.location.origin : d.location.href
          , I = typeof P == "string" ? P : fl(P);
        return I = I.replace(/ $/, "%20"),
        ze($, "No window.location.(origin|href) available to create URL for href: " + I),
        new URL(I,$)
    }
    let _ = {
        get action() {
            return g
        },
        get location() {
            return i(d, h)
        },
        listen(P) {
            if (m)
                throw new Error("A history only accepts one active listener");
            return d.addEventListener(Wc, w),
            m = P,
            () => {
                d.removeEventListener(Wc, w),
                m = null
            }
        },
        createHref(P) {
            return s(d, P)
        },
        createURL: E,
        encodeLocation(P) {
            let $ = E(P);
            return {
                pathname: $.pathname,
                search: $.search,
                hash: $.hash
            }
        },
        push: v,
        replace: R,
        go(P) {
            return h.go(P)
        }
    };
    return _
}
var Yc;
(function(i) {
    i.data = "data",
    i.deferred = "deferred",
    i.redirect = "redirect",
    i.error = "error"
}
)(Yc || (Yc = {}));
function Hh(i, s, l) {
    return l === void 0 && (l = "/"),
    Kh(i, s, l)
}
function Kh(i, s, l, u) {
    let d = typeof s == "string" ? nr(s) : s
      , f = Da(d.pathname || "/", l);
    if (f == null)
        return null;
    let h = Sd(i);
    Wh(h);
    let g = null
      , m = sm(f);
    for (let x = 0; g == null && x < h.length; ++x)
        g = tm(h[x], m);
    return g
}
function Sd(i, s, l, u) {
    s === void 0 && (s = []),
    l === void 0 && (l = []),
    u === void 0 && (u = "");
    let d = (f, h, g) => {
        let m = {
            relativePath: g === void 0 ? f.path || "" : g,
            caseSensitive: f.caseSensitive === !0,
            childrenIndex: h,
            route: f
        };
        m.relativePath.startsWith("/") && (ze(m.relativePath.startsWith(u), 'Absolute route path "' + m.relativePath + '" nested under path ' + ('"' + u + '" is not valid. An absolute child route path ') + "must start with the combined path of all its parent routes."),
        m.relativePath = m.relativePath.slice(u.length));
        let x = on([u, m.relativePath])
          , b = l.concat(m);
        f.children && f.children.length > 0 && (ze(f.index !== !0, "Index routes must not have child routes. Please remove " + ('all child routes from route path "' + x + '".')),
        Sd(f.children, s, b, x)),
        !(f.path == null && !f.index) && s.push({
            path: x,
            score: Zh(x, f.index),
            routesMeta: b
        })
    }
    ;
    return i.forEach( (f, h) => {
        var g;
        if (f.path === "" || !((g = f.path) != null && g.includes("?")))
            d(f, h);
        else
            for (let m of Cd(f.path))
                d(f, h, m)
    }
    ),
    s
}
function Cd(i) {
    let s = i.split("/");
    if (s.length === 0)
        return [];
    let[l,...u] = s
      , d = l.endsWith("?")
      , f = l.replace(/\?$/, "");
    if (u.length === 0)
        return d ? [f, ""] : [f];
    let h = Cd(u.join("/"))
      , g = [];
    return g.push(...h.map(m => m === "" ? f : [f, m].join("/"))),
    d && g.push(...h),
    g.map(m => i.startsWith("/") && m === "" ? "/" : m)
}
function Wh(i) {
    i.sort( (s, l) => s.score !== l.score ? l.score - s.score : em(s.routesMeta.map(u => u.childrenIndex), l.routesMeta.map(u => u.childrenIndex)))
}
const qh = /^:[\w-]+$/
  , Yh = 3
  , Qh = 2
  , Gh = 1
  , Jh = 10
  , Xh = -2
  , Qc = i => i === "*";
function Zh(i, s) {
    let l = i.split("/")
      , u = l.length;
    return l.some(Qc) && (u += Xh),
    s && (u += Qh),
    l.filter(d => !Qc(d)).reduce( (d, f) => d + (qh.test(f) ? Yh : f === "" ? Gh : Jh), u)
}
function em(i, s) {
    return i.length === s.length && i.slice(0, -1).every( (u, d) => u === s[d]) ? i[i.length - 1] - s[s.length - 1] : 0
}
function tm(i, s, l) {
    let {routesMeta: u} = i
      , d = {}
      , f = "/"
      , h = [];
    for (let g = 0; g < u.length; ++g) {
        let m = u[g]
          , x = g === u.length - 1
          , b = f === "/" ? s : s.slice(f.length) || "/"
          , w = nm({
            path: m.relativePath,
            caseSensitive: m.caseSensitive,
            end: x
        }, b)
          , v = m.route;
        if (!w)
            return null;
        Object.assign(d, w.params),
        h.push({
            params: d,
            pathname: on([f, w.pathname]),
            pathnameBase: am(on([f, w.pathnameBase])),
            route: v
        }),
        w.pathnameBase !== "/" && (f = on([f, w.pathnameBase]))
    }
    return h
}
function nm(i, s) {
    typeof i == "string" && (i = {
        path: i,
        caseSensitive: !1,
        end: !0
    });
    let[l,u] = rm(i.path, i.caseSensitive, i.end)
      , d = s.match(l);
    if (!d)
        return null;
    let f = d[0]
      , h = f.replace(/(.)\/+$/, "$1")
      , g = d.slice(1);
    return {
        params: u.reduce( (x, b, w) => {
            let {paramName: v, isOptional: R} = b;
            if (v === "*") {
                let _ = g[w] || "";
                h = f.slice(0, f.length - _.length).replace(/(.)\/+$/, "$1")
            }
            const E = g[w];
            return R && !E ? x[v] = void 0 : x[v] = (E || "").replace(/%2F/g, "/"),
            x
        }
        , {}),
        pathname: f,
        pathnameBase: h,
        pattern: i
    }
}
function rm(i, s, l) {
    s === void 0 && (s = !1),
    l === void 0 && (l = !0),
    kd(i === "*" || !i.endsWith("*") || i.endsWith("/*"), 'Route path "' + i + '" will be treated as if it were ' + ('"' + i.replace(/\*$/, "/*") + '" because the `*` character must ') + "always follow a `/` in the pattern. To get rid of this warning, " + ('please change the route path to "' + i.replace(/\*$/, "/*") + '".'));
    let u = []
      , d = "^" + i.replace(/\/*\*?$/, "").replace(/^\/*/, "/").replace(/[\\.*+^${}|()[\]]/g, "\\$&").replace(/\/:([\w-]+)(\?)?/g, (h, g, m) => (u.push({
        paramName: g,
        isOptional: m != null
    }),
    m ? "/?([^\\/]+)?" : "/([^\\/]+)"));
    return i.endsWith("*") ? (u.push({
        paramName: "*"
    }),
    d += i === "*" || i === "/*" ? "(.*)$" : "(?:\\/(.+)|\\/*)$") : l ? d += "\\/*$" : i !== "" && i !== "/" && (d += "(?:(?=\\/|$))"),
    [new RegExp(d,s ? void 0 : "i"), u]
}
function sm(i) {
    try {
        return i.split("/").map(s => decodeURIComponent(s).replace(/\//g, "%2F")).join("/")
    } catch (s) {
        return kd(!1, 'The URL path "' + i + '" could not be decoded because it is is a malformed URL segment. This is probably due to a bad percent ' + ("encoding (" + s + ").")),
        i
    }
}
function Da(i, s) {
    if (s === "/")
        return i;
    if (!i.toLowerCase().startsWith(s.toLowerCase()))
        return null;
    let l = s.endsWith("/") ? s.length - 1 : s.length
      , u = i.charAt(l);
    return u && u !== "/" ? null : i.slice(l) || "/"
}
function lm(i, s) {
    s === void 0 && (s = "/");
    let {pathname: l, search: u="", hash: d=""} = typeof i == "string" ? nr(i) : i, f;
    return l ? (l = Ld(l),
    l.startsWith("/") ? f = Gc(l.substring(1), "/") : f = Gc(l, s)) : f = s,
    {
        pathname: f,
        search: om(u),
        hash: um(d)
    }
}
function Gc(i, s) {
    let l = s.replace(/\/+$/, "").split("/");
    return i.split("/").forEach(d => {
        d === ".." ? l.length > 1 && l.pop() : d !== "." && l.push(d)
    }
    ),
    l.length > 1 ? l.join("/") : "/"
}
function wa(i, s, l, u) {
    return "Cannot include a '" + i + "' character in a manually specified " + ("`to." + s + "` field [" + JSON.stringify(u) + "].  Please separate it out to the ") + ("`to." + l + "` field. Alternatively you may provide the full path as ") + 'a string in <Link to="..."> and the router will parse it for you.'
}
function im(i) {
    return i.filter( (s, l) => l === 0 || s.route.path && s.route.path.length > 0)
}
function Ed(i, s) {
    let l = im(i);
    return s ? l.map( (u, d) => d === l.length - 1 ? u.pathname : u.pathnameBase) : l.map(u => u.pathnameBase)
}
function Pd(i, s, l, u) {
    u === void 0 && (u = !1);
    let d;
    typeof i == "string" ? d = nr(i) : (d = qr({}, i),
    ze(!d.pathname || !d.pathname.includes("?"), wa("?", "pathname", "search", d)),
    ze(!d.pathname || !d.pathname.includes("#"), wa("#", "pathname", "hash", d)),
    ze(!d.search || !d.search.includes("#"), wa("#", "search", "hash", d)));
    let f = i === "" || d.pathname === "", h = f ? "/" : d.pathname, g;
    if (h == null)
        g = l;
    else {
        let w = s.length - 1;
        if (!u && h.startsWith("..")) {
            let v = h.split("/");
            for (; v[0] === ".."; )
                v.shift(),
                w -= 1;
            d.pathname = v.join("/")
        }
        g = w >= 0 ? s[w] : "/"
    }
    let m = lm(d, g)
      , x = h && h !== "/" && h.endsWith("/")
      , b = (f || h === ".") && l.endsWith("/");
    return !m.pathname.endsWith("/") && (x || b) && (m.pathname += "/"),
    m
}
const Ld = i => i.replace(/\/\/+/g, "/")
  , on = i => Ld(i.join("/"))
  , am = i => i.replace(/\/+$/, "").replace(/^\/*/, "/")
  , om = i => !i || i === "?" ? "" : i.startsWith("?") ? i : "?" + i
  , um = i => !i || i === "#" ? "" : i.startsWith("#") ? i : "#" + i;
function cm(i) {
    return i != null && typeof i.status == "number" && typeof i.statusText == "string" && typeof i.internal == "boolean" && "data" in i
}
const _d = ["post", "put", "patch", "delete"];
new Set(_d);
const dm = ["get", ..._d];
new Set(dm);
/**
 * React Router v6.30.6
 *
 * Copyright (c) Remix Software Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.md file in the root directory of this source tree.
 *
 * @license MIT
 */
function Yr() {
    return Yr = Object.assign ? Object.assign.bind() : function(i) {
        for (var s = 1; s < arguments.length; s++) {
            var l = arguments[s];
            for (var u in l)
                ({}).hasOwnProperty.call(l, u) && (i[u] = l[u])
        }
        return i
    }
    ,
    Yr.apply(null, arguments)
}
const $a = O.createContext(null)
  , fm = O.createContext(null)
  , En = O.createContext(null)
  , yl = O.createContext(null)
  , cn = O.createContext({
    outlet: null,
    matches: [],
    isDataRoute: !1
})
  , Rd = O.createContext(null);
function pm(i, s) {
    let {relative: l} = s === void 0 ? {} : s;
    Jr() || ze(!1);
    let {basename: u, navigator: d} = O.useContext(En)
      , {hash: f, pathname: h, search: g} = Td(i, {
        relative: l
    })
      , m = h;
    return u !== "/" && (m = h === "/" ? u : on([u, h])),
    d.createHref({
        pathname: m,
        search: g,
        hash: f
    })
}
function Jr() {
    return O.useContext(yl) != null
}
function Xr() {
    return Jr() || ze(!1),
    O.useContext(yl).location
}
function Od(i) {
    O.useContext(En).static || O.useLayoutEffect(i)
}
function rr() {
    let {isDataRoute: i} = O.useContext(cn);
    return i ? Em() : hm()
}
function hm() {
    Jr() || ze(!1);
    let i = O.useContext($a)
      , {basename: s, future: l, navigator: u} = O.useContext(En)
      , {matches: d} = O.useContext(cn)
      , {pathname: f} = Xr()
      , h = JSON.stringify(Ed(d, l.v7_relativeSplatPath))
      , g = O.useRef(!1);
    return Od( () => {
        g.current = !0
    }
    ),
    O.useCallback(function(x, b) {
        if (b === void 0 && (b = {}),
        !g.current)
            return;
        if (typeof x == "number") {
            u.go(x);
            return
        }
        let w = Pd(x, JSON.parse(h), f, b.relative === "path");
        i == null && s !== "/" && (w.pathname = w.pathname === "/" ? s : on([s, w.pathname])),
        (b.replace ? u.replace : u.push)(w, b.state, b)
    }, [s, u, h, f, i])
}
function mm() {
    let {matches: i} = O.useContext(cn)
      , s = i[i.length - 1];
    return s ? s.params : {}
}
function Td(i, s) {
    let {relative: l} = s === void 0 ? {} : s
      , {future: u} = O.useContext(En)
      , {matches: d} = O.useContext(cn)
      , {pathname: f} = Xr()
      , h = JSON.stringify(Ed(d, u.v7_relativeSplatPath));
    return O.useMemo( () => Pd(i, JSON.parse(h), f, l === "path"), [i, h, f, l])
}
function gm(i, s) {
    return xm(i, s)
}
function xm(i, s, l, u) {
    Jr() || ze(!1);
    let {navigator: d} = O.useContext(En)
      , {matches: f} = O.useContext(cn)
      , h = f[f.length - 1]
      , g = h ? h.params : {};
    h && h.pathname;
    let m = h ? h.pathnameBase : "/";
    h && h.route;
    let x = Xr(), b;
    if (s) {
        var w;
        let P = typeof s == "string" ? nr(s) : s;
        m === "/" || (w = P.pathname) != null && w.startsWith(m) || ze(!1),
        b = P
    } else
        b = x;
    let v = b.pathname || "/"
      , R = v;
    if (m !== "/") {
        let P = m.replace(/^\//, "").split("/");
        R = "/" + v.replace(/^\//, "").split("/").slice(P.length).join("/")
    }
    let E = Hh(i, {
        pathname: R
    })
      , _ = Nm(E && E.map(P => Object.assign({}, P, {
        params: Object.assign({}, g, P.params),
        pathname: on([m, d.encodeLocation ? d.encodeLocation(P.pathname).pathname : P.pathname]),
        pathnameBase: P.pathnameBase === "/" ? m : on([m, d.encodeLocation ? d.encodeLocation(P.pathnameBase).pathname : P.pathnameBase])
    })), f, l, u);
    return s && _ ? O.createElement(yl.Provider, {
        value: {
            location: Yr({
                pathname: "/",
                search: "",
                hash: "",
                state: null,
                key: "default"
            }, b),
            navigationType: ln.Pop
        }
    }, _) : _
}
function ym() {
    let i = Cm()
      , s = cm(i) ? i.status + " " + i.statusText : i instanceof Error ? i.message : JSON.stringify(i)
      , l = i instanceof Error ? i.stack : null
      , d = {
        padding: "0.5rem",
        backgroundColor: "rgba(200,200,200, 0.5)"
    };
    return O.createElement(O.Fragment, null, O.createElement("h2", null, "Unexpected Application Error!"), O.createElement("h3", {
        style: {
            fontStyle: "italic"
        }
    }, s), l ? O.createElement("pre", {
        style: d
    }, l) : null, null)
}
const vm = O.createElement(ym, null);
class wm extends O.Component {
    constructor(s) {
        super(s),
        this.state = {
            location: s.location,
            revalidation: s.revalidation,
            error: s.error
        }
    }
    static getDerivedStateFromError(s) {
        return {
            error: s
        }
    }
    static getDerivedStateFromProps(s, l) {
        return l.location !== s.location || l.revalidation !== "idle" && s.revalidation === "idle" ? {
            error: s.error,
            location: s.location,
            revalidation: s.revalidation
        } : {
            error: s.error !== void 0 ? s.error : l.error,
            location: l.location,
            revalidation: s.revalidation || l.revalidation
        }
    }
    componentDidCatch(s, l) {
        console.error("React Router caught the following error during render", s, l)
    }
    render() {
        return this.state.error !== void 0 ? O.createElement(cn.Provider, {
            value: this.props.routeContext
        }, O.createElement(Rd.Provider, {
            value: this.state.error,
            children: this.props.component
        })) : this.props.children
    }
}
function bm(i) {
    let {routeContext: s, match: l, children: u} = i
      , d = O.useContext($a);
    return d && d.static && d.staticContext && (l.route.errorElement || l.route.ErrorBoundary) && (d.staticContext._deepestRenderedBoundaryId = l.route.id),
    O.createElement(cn.Provider, {
        value: s
    }, u)
}
function Nm(i, s, l, u) {
    var d;
    if (s === void 0 && (s = []),
    l === void 0 && (l = null),
    u === void 0 && (u = null),
    i == null) {
        var f;
        if (!l)
            return null;
        if (l.errors)
            i = l.matches;
        else if ((f = u) != null && f.v7_partialHydration && s.length === 0 && !l.initialized && l.matches.length > 0)
            i = l.matches;
        else
            return null
    }
    let h = i
      , g = (d = l) == null ? void 0 : d.errors;
    if (g != null) {
        let b = h.findIndex(w => w.route.id && (g == null ? void 0 : g[w.route.id]) !== void 0);
        b >= 0 || ze(!1),
        h = h.slice(0, Math.min(h.length, b + 1))
    }
    let m = !1
      , x = -1;
    if (l && u && u.v7_partialHydration)
        for (let b = 0; b < h.length; b++) {
            let w = h[b];
            if ((w.route.HydrateFallback || w.route.hydrateFallbackElement) && (x = b),
            w.route.id) {
                let {loaderData: v, errors: R} = l
                  , E = w.route.loader && v[w.route.id] === void 0 && (!R || R[w.route.id] === void 0);
                if (w.route.lazy || E) {
                    m = !0,
                    x >= 0 ? h = h.slice(0, x + 1) : h = [h[0]];
                    break
                }
            }
        }
    return h.reduceRight( (b, w, v) => {
        let R, E = !1, _ = null, P = null;
        l && (R = g && w.route.id ? g[w.route.id] : void 0,
        _ = w.route.errorElement || vm,
        m && (x < 0 && v === 0 ? (Pm("route-fallback"),
        E = !0,
        P = null) : x === v && (E = !0,
        P = w.route.hydrateFallbackElement || null)));
        let $ = s.concat(h.slice(0, v + 1))
          , I = () => {
            let V;
            return R ? V = _ : E ? V = P : w.route.Component ? V = O.createElement(w.route.Component, null) : w.route.element ? V = w.route.element : V = b,
            O.createElement(bm, {
                match: w,
                routeContext: {
                    outlet: b,
                    matches: $,
                    isDataRoute: l != null
                },
                children: V
            })
        }
        ;
        return l && (w.route.ErrorBoundary || w.route.errorElement || v === 0) ? O.createElement(wm, {
            location: l.location,
            revalidation: l.revalidation,
            component: _,
            error: R,
            children: I(),
            routeContext: {
                outlet: null,
                matches: $,
                isDataRoute: !0
            }
        }) : I()
    }
    , null)
}
var zd = (function(i) {
    return i.UseBlocker = "useBlocker",
    i.UseRevalidator = "useRevalidator",
    i.UseNavigateStable = "useNavigate",
    i
}
)(zd || {})
  , Md = (function(i) {
    return i.UseBlocker = "useBlocker",
    i.UseLoaderData = "useLoaderData",
    i.UseActionData = "useActionData",
    i.UseRouteError = "useRouteError",
    i.UseNavigation = "useNavigation",
    i.UseRouteLoaderData = "useRouteLoaderData",
    i.UseMatches = "useMatches",
    i.UseRevalidator = "useRevalidator",
    i.UseNavigateStable = "useNavigate",
    i.UseRouteId = "useRouteId",
    i
}
)(Md || {});
function jm(i) {
    let s = O.useContext($a);
    return s || ze(!1),
    s
}
function km(i) {
    let s = O.useContext(fm);
    return s || ze(!1),
    s
}
function Sm(i) {
    let s = O.useContext(cn);
    return s || ze(!1),
    s
}
function Ad(i) {
    let s = Sm()
      , l = s.matches[s.matches.length - 1];
    return l.route.id || ze(!1),
    l.route.id
}
function Cm() {
    var i;
    let s = O.useContext(Rd)
      , l = km()
      , u = Ad();
    return s !== void 0 ? s : (i = l.errors) == null ? void 0 : i[u]
}
function Em() {
    let {router: i} = jm(zd.UseNavigateStable)
      , s = Ad(Md.UseNavigateStable)
      , l = O.useRef(!1);
    return Od( () => {
        l.current = !0
    }
    ),
    O.useCallback(function(d, f) {
        f === void 0 && (f = {}),
        l.current && (typeof d == "number" ? i.navigate(d) : i.navigate(d, Yr({
            fromRouteId: s
        }, f)))
    }, [i, s])
}
const Jc = {};
function Pm(i, s, l) {
    Jc[i] || (Jc[i] = !0)
}
function Lm(i, s) {
    i == null || i.v7_startTransition,
    i == null || i.v7_relativeSplatPath
}
function It(i) {
    ze(!1)
}
function _m(i) {
    let {basename: s="/", children: l=null, location: u, navigationType: d=ln.Pop, navigator: f, static: h=!1, future: g} = i;
    Jr() && ze(!1);
    let m = s.replace(/^\/*/, "/")
      , x = O.useMemo( () => ({
        basename: m,
        navigator: f,
        static: h,
        future: Yr({
            v7_relativeSplatPath: !1
        }, g)
    }), [m, g, f, h]);
    typeof u == "string" && (u = nr(u));
    let {pathname: b="/", search: w="", hash: v="", state: R=null, key: E="default"} = u
      , _ = O.useMemo( () => {
        let P = Da(b, m);
        return P == null ? null : {
            location: {
                pathname: P,
                search: w,
                hash: v,
                state: R,
                key: E
            },
            navigationType: d
        }
    }
    , [m, b, w, v, R, E, d]);
    return _ == null ? null : O.createElement(En.Provider, {
        value: x
    }, O.createElement(yl.Provider, {
        children: l,
        value: _
    }))
}
function Rm(i) {
    let {children: s, location: l} = i;
    return gm(ka(s), l)
}
new Promise( () => {}
);
function ka(i, s) {
    s === void 0 && (s = []);
    let l = [];
    return O.Children.forEach(i, (u, d) => {
        if (!O.isValidElement(u))
            return;
        let f = [...s, d];
        if (u.type === O.Fragment) {
            l.push.apply(l, ka(u.props.children, f));
            return
        }
        u.type !== It && ze(!1),
        !u.props.index || !u.props.children || ze(!1);
        let h = {
            id: u.props.id || f.join("-"),
            caseSensitive: u.props.caseSensitive,
            element: u.props.element,
            Component: u.props.Component,
            index: u.props.index,
            path: u.props.path,
            loader: u.props.loader,
            action: u.props.action,
            errorElement: u.props.errorElement,
            ErrorBoundary: u.props.ErrorBoundary,
            hasErrorBoundary: u.props.ErrorBoundary != null || u.props.errorElement != null,
            shouldRevalidate: u.props.shouldRevalidate,
            handle: u.props.handle,
            lazy: u.props.lazy
        };
        u.props.children && (h.children = ka(u.props.children, f)),
        l.push(h)
    }
    ),
    l
}
/**
 * React Router DOM v6.30.6
 *
 * Copyright (c) Remix Software Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.md file in the root directory of this source tree.
 *
 * @license MIT
 */
function Sa() {
    return Sa = Object.assign ? Object.assign.bind() : function(i) {
        for (var s = 1; s < arguments.length; s++) {
            var l = arguments[s];
            for (var u in l)
                ({}).hasOwnProperty.call(l, u) && (i[u] = l[u])
        }
        return i
    }
    ,
    Sa.apply(null, arguments)
}
function Om(i, s) {
    if (i == null)
        return {};
    var l = {};
    for (var u in i)
        if ({}.hasOwnProperty.call(i, u)) {
            if (s.indexOf(u) !== -1)
                continue;
            l[u] = i[u]
        }
    return l
}
function Tm(i) {
    return !!(i.metaKey || i.altKey || i.ctrlKey || i.shiftKey)
}
function zm(i, s) {
    return i.button === 0 && (!s || s === "_self") && !Tm(i)
}
const Mm = ["onClick", "relative", "reloadDocument", "replace", "state", "target", "to", "preventScrollReset", "viewTransition"]
  , Am = "6";
try {
    window.__reactRouterVersion = Am
} catch {}
const Dm = "startTransition"
  , Xc = zh[Dm];
function $m(i) {
    let {basename: s, children: l, future: u, window: d} = i
      , f = O.useRef();
    f.current == null && (f.current = Uh({
        window: d,
        v5Compat: !0
    }));
    let h = f.current
      , [g,m] = O.useState({
        action: h.action,
        location: h.location
    })
      , {v7_startTransition: x} = u || {}
      , b = O.useCallback(w => {
        x && Xc ? Xc( () => m(w)) : m(w)
    }
    , [m, x]);
    return O.useLayoutEffect( () => h.listen(b), [h, b]),
    O.useEffect( () => Lm(u), [u]),
    O.createElement(_m, {
        basename: s,
        children: l,
        location: g.location,
        navigationType: g.action,
        navigator: h,
        future: u
    })
}
const Im = typeof window < "u" && typeof window.document < "u" && typeof window.document.createElement < "u"
  , Fm = /^(?:[a-z][a-z0-9+.-]*:|\/\/)/i
  , Ue = O.forwardRef(function(s, l) {
    let {onClick: u, relative: d, reloadDocument: f, replace: h, state: g, target: m, to: x, preventScrollReset: b, viewTransition: w} = s, v = Om(s, Mm), {basename: R} = O.useContext(En), E, _ = !1;
    if (typeof x == "string" && Fm.test(x) && (E = x,
    Im))
        try {
            let V = new URL(window.location.href)
              , H = x.startsWith("//") ? new URL(V.protocol + x) : new URL(x)
              , se = Da(H.pathname, R);
            H.origin === V.origin && se != null ? x = se + H.search + H.hash : _ = !0
        } catch {}
    let P = pm(x, {
        relative: d
    })
      , $ = Um(x, {
        replace: h,
        state: g,
        target: m,
        preventScrollReset: b,
        relative: d,
        viewTransition: w
    });
    function I(V) {
        u && u(V),
        V.defaultPrevented || $(V)
    }
    return O.createElement("a", Sa({}, v, {
        href: E || P,
        onClick: _ || f ? u : I,
        ref: l,
        target: m
    }))
});
var Zc;
(function(i) {
    i.UseScrollRestoration = "useScrollRestoration",
    i.UseSubmit = "useSubmit",
    i.UseSubmitFetcher = "useSubmitFetcher",
    i.UseFetcher = "useFetcher",
    i.useViewTransitionState = "useViewTransitionState"
}
)(Zc || (Zc = {}));
var ed;
(function(i) {
    i.UseFetcher = "useFetcher",
    i.UseFetchers = "useFetchers",
    i.UseScrollRestoration = "useScrollRestoration"
}
)(ed || (ed = {}));
function Um(i, s) {
    let {target: l, replace: u, state: d, preventScrollReset: f, relative: h, viewTransition: g} = s === void 0 ? {} : s
      , m = rr()
      , x = Xr()
      , b = Td(i, {
        relative: h
    });
    return O.useCallback(w => {
        if (zm(w, l)) {
            w.preventDefault();
            let v = u !== void 0 ? u : fl(x) === fl(b);
            m(i, {
                replace: v,
                state: d,
                preventScrollReset: f,
                relative: h,
                viewTransition: g
            })
        }
    }
    , [x, m, b, u, d, l, i, f, h, g])
}
const Bm = (i, s, l, u) => {
    var f, h, g, m;
    const d = [l, {
        code: s,
        ...u || {}
    }];
    if ((h = (f = i == null ? void 0 : i.services) == null ? void 0 : f.logger) != null && h.forward)
        return i.services.logger.forward(d, "warn", "react-i18next::", !0);
    Sn(d[0]) && (d[0] = `react-i18next:: ${d[0]}`),
    (m = (g = i == null ? void 0 : i.services) == null ? void 0 : g.logger) != null && m.warn ? i.services.logger.warn(...d) : console != null && console.warn && console.warn(...d)
}
  , td = {}
  , Ca = (i, s, l, u) => {
    Sn(l) && td[l] || (Sn(l) && (td[l] = new Date),
    Bm(i, s, l, u))
}
  , Dd = (i, s) => () => {
    if (i.isInitialized)
        s();
    else {
        const l = () => {
            setTimeout( () => {
                i.off("initialized", l)
            }
            , 0),
            s()
        }
        ;
        i.on("initialized", l)
    }
}
  , Ea = (i, s, l) => {
    i.loadNamespaces(s, Dd(i, l))
}
  , nd = (i, s, l, u) => {
    if (Sn(l) && (l = [l]),
    i.options.preload && i.options.preload.indexOf(s) > -1)
        return Ea(i, l, u);
    l.forEach(d => {
        i.options.ns.indexOf(d) < 0 && i.options.ns.push(d)
    }
    ),
    i.loadLanguages(s, Dd(i, u))
}
  , Vm = (i, s, l={}) => !s.languages || !s.languages.length ? (Ca(s, "NO_LANGUAGES", "i18n.languages were undefined or empty", {
    languages: s.languages
}),
!0) : s.hasLoadedNamespace(i, {
    lng: l.lng,
    precheck: (u, d) => {
        if (l.bindI18n && l.bindI18n.indexOf("languageChanging") > -1 && u.services.backendConnector.backend && u.isLanguageChangingTo && !d(u.isLanguageChangingTo, i))
            return !1
    }
})
  , Sn = i => typeof i == "string"
  , Hm = i => typeof i == "object" && i !== null
  , Km = /&(?:amp|#38|lt|#60|gt|#62|apos|#39|quot|#34|nbsp|#160|copy|#169|reg|#174|hellip|#8230|#x2F|#47);/g
  , Wm = {
    "&amp;": "&",
    "&#38;": "&",
    "&lt;": "<",
    "&#60;": "<",
    "&gt;": ">",
    "&#62;": ">",
    "&apos;": "'",
    "&#39;": "'",
    "&quot;": '"',
    "&#34;": '"',
    "&nbsp;": " ",
    "&#160;": " ",
    "&copy;": "©",
    "&#169;": "©",
    "&reg;": "®",
    "&#174;": "®",
    "&hellip;": "…",
    "&#8230;": "…",
    "&#x2F;": "/",
    "&#47;": "/"
}
  , qm = i => Wm[i]
  , Ym = i => i.replace(Km, qm);
let Pa = {
    bindI18n: "languageChanged",
    bindI18nStore: "",
    transEmptyNodeValue: "",
    transSupportBasicHtmlNodes: !0,
    transWrapTextNodes: "",
    transKeepBasicHtmlNodesFor: ["br", "strong", "i", "p"],
    useSuspense: !0,
    unescape: Ym
};
const Qm = (i={}) => {
    Pa = {
        ...Pa,
        ...i
    }
}
  , Gm = () => Pa;
let $d;
const Jm = i => {
    $d = i
}
  , Xm = () => $d
  , Zm = {
    type: "3rdParty",
    init(i) {
        Qm(i.options.react),
        Jm(i)
    }
}
  , eg = O.createContext();
class tg {
    constructor() {
        this.usedNamespaces = {}
    }
    addUsedNamespaces(s) {
        s.forEach(l => {
            this.usedNamespaces[l] || (this.usedNamespaces[l] = !0)
        }
        )
    }
    getUsedNamespaces() {
        return Object.keys(this.usedNamespaces)
    }
}
const ng = (i, s) => {
    const l = O.useRef();
    return O.useEffect( () => {
        l.current = i
    }
    , [i, s]),
    l.current
}
  , Id = (i, s, l, u) => i.getFixedT(s, l, u)
  , rg = (i, s, l, u) => O.useCallback(Id(i, s, l, u), [i, s, l, u])
  , Je = (i, s={}) => {
    var H, se, K, te;
    const {i18n: l} = s
      , {i18n: u, defaultNS: d} = O.useContext(eg) || {}
      , f = l || u || Xm();
    if (f && !f.reportNamespaces && (f.reportNamespaces = new tg),
    !f) {
        Ca(f, "NO_I18NEXT_INSTANCE", "useTranslation: You will need to pass in an i18next instance by using initReactI18next");
        const ee = (ue, ce) => Sn(ce) ? ce : Hm(ce) && Sn(ce.defaultValue) ? ce.defaultValue : Array.isArray(ue) ? ue[ue.length - 1] : ue
          , J = [ee, {}, !1];
        return J.t = ee,
        J.i18n = {},
        J.ready = !1,
        J
    }
    (H = f.options.react) != null && H.wait && Ca(f, "DEPRECATED_OPTION", "useTranslation: It seems you are still using the old wait option, you may migrate to the new useSuspense behaviour.");
    const h = {
        ...Gm(),
        ...f.options.react,
        ...s
    }
      , {useSuspense: g, keyPrefix: m} = h;
    let x = d || ((se = f.options) == null ? void 0 : se.defaultNS);
    x = Sn(x) ? [x] : x || ["translation"],
    (te = (K = f.reportNamespaces).addUsedNamespaces) == null || te.call(K, x);
    const b = (f.isInitialized || f.initializedStoreOnce) && x.every(ee => Vm(ee, f, h))
      , w = rg(f, s.lng || null, h.nsMode === "fallback" ? x : x[0], m)
      , v = () => w
      , R = () => Id(f, s.lng || null, h.nsMode === "fallback" ? x : x[0], m)
      , [E,_] = O.useState(v);
    let P = x.join();
    s.lng && (P = `${s.lng}${P}`);
    const $ = ng(P)
      , I = O.useRef(!0);
    O.useEffect( () => {
        const {bindI18n: ee, bindI18nStore: J} = h;
        I.current = !0,
        !b && !g && (s.lng ? nd(f, s.lng, x, () => {
            I.current && _(R)
        }
        ) : Ea(f, x, () => {
            I.current && _(R)
        }
        )),
        b && $ && $ !== P && I.current && _(R);
        const ue = () => {
            I.current && _(R)
        }
        ;
        return ee && (f == null || f.on(ee, ue)),
        J && (f == null || f.store.on(J, ue)),
        () => {
            I.current = !1,
            f && ee && (ee == null || ee.split(" ").forEach(ce => f.off(ce, ue))),
            J && f && J.split(" ").forEach(ce => f.store.off(ce, ue))
        }
    }
    , [f, P]),
    O.useEffect( () => {
        I.current && b && _(v)
    }
    , [f, m, b]);
    const V = [E, f, b];
    if (V.t = E,
    V.i18n = f,
    V.ready = b,
    b || !b && !g)
        return V;
    throw new Promise(ee => {
        s.lng ? nd(f, s.lng, x, () => ee()) : Ea(f, x, () => ee())
    }
    )
}
  , re = i => typeof i == "string"
  , Hr = () => {
    let i, s;
    const l = new Promise( (u, d) => {
        i = u,
        s = d
    }
    );
    return l.resolve = i,
    l.reject = s,
    l
}
  , rd = i => i == null ? "" : "" + i
  , sg = (i, s, l) => {
    i.forEach(u => {
        s[u] && (l[u] = s[u])
    }
    )
}
  , lg = /###/g
  , sd = i => i && i.indexOf("###") > -1 ? i.replace(lg, ".") : i
  , ld = i => !i || re(i)
  , Wr = (i, s, l) => {
    const u = re(s) ? s.split(".") : s;
    let d = 0;
    for (; d < u.length - 1; ) {
        if (ld(i))
            return {};
        const f = sd(u[d]);
        !i[f] && l && (i[f] = new l),
        Object.prototype.hasOwnProperty.call(i, f) ? i = i[f] : i = {},
        ++d
    }
    return ld(i) ? {} : {
        obj: i,
        k: sd(u[d])
    }
}
  , id = (i, s, l) => {
    const {obj: u, k: d} = Wr(i, s, Object);
    if (u !== void 0 || s.length === 1) {
        u[d] = l;
        return
    }
    let f = s[s.length - 1]
      , h = s.slice(0, s.length - 1)
      , g = Wr(i, h, Object);
    for (; g.obj === void 0 && h.length; )
        f = `${h[h.length - 1]}.${f}`,
        h = h.slice(0, h.length - 1),
        g = Wr(i, h, Object),
        g != null && g.obj && typeof g.obj[`${g.k}.${f}`] < "u" && (g.obj = void 0);
    g.obj[`${g.k}.${f}`] = l
}
  , ig = (i, s, l, u) => {
    const {obj: d, k: f} = Wr(i, s, Object);
    d[f] = d[f] || [],
    d[f].push(l)
}
  , pl = (i, s) => {
    const {obj: l, k: u} = Wr(i, s);
    if (l && Object.prototype.hasOwnProperty.call(l, u))
        return l[u]
}
  , ag = (i, s, l) => {
    const u = pl(i, l);
    return u !== void 0 ? u : pl(s, l)
}
  , Fd = (i, s, l) => {
    for (const u in s)
        u !== "__proto__" && u !== "constructor" && (u in i ? re(i[u]) || i[u] instanceof String || re(s[u]) || s[u] instanceof String ? l && (i[u] = s[u]) : Fd(i[u], s[u], l) : i[u] = s[u]);
    return i
}
  , Zn = i => i.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&");
var og = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;",
    "/": "&#x2F;"
};
const ug = i => re(i) ? i.replace(/[&<>"'\/]/g, s => og[s]) : i;
class cg {
    constructor(s) {
        this.capacity = s,
        this.regExpMap = new Map,
        this.regExpQueue = []
    }
    getRegExp(s) {
        const l = this.regExpMap.get(s);
        if (l !== void 0)
            return l;
        const u = new RegExp(s);
        return this.regExpQueue.length === this.capacity && this.regExpMap.delete(this.regExpQueue.shift()),
        this.regExpMap.set(s, u),
        this.regExpQueue.push(s),
        u
    }
}
const dg = [" ", ",", "?", "!", ";"]
  , fg = new cg(20)
  , pg = (i, s, l) => {
    s = s || "",
    l = l || "";
    const u = dg.filter(h => s.indexOf(h) < 0 && l.indexOf(h) < 0);
    if (u.length === 0)
        return !0;
    const d = fg.getRegExp(`(${u.map(h => h === "?" ? "\\?" : h).join("|")})`);
    let f = !d.test(i);
    if (!f) {
        const h = i.indexOf(l);
        h > 0 && !d.test(i.substring(0, h)) && (f = !0)
    }
    return f
}
  , La = function(i, s) {
    let l = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : ".";
    if (!i)
        return;
    if (i[s])
        return Object.prototype.hasOwnProperty.call(i, s) ? i[s] : void 0;
    const u = s.split(l);
    let d = i;
    for (let f = 0; f < u.length; ) {
        if (!d || typeof d != "object")
            return;
        let h, g = "";
        for (let m = f; m < u.length; ++m)
            if (m !== f && (g += l),
            g += u[m],
            h = d[g],
            h !== void 0) {
                if (["string", "number", "boolean"].indexOf(typeof h) > -1 && m < u.length - 1)
                    continue;
                f += m - f + 1;
                break
            }
        d = h
    }
    return d
}
  , hl = i => i == null ? void 0 : i.replace("_", "-")
  , hg = {
    type: "logger",
    log(i) {
        this.output("log", i)
    },
    warn(i) {
        this.output("warn", i)
    },
    error(i) {
        this.output("error", i)
    },
    output(i, s) {
        var l, u;
        (u = (l = console == null ? void 0 : console[i]) == null ? void 0 : l.apply) == null || u.call(l, console, s)
    }
};
class ml {
    constructor(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {};
        this.init(s, l)
    }
    init(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {};
        this.prefix = l.prefix || "i18next:",
        this.logger = s || hg,
        this.options = l,
        this.debug = l.debug
    }
    log() {
        for (var s = arguments.length, l = new Array(s), u = 0; u < s; u++)
            l[u] = arguments[u];
        return this.forward(l, "log", "", !0)
    }
    warn() {
        for (var s = arguments.length, l = new Array(s), u = 0; u < s; u++)
            l[u] = arguments[u];
        return this.forward(l, "warn", "", !0)
    }
    error() {
        for (var s = arguments.length, l = new Array(s), u = 0; u < s; u++)
            l[u] = arguments[u];
        return this.forward(l, "error", "")
    }
    deprecate() {
        for (var s = arguments.length, l = new Array(s), u = 0; u < s; u++)
            l[u] = arguments[u];
        return this.forward(l, "warn", "WARNING DEPRECATED: ", !0)
    }
    forward(s, l, u, d) {
        return d && !this.debug ? null : (re(s[0]) && (s[0] = `${u}${this.prefix} ${s[0]}`),
        this.logger[l](s))
    }
    create(s) {
        return new ml(this.logger,{
            prefix: `${this.prefix}:${s}:`,
            ...this.options
        })
    }
    clone(s) {
        return s = s || this.options,
        s.prefix = s.prefix || this.prefix,
        new ml(this.logger,s)
    }
}
var Pt = new ml;
class vl {
    constructor() {
        this.observers = {}
    }
    on(s, l) {
        return s.split(" ").forEach(u => {
            this.observers[u] || (this.observers[u] = new Map);
            const d = this.observers[u].get(l) || 0;
            this.observers[u].set(l, d + 1)
        }
        ),
        this
    }
    off(s, l) {
        if (this.observers[s]) {
            if (!l) {
                delete this.observers[s];
                return
            }
            this.observers[s].delete(l)
        }
    }
    emit(s) {
        for (var l = arguments.length, u = new Array(l > 1 ? l - 1 : 0), d = 1; d < l; d++)
            u[d - 1] = arguments[d];
        this.observers[s] && Array.from(this.observers[s].entries()).forEach(h => {
            let[g,m] = h;
            for (let x = 0; x < m; x++)
                g(...u)
        }
        ),
        this.observers["*"] && Array.from(this.observers["*"].entries()).forEach(h => {
            let[g,m] = h;
            for (let x = 0; x < m; x++)
                g.apply(g, [s, ...u])
        }
        )
    }
}
class ad extends vl {
    constructor(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {
            ns: ["translation"],
            defaultNS: "translation"
        };
        super(),
        this.data = s || {},
        this.options = l,
        this.options.keySeparator === void 0 && (this.options.keySeparator = "."),
        this.options.ignoreJSONStructure === void 0 && (this.options.ignoreJSONStructure = !0)
    }
    addNamespaces(s) {
        this.options.ns.indexOf(s) < 0 && this.options.ns.push(s)
    }
    removeNamespaces(s) {
        const l = this.options.ns.indexOf(s);
        l > -1 && this.options.ns.splice(l, 1)
    }
    getResource(s, l, u) {
        var x, b;
        let d = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {};
        const f = d.keySeparator !== void 0 ? d.keySeparator : this.options.keySeparator
          , h = d.ignoreJSONStructure !== void 0 ? d.ignoreJSONStructure : this.options.ignoreJSONStructure;
        let g;
        s.indexOf(".") > -1 ? g = s.split(".") : (g = [s, l],
        u && (Array.isArray(u) ? g.push(...u) : re(u) && f ? g.push(...u.split(f)) : g.push(u)));
        const m = pl(this.data, g);
        return !m && !l && !u && s.indexOf(".") > -1 && (s = g[0],
        l = g[1],
        u = g.slice(2).join(".")),
        m || !h || !re(u) ? m : La((b = (x = this.data) == null ? void 0 : x[s]) == null ? void 0 : b[l], u, f)
    }
    addResource(s, l, u, d) {
        let f = arguments.length > 4 && arguments[4] !== void 0 ? arguments[4] : {
            silent: !1
        };
        const h = f.keySeparator !== void 0 ? f.keySeparator : this.options.keySeparator;
        let g = [s, l];
        u && (g = g.concat(h ? u.split(h) : u)),
        s.indexOf(".") > -1 && (g = s.split("."),
        d = l,
        l = g[1]),
        this.addNamespaces(l),
        id(this.data, g, d),
        f.silent || this.emit("added", s, l, u, d)
    }
    addResources(s, l, u) {
        let d = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {
            silent: !1
        };
        for (const f in u)
            (re(u[f]) || Array.isArray(u[f])) && this.addResource(s, l, f, u[f], {
                silent: !0
            });
        d.silent || this.emit("added", s, l, u)
    }
    addResourceBundle(s, l, u, d, f) {
        let h = arguments.length > 5 && arguments[5] !== void 0 ? arguments[5] : {
            silent: !1,
            skipCopy: !1
        }
          , g = [s, l];
        s.indexOf(".") > -1 && (g = s.split("."),
        d = u,
        u = l,
        l = g[1]),
        this.addNamespaces(l);
        let m = pl(this.data, g) || {};
        h.skipCopy || (u = JSON.parse(JSON.stringify(u))),
        d ? Fd(m, u, f) : m = {
            ...m,
            ...u
        },
        id(this.data, g, m),
        h.silent || this.emit("added", s, l, u)
    }
    removeResourceBundle(s, l) {
        this.hasResourceBundle(s, l) && delete this.data[s][l],
        this.removeNamespaces(l),
        this.emit("removed", s, l)
    }
    hasResourceBundle(s, l) {
        return this.getResource(s, l) !== void 0
    }
    getResourceBundle(s, l) {
        return l || (l = this.options.defaultNS),
        this.getResource(s, l)
    }
    getDataByLanguage(s) {
        return this.data[s]
    }
    hasLanguageSomeTranslations(s) {
        const l = this.getDataByLanguage(s);
        return !!(l && Object.keys(l) || []).find(d => l[d] && Object.keys(l[d]).length > 0)
    }
    toJSON() {
        return this.data
    }
}
var Ud = {
    processors: {},
    addPostProcessor(i) {
        this.processors[i.name] = i
    },
    handle(i, s, l, u, d) {
        return i.forEach(f => {
            var h;
            s = ((h = this.processors[f]) == null ? void 0 : h.process(s, l, u, d)) ?? s
        }
        ),
        s
    }
};
const od = {}
  , ud = i => !re(i) && typeof i != "boolean" && typeof i != "number";
class gl extends vl {
    constructor(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {};
        super(),
        sg(["resourceStore", "languageUtils", "pluralResolver", "interpolator", "backendConnector", "i18nFormat", "utils"], s, this),
        this.options = l,
        this.options.keySeparator === void 0 && (this.options.keySeparator = "."),
        this.logger = Pt.create("translator")
    }
    changeLanguage(s) {
        s && (this.language = s)
    }
    exists(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {
            interpolation: {}
        };
        if (s == null)
            return !1;
        const u = this.resolve(s, l);
        return (u == null ? void 0 : u.res) !== void 0
    }
    extractFromKey(s, l) {
        let u = l.nsSeparator !== void 0 ? l.nsSeparator : this.options.nsSeparator;
        u === void 0 && (u = ":");
        const d = l.keySeparator !== void 0 ? l.keySeparator : this.options.keySeparator;
        let f = l.ns || this.options.defaultNS || [];
        const h = u && s.indexOf(u) > -1
          , g = !this.options.userDefinedKeySeparator && !l.keySeparator && !this.options.userDefinedNsSeparator && !l.nsSeparator && !pg(s, u, d);
        if (h && !g) {
            const m = s.match(this.interpolator.nestingRegexp);
            if (m && m.length > 0)
                return {
                    key: s,
                    namespaces: re(f) ? [f] : f
                };
            const x = s.split(u);
            (u !== d || u === d && this.options.ns.indexOf(x[0]) > -1) && (f = x.shift()),
            s = x.join(d)
        }
        return {
            key: s,
            namespaces: re(f) ? [f] : f
        }
    }
    translate(s, l, u) {
        if (typeof l != "object" && this.options.overloadTranslationOptionHandler && (l = this.options.overloadTranslationOptionHandler(arguments)),
        typeof l == "object" && (l = {
            ...l
        }),
        l || (l = {}),
        s == null)
            return "";
        Array.isArray(s) || (s = [String(s)]);
        const d = l.returnDetails !== void 0 ? l.returnDetails : this.options.returnDetails
          , f = l.keySeparator !== void 0 ? l.keySeparator : this.options.keySeparator
          , {key: h, namespaces: g} = this.extractFromKey(s[s.length - 1], l)
          , m = g[g.length - 1]
          , x = l.lng || this.language
          , b = l.appendNamespaceToCIMode || this.options.appendNamespaceToCIMode;
        if ((x == null ? void 0 : x.toLowerCase()) === "cimode") {
            if (b) {
                const ce = l.nsSeparator || this.options.nsSeparator;
                return d ? {
                    res: `${m}${ce}${h}`,
                    usedKey: h,
                    exactUsedKey: h,
                    usedLng: x,
                    usedNS: m,
                    usedParams: this.getUsedParamsDetails(l)
                } : `${m}${ce}${h}`
            }
            return d ? {
                res: h,
                usedKey: h,
                exactUsedKey: h,
                usedLng: x,
                usedNS: m,
                usedParams: this.getUsedParamsDetails(l)
            } : h
        }
        const w = this.resolve(s, l);
        let v = w == null ? void 0 : w.res;
        const R = (w == null ? void 0 : w.usedKey) || h
          , E = (w == null ? void 0 : w.exactUsedKey) || h
          , _ = ["[object Number]", "[object Function]", "[object RegExp]"]
          , P = l.joinArrays !== void 0 ? l.joinArrays : this.options.joinArrays
          , $ = !this.i18nFormat || this.i18nFormat.handleAsObject
          , I = l.count !== void 0 && !re(l.count)
          , V = gl.hasDefaultValue(l)
          , H = I ? this.pluralResolver.getSuffix(x, l.count, l) : ""
          , se = l.ordinal && I ? this.pluralResolver.getSuffix(x, l.count, {
            ordinal: !1
        }) : ""
          , K = I && !l.ordinal && l.count === 0
          , te = K && l[`defaultValue${this.options.pluralSeparator}zero`] || l[`defaultValue${H}`] || l[`defaultValue${se}`] || l.defaultValue;
        let ee = v;
        $ && !v && V && (ee = te);
        const J = ud(ee)
          , ue = Object.prototype.toString.apply(ee);
        if ($ && ee && J && _.indexOf(ue) < 0 && !(re(P) && Array.isArray(ee))) {
            if (!l.returnObjects && !this.options.returnObjects) {
                this.options.returnedObjectHandler || this.logger.warn("accessing an object - but returnObjects options is not enabled!");
                const ce = this.options.returnedObjectHandler ? this.options.returnedObjectHandler(R, ee, {
                    ...l,
                    ns: g
                }) : `key '${h} (${this.language})' returned an object instead of string.`;
                return d ? (w.res = ce,
                w.usedParams = this.getUsedParamsDetails(l),
                w) : ce
            }
            if (f) {
                const ce = Array.isArray(ee)
                  , me = ce ? [] : {}
                  , De = ce ? E : R;
                for (const je in ee)
                    if (Object.prototype.hasOwnProperty.call(ee, je)) {
                        const Pe = `${De}${f}${je}`;
                        V && !v ? me[je] = this.translate(Pe, {
                            ...l,
                            defaultValue: ud(te) ? te[je] : void 0,
                            joinArrays: !1,
                            ns: g
                        }) : me[je] = this.translate(Pe, {
                            ...l,
                            joinArrays: !1,
                            ns: g
                        }),
                        me[je] === Pe && (me[je] = ee[je])
                    }
                v = me
            }
        } else if ($ && re(P) && Array.isArray(v))
            v = v.join(P),
            v && (v = this.extendTranslation(v, s, l, u));
        else {
            let ce = !1
              , me = !1;
            !this.isValidLookup(v) && V && (ce = !0,
            v = te),
            this.isValidLookup(v) || (me = !0,
            v = h);
            const je = (l.missingKeyNoValueFallbackToKey || this.options.missingKeyNoValueFallbackToKey) && me ? void 0 : v
              , Pe = V && te !== v && this.options.updateMissing;
            if (me || ce || Pe) {
                if (this.logger.log(Pe ? "updateKey" : "missingKey", x, m, h, Pe ? te : v),
                f) {
                    const Y = this.resolve(h, {
                        ...l,
                        keySeparator: !1
                    });
                    Y && Y.res && this.logger.warn("Seems the loaded translations were in flat JSON format instead of nested. Either set keySeparator: false on init or make sure your translations are published in nested format.")
                }
                let Oe = [];
                const ye = this.languageUtils.getFallbackCodes(this.options.fallbackLng, l.lng || this.language);
                if (this.options.saveMissingTo === "fallback" && ye && ye[0])
                    for (let Y = 0; Y < ye.length; Y++)
                        Oe.push(ye[Y]);
                else
                    this.options.saveMissingTo === "all" ? Oe = this.languageUtils.toResolveHierarchy(l.lng || this.language) : Oe.push(l.lng || this.language);
                const F = (Y, U, k) => {
                    var le;
                    const T = V && k !== v ? k : je;
                    this.options.missingKeyHandler ? this.options.missingKeyHandler(Y, m, U, T, Pe, l) : (le = this.backendConnector) != null && le.saveMissing && this.backendConnector.saveMissing(Y, m, U, T, Pe, l),
                    this.emit("missingKey", Y, m, U, v)
                }
                ;
                this.options.saveMissing && (this.options.saveMissingPlurals && I ? Oe.forEach(Y => {
                    const U = this.pluralResolver.getSuffixes(Y, l);
                    K && l[`defaultValue${this.options.pluralSeparator}zero`] && U.indexOf(`${this.options.pluralSeparator}zero`) < 0 && U.push(`${this.options.pluralSeparator}zero`),
                    U.forEach(k => {
                        F([Y], h + k, l[`defaultValue${k}`] || te)
                    }
                    )
                }
                ) : F(Oe, h, te))
            }
            v = this.extendTranslation(v, s, l, w, u),
            me && v === h && this.options.appendNamespaceToMissingKey && (v = `${m}:${h}`),
            (me || ce) && this.options.parseMissingKeyHandler && (v = this.options.parseMissingKeyHandler(this.options.appendNamespaceToMissingKey ? `${m}:${h}` : h, ce ? v : void 0))
        }
        return d ? (w.res = v,
        w.usedParams = this.getUsedParamsDetails(l),
        w) : v
    }
    extendTranslation(s, l, u, d, f) {
        var x, b;
        var h = this;
        if ((x = this.i18nFormat) != null && x.parse)
            s = this.i18nFormat.parse(s, {
                ...this.options.interpolation.defaultVariables,
                ...u
            }, u.lng || this.language || d.usedLng, d.usedNS, d.usedKey, {
                resolved: d
            });
        else if (!u.skipInterpolation) {
            u.interpolation && this.interpolator.init({
                ...u,
                interpolation: {
                    ...this.options.interpolation,
                    ...u.interpolation
                }
            });
            const w = re(s) && (((b = u == null ? void 0 : u.interpolation) == null ? void 0 : b.skipOnVariables) !== void 0 ? u.interpolation.skipOnVariables : this.options.interpolation.skipOnVariables);
            let v;
            if (w) {
                const E = s.match(this.interpolator.nestingRegexp);
                v = E && E.length
            }
            let R = u.replace && !re(u.replace) ? u.replace : u;
            if (this.options.interpolation.defaultVariables && (R = {
                ...this.options.interpolation.defaultVariables,
                ...R
            }),
            s = this.interpolator.interpolate(s, R, u.lng || this.language || d.usedLng, u),
            w) {
                const E = s.match(this.interpolator.nestingRegexp)
                  , _ = E && E.length;
                v < _ && (u.nest = !1)
            }
            !u.lng && d && d.res && (u.lng = this.language || d.usedLng),
            u.nest !== !1 && (s = this.interpolator.nest(s, function() {
                for (var E = arguments.length, _ = new Array(E), P = 0; P < E; P++)
                    _[P] = arguments[P];
                return (f == null ? void 0 : f[0]) === _[0] && !u.context ? (h.logger.warn(`It seems you are nesting recursively key: ${_[0]} in key: ${l[0]}`),
                null) : h.translate(..._, l)
            }, u)),
            u.interpolation && this.interpolator.reset()
        }
        const g = u.postProcess || this.options.postProcess
          , m = re(g) ? [g] : g;
        return s != null && (m != null && m.length) && u.applyPostProcessor !== !1 && (s = Ud.handle(m, s, l, this.options && this.options.postProcessPassResolved ? {
            i18nResolved: {
                ...d,
                usedParams: this.getUsedParamsDetails(u)
            },
            ...u
        } : u, this)),
        s
    }
    resolve(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {}, u, d, f, h, g;
        return re(s) && (s = [s]),
        s.forEach(m => {
            if (this.isValidLookup(u))
                return;
            const x = this.extractFromKey(m, l)
              , b = x.key;
            d = b;
            let w = x.namespaces;
            this.options.fallbackNS && (w = w.concat(this.options.fallbackNS));
            const v = l.count !== void 0 && !re(l.count)
              , R = v && !l.ordinal && l.count === 0
              , E = l.context !== void 0 && (re(l.context) || typeof l.context == "number") && l.context !== ""
              , _ = l.lngs ? l.lngs : this.languageUtils.toResolveHierarchy(l.lng || this.language, l.fallbackLng);
            w.forEach(P => {
                var $, I;
                this.isValidLookup(u) || (g = P,
                !od[`${_[0]}-${P}`] && (($ = this.utils) != null && $.hasLoadedNamespace) && !((I = this.utils) != null && I.hasLoadedNamespace(g)) && (od[`${_[0]}-${P}`] = !0,
                this.logger.warn(`key "${d}" for languages "${_.join(", ")}" won't get resolved as namespace "${g}" was not yet loaded`, "This means something IS WRONG in your setup. You access the t function before i18next.init / i18next.loadNamespace / i18next.changeLanguage was done. Wait for the callback or Promise to resolve before accessing it!!!")),
                _.forEach(V => {
                    var K;
                    if (this.isValidLookup(u))
                        return;
                    h = V;
                    const H = [b];
                    if ((K = this.i18nFormat) != null && K.addLookupKeys)
                        this.i18nFormat.addLookupKeys(H, b, V, P, l);
                    else {
                        let te;
                        v && (te = this.pluralResolver.getSuffix(V, l.count, l));
                        const ee = `${this.options.pluralSeparator}zero`
                          , J = `${this.options.pluralSeparator}ordinal${this.options.pluralSeparator}`;
                        if (v && (H.push(b + te),
                        l.ordinal && te.indexOf(J) === 0 && H.push(b + te.replace(J, this.options.pluralSeparator)),
                        R && H.push(b + ee)),
                        E) {
                            const ue = `${b}${this.options.contextSeparator}${l.context}`;
                            H.push(ue),
                            v && (H.push(ue + te),
                            l.ordinal && te.indexOf(J) === 0 && H.push(ue + te.replace(J, this.options.pluralSeparator)),
                            R && H.push(ue + ee))
                        }
                    }
                    let se;
                    for (; se = H.pop(); )
                        this.isValidLookup(u) || (f = se,
                        u = this.getResource(V, P, se, l))
                }
                ))
            }
            )
        }
        ),
        {
            res: u,
            usedKey: d,
            exactUsedKey: f,
            usedLng: h,
            usedNS: g
        }
    }
    isValidLookup(s) {
        return s !== void 0 && !(!this.options.returnNull && s === null) && !(!this.options.returnEmptyString && s === "")
    }
    getResource(s, l, u) {
        var f;
        let d = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {};
        return (f = this.i18nFormat) != null && f.getResource ? this.i18nFormat.getResource(s, l, u, d) : this.resourceStore.getResource(s, l, u, d)
    }
    getUsedParamsDetails() {
        let s = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {};
        const l = ["defaultValue", "ordinal", "context", "replace", "lng", "lngs", "fallbackLng", "ns", "keySeparator", "nsSeparator", "returnObjects", "returnDetails", "joinArrays", "postProcess", "interpolation"]
          , u = s.replace && !re(s.replace);
        let d = u ? s.replace : s;
        if (u && typeof s.count < "u" && (d.count = s.count),
        this.options.interpolation.defaultVariables && (d = {
            ...this.options.interpolation.defaultVariables,
            ...d
        }),
        !u) {
            d = {
                ...d
            };
            for (const f of l)
                delete d[f]
        }
        return d
    }
    static hasDefaultValue(s) {
        const l = "defaultValue";
        for (const u in s)
            if (Object.prototype.hasOwnProperty.call(s, u) && l === u.substring(0, l.length) && s[u] !== void 0)
                return !0;
        return !1
    }
}
class cd {
    constructor(s) {
        this.options = s,
        this.supportedLngs = this.options.supportedLngs || !1,
        this.logger = Pt.create("languageUtils")
    }
    getScriptPartFromCode(s) {
        if (s = hl(s),
        !s || s.indexOf("-") < 0)
            return null;
        const l = s.split("-");
        return l.length === 2 || (l.pop(),
        l[l.length - 1].toLowerCase() === "x") ? null : this.formatLanguageCode(l.join("-"))
    }
    getLanguagePartFromCode(s) {
        if (s = hl(s),
        !s || s.indexOf("-") < 0)
            return s;
        const l = s.split("-");
        return this.formatLanguageCode(l[0])
    }
    formatLanguageCode(s) {
        if (re(s) && s.indexOf("-") > -1) {
            let l;
            try {
                l = Intl.getCanonicalLocales(s)[0]
            } catch {}
            return l && this.options.lowerCaseLng && (l = l.toLowerCase()),
            l || (this.options.lowerCaseLng ? s.toLowerCase() : s)
        }
        return this.options.cleanCode || this.options.lowerCaseLng ? s.toLowerCase() : s
    }
    isSupportedCode(s) {
        return (this.options.load === "languageOnly" || this.options.nonExplicitSupportedLngs) && (s = this.getLanguagePartFromCode(s)),
        !this.supportedLngs || !this.supportedLngs.length || this.supportedLngs.indexOf(s) > -1
    }
    getBestMatchFromCodes(s) {
        if (!s)
            return null;
        let l;
        return s.forEach(u => {
            if (l)
                return;
            const d = this.formatLanguageCode(u);
            (!this.options.supportedLngs || this.isSupportedCode(d)) && (l = d)
        }
        ),
        !l && this.options.supportedLngs && s.forEach(u => {
            if (l)
                return;
            const d = this.getLanguagePartFromCode(u);
            if (this.isSupportedCode(d))
                return l = d;
            l = this.options.supportedLngs.find(f => {
                if (f === d)
                    return f;
                if (!(f.indexOf("-") < 0 && d.indexOf("-") < 0) && (f.indexOf("-") > 0 && d.indexOf("-") < 0 && f.substring(0, f.indexOf("-")) === d || f.indexOf(d) === 0 && d.length > 1))
                    return f
            }
            )
        }
        ),
        l || (l = this.getFallbackCodes(this.options.fallbackLng)[0]),
        l
    }
    getFallbackCodes(s, l) {
        if (!s)
            return [];
        if (typeof s == "function" && (s = s(l)),
        re(s) && (s = [s]),
        Array.isArray(s))
            return s;
        if (!l)
            return s.default || [];
        let u = s[l];
        return u || (u = s[this.getScriptPartFromCode(l)]),
        u || (u = s[this.formatLanguageCode(l)]),
        u || (u = s[this.getLanguagePartFromCode(l)]),
        u || (u = s.default),
        u || []
    }
    toResolveHierarchy(s, l) {
        const u = this.getFallbackCodes(l || this.options.fallbackLng || [], s)
          , d = []
          , f = h => {
            h && (this.isSupportedCode(h) ? d.push(h) : this.logger.warn(`rejecting language code not found in supportedLngs: ${h}`))
        }
        ;
        return re(s) && (s.indexOf("-") > -1 || s.indexOf("_") > -1) ? (this.options.load !== "languageOnly" && f(this.formatLanguageCode(s)),
        this.options.load !== "languageOnly" && this.options.load !== "currentOnly" && f(this.getScriptPartFromCode(s)),
        this.options.load !== "currentOnly" && f(this.getLanguagePartFromCode(s))) : re(s) && f(this.formatLanguageCode(s)),
        u.forEach(h => {
            d.indexOf(h) < 0 && f(this.formatLanguageCode(h))
        }
        ),
        d
    }
}
const dd = {
    zero: 0,
    one: 1,
    two: 2,
    few: 3,
    many: 4,
    other: 5
}
  , fd = {
    select: i => i === 1 ? "one" : "other",
    resolvedOptions: () => ({
        pluralCategories: ["one", "other"]
    })
};
class mg {
    constructor(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {};
        this.languageUtils = s,
        this.options = l,
        this.logger = Pt.create("pluralResolver"),
        this.pluralRulesCache = {}
    }
    addRule(s, l) {
        this.rules[s] = l
    }
    clearCache() {
        this.pluralRulesCache = {}
    }
    getRule(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {};
        const u = hl(s === "dev" ? "en" : s)
          , d = l.ordinal ? "ordinal" : "cardinal"
          , f = JSON.stringify({
            cleanedCode: u,
            type: d
        });
        if (f in this.pluralRulesCache)
            return this.pluralRulesCache[f];
        let h;
        try {
            h = new Intl.PluralRules(u,{
                type: d
            })
        } catch {
            if (!Intl)
                return this.logger.error("No Intl support, please use an Intl polyfill!"),
                fd;
            if (!s.match(/-|_/))
                return fd;
            const m = this.languageUtils.getLanguagePartFromCode(s);
            h = this.getRule(m, l)
        }
        return this.pluralRulesCache[f] = h,
        h
    }
    needsPlural(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {}
          , u = this.getRule(s, l);
        return u || (u = this.getRule("dev", l)),
        (u == null ? void 0 : u.resolvedOptions().pluralCategories.length) > 1
    }
    getPluralFormsOfKey(s, l) {
        let u = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : {};
        return this.getSuffixes(s, u).map(d => `${l}${d}`)
    }
    getSuffixes(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {}
          , u = this.getRule(s, l);
        return u || (u = this.getRule("dev", l)),
        u ? u.resolvedOptions().pluralCategories.sort( (d, f) => dd[d] - dd[f]).map(d => `${this.options.prepend}${l.ordinal ? `ordinal${this.options.prepend}` : ""}${d}`) : []
    }
    getSuffix(s, l) {
        let u = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : {};
        const d = this.getRule(s, u);
        return d ? `${this.options.prepend}${u.ordinal ? `ordinal${this.options.prepend}` : ""}${d.select(l)}` : (this.logger.warn(`no plural rule found for: ${s}`),
        this.getSuffix("dev", l, u))
    }
}
const pd = function(i, s, l) {
    let u = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : "."
      , d = arguments.length > 4 && arguments[4] !== void 0 ? arguments[4] : !0
      , f = ag(i, s, l);
    return !f && d && re(l) && (f = La(i, l, u),
    f === void 0 && (f = La(s, l, u))),
    f
}
  , ba = i => i.replace(/\$/g, "$$$$");
class gg {
    constructor() {
        var l;
        let s = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {};
        this.logger = Pt.create("interpolator"),
        this.options = s,
        this.format = ((l = s == null ? void 0 : s.interpolation) == null ? void 0 : l.format) || (u => u),
        this.init(s)
    }
    init() {
        let s = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {};
        s.interpolation || (s.interpolation = {
            escapeValue: !0
        });
        const {escape: l, escapeValue: u, useRawValueToEscape: d, prefix: f, prefixEscaped: h, suffix: g, suffixEscaped: m, formatSeparator: x, unescapeSuffix: b, unescapePrefix: w, nestingPrefix: v, nestingPrefixEscaped: R, nestingSuffix: E, nestingSuffixEscaped: _, nestingOptionsSeparator: P, maxReplaces: $, alwaysFormat: I} = s.interpolation;
        this.escape = l !== void 0 ? l : ug,
        this.escapeValue = u !== void 0 ? u : !0,
        this.useRawValueToEscape = d !== void 0 ? d : !1,
        this.prefix = f ? Zn(f) : h || "{{",
        this.suffix = g ? Zn(g) : m || "}}",
        this.formatSeparator = x || ",",
        this.unescapePrefix = b ? "" : w || "-",
        this.unescapeSuffix = this.unescapePrefix ? "" : b || "",
        this.nestingPrefix = v ? Zn(v) : R || Zn("$t("),
        this.nestingSuffix = E ? Zn(E) : _ || Zn(")"),
        this.nestingOptionsSeparator = P || ",",
        this.maxReplaces = $ || 1e3,
        this.alwaysFormat = I !== void 0 ? I : !1,
        this.resetRegExp()
    }
    reset() {
        this.options && this.init(this.options)
    }
    resetRegExp() {
        const s = (l, u) => (l == null ? void 0 : l.source) === u ? (l.lastIndex = 0,
        l) : new RegExp(u,"g");
        this.regexp = s(this.regexp, `${this.prefix}(.+?)${this.suffix}`),
        this.regexpUnescape = s(this.regexpUnescape, `${this.prefix}${this.unescapePrefix}(.+?)${this.unescapeSuffix}${this.suffix}`),
        this.nestingRegexp = s(this.nestingRegexp, `${this.nestingPrefix}(.+?)${this.nestingSuffix}`)
    }
    interpolate(s, l, u, d) {
        var R;
        let f, h, g;
        const m = this.options && this.options.interpolation && this.options.interpolation.defaultVariables || {}
          , x = E => {
            if (E.indexOf(this.formatSeparator) < 0) {
                const I = pd(l, m, E, this.options.keySeparator, this.options.ignoreJSONStructure);
                return this.alwaysFormat ? this.format(I, void 0, u, {
                    ...d,
                    ...l,
                    interpolationkey: E
                }) : I
            }
            const _ = E.split(this.formatSeparator)
              , P = _.shift().trim()
              , $ = _.join(this.formatSeparator).trim();
            return this.format(pd(l, m, P, this.options.keySeparator, this.options.ignoreJSONStructure), $, u, {
                ...d,
                ...l,
                interpolationkey: P
            })
        }
        ;
        this.resetRegExp();
        const b = (d == null ? void 0 : d.missingInterpolationHandler) || this.options.missingInterpolationHandler
          , w = ((R = d == null ? void 0 : d.interpolation) == null ? void 0 : R.skipOnVariables) !== void 0 ? d.interpolation.skipOnVariables : this.options.interpolation.skipOnVariables;
        return [{
            regex: this.regexpUnescape,
            safeValue: E => ba(E)
        }, {
            regex: this.regexp,
            safeValue: E => this.escapeValue ? ba(this.escape(E)) : ba(E)
        }].forEach(E => {
            for (g = 0; f = E.regex.exec(s); ) {
                const _ = f[1].trim();
                if (h = x(_),
                h === void 0)
                    if (typeof b == "function") {
                        const $ = b(s, f, d);
                        h = re($) ? $ : ""
                    } else if (d && Object.prototype.hasOwnProperty.call(d, _))
                        h = "";
                    else if (w) {
                        h = f[0];
                        continue
                    } else
                        this.logger.warn(`missed to pass in variable ${_} for interpolating ${s}`),
                        h = "";
                else
                    !re(h) && !this.useRawValueToEscape && (h = rd(h));
                const P = E.safeValue(h);
                if (s = s.replace(f[0], P),
                w ? (E.regex.lastIndex += h.length,
                E.regex.lastIndex -= f[0].length) : E.regex.lastIndex = 0,
                g++,
                g >= this.maxReplaces)
                    break
            }
        }
        ),
        s
    }
    nest(s, l) {
        let u = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : {}, d, f, h;
        const g = (m, x) => {
            const b = this.nestingOptionsSeparator;
            if (m.indexOf(b) < 0)
                return m;
            const w = m.split(new RegExp(`${b}[ ]*{`));
            let v = `{${w[1]}`;
            m = w[0],
            v = this.interpolate(v, h);
            const R = v.match(/'/g)
              , E = v.match(/"/g);
            (((R == null ? void 0 : R.length) ?? 0) % 2 === 0 && !E || E.length % 2 !== 0) && (v = v.replace(/'/g, '"'));
            try {
                h = JSON.parse(v),
                x && (h = {
                    ...x,
                    ...h
                })
            } catch (_) {
                return this.logger.warn(`failed parsing options string in nesting for key ${m}`, _),
                `${m}${b}${v}`
            }
            return h.defaultValue && h.defaultValue.indexOf(this.prefix) > -1 && delete h.defaultValue,
            m
        }
        ;
        for (; d = this.nestingRegexp.exec(s); ) {
            let m = [];
            h = {
                ...u
            },
            h = h.replace && !re(h.replace) ? h.replace : h,
            h.applyPostProcessor = !1,
            delete h.defaultValue;
            let x = !1;
            if (d[0].indexOf(this.formatSeparator) !== -1 && !/{.*}/.test(d[1])) {
                const b = d[1].split(this.formatSeparator).map(w => w.trim());
                d[1] = b.shift(),
                m = b,
                x = !0
            }
            if (f = l(g.call(this, d[1].trim(), h), h),
            f && d[0] === s && !re(f))
                return f;
            re(f) || (f = rd(f)),
            f || (this.logger.warn(`missed to resolve ${d[1]} for nesting ${s}`),
            f = ""),
            x && (f = m.reduce( (b, w) => this.format(b, w, u.lng, {
                ...u,
                interpolationkey: d[1].trim()
            }), f.trim())),
            s = s.replace(d[0], f),
            this.regexp.lastIndex = 0
        }
        return s
    }
}
const xg = i => {
    let s = i.toLowerCase().trim();
    const l = {};
    if (i.indexOf("(") > -1) {
        const u = i.split("(");
        s = u[0].toLowerCase().trim();
        const d = u[1].substring(0, u[1].length - 1);
        s === "currency" && d.indexOf(":") < 0 ? l.currency || (l.currency = d.trim()) : s === "relativetime" && d.indexOf(":") < 0 ? l.range || (l.range = d.trim()) : d.split(";").forEach(h => {
            if (h) {
                const [g,...m] = h.split(":")
                  , x = m.join(":").trim().replace(/^'+|'+$/g, "")
                  , b = g.trim();
                l[b] || (l[b] = x),
                x === "false" && (l[b] = !1),
                x === "true" && (l[b] = !0),
                isNaN(x) || (l[b] = parseInt(x, 10))
            }
        }
        )
    }
    return {
        formatName: s,
        formatOptions: l
    }
}
  , er = i => {
    const s = {};
    return (l, u, d) => {
        let f = d;
        d && d.interpolationkey && d.formatParams && d.formatParams[d.interpolationkey] && d[d.interpolationkey] && (f = {
            ...f,
            [d.interpolationkey]: void 0
        });
        const h = u + JSON.stringify(f);
        let g = s[h];
        return g || (g = i(hl(u), d),
        s[h] = g),
        g(l)
    }
}
;
class yg {
    constructor() {
        let s = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {};
        this.logger = Pt.create("formatter"),
        this.options = s,
        this.formats = {
            number: er( (l, u) => {
                const d = new Intl.NumberFormat(l,{
                    ...u
                });
                return f => d.format(f)
            }
            ),
            currency: er( (l, u) => {
                const d = new Intl.NumberFormat(l,{
                    ...u,
                    style: "currency"
                });
                return f => d.format(f)
            }
            ),
            datetime: er( (l, u) => {
                const d = new Intl.DateTimeFormat(l,{
                    ...u
                });
                return f => d.format(f)
            }
            ),
            relativetime: er( (l, u) => {
                const d = new Intl.RelativeTimeFormat(l,{
                    ...u
                });
                return f => d.format(f, u.range || "day")
            }
            ),
            list: er( (l, u) => {
                const d = new Intl.ListFormat(l,{
                    ...u
                });
                return f => d.format(f)
            }
            )
        },
        this.init(s)
    }
    init(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {
            interpolation: {}
        };
        this.formatSeparator = l.interpolation.formatSeparator || ","
    }
    add(s, l) {
        this.formats[s.toLowerCase().trim()] = l
    }
    addCached(s, l) {
        this.formats[s.toLowerCase().trim()] = er(l)
    }
    format(s, l, u) {
        let d = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {};
        const f = l.split(this.formatSeparator);
        if (f.length > 1 && f[0].indexOf("(") > 1 && f[0].indexOf(")") < 0 && f.find(g => g.indexOf(")") > -1)) {
            const g = f.findIndex(m => m.indexOf(")") > -1);
            f[0] = [f[0], ...f.splice(1, g)].join(this.formatSeparator)
        }
        return f.reduce( (g, m) => {
            var w;
            const {formatName: x, formatOptions: b} = xg(m);
            if (this.formats[x]) {
                let v = g;
                try {
                    const R = ((w = d == null ? void 0 : d.formatParams) == null ? void 0 : w[d.interpolationkey]) || {}
                      , E = R.locale || R.lng || d.locale || d.lng || u;
                    v = this.formats[x](g, E, {
                        ...b,
                        ...d,
                        ...R
                    })
                } catch (R) {
                    this.logger.warn(R)
                }
                return v
            } else
                this.logger.warn(`there was no format function for ${x}`);
            return g
        }
        , s)
    }
}
const vg = (i, s) => {
    i.pending[s] !== void 0 && (delete i.pending[s],
    i.pendingCount--)
}
;
class wg extends vl {
    constructor(s, l, u) {
        var f, h;
        let d = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {};
        super(),
        this.backend = s,
        this.store = l,
        this.services = u,
        this.languageUtils = u.languageUtils,
        this.options = d,
        this.logger = Pt.create("backendConnector"),
        this.waitingReads = [],
        this.maxParallelReads = d.maxParallelReads || 10,
        this.readingCalls = 0,
        this.maxRetries = d.maxRetries >= 0 ? d.maxRetries : 5,
        this.retryTimeout = d.retryTimeout >= 1 ? d.retryTimeout : 350,
        this.state = {},
        this.queue = [],
        (h = (f = this.backend) == null ? void 0 : f.init) == null || h.call(f, u, d.backend, d)
    }
    queueLoad(s, l, u, d) {
        const f = {}
          , h = {}
          , g = {}
          , m = {};
        return s.forEach(x => {
            let b = !0;
            l.forEach(w => {
                const v = `${x}|${w}`;
                !u.reload && this.store.hasResourceBundle(x, w) ? this.state[v] = 2 : this.state[v] < 0 || (this.state[v] === 1 ? h[v] === void 0 && (h[v] = !0) : (this.state[v] = 1,
                b = !1,
                h[v] === void 0 && (h[v] = !0),
                f[v] === void 0 && (f[v] = !0),
                m[w] === void 0 && (m[w] = !0)))
            }
            ),
            b || (g[x] = !0)
        }
        ),
        (Object.keys(f).length || Object.keys(h).length) && this.queue.push({
            pending: h,
            pendingCount: Object.keys(h).length,
            loaded: {},
            errors: [],
            callback: d
        }),
        {
            toLoad: Object.keys(f),
            pending: Object.keys(h),
            toLoadLanguages: Object.keys(g),
            toLoadNamespaces: Object.keys(m)
        }
    }
    loaded(s, l, u) {
        const d = s.split("|")
          , f = d[0]
          , h = d[1];
        l && this.emit("failedLoading", f, h, l),
        !l && u && this.store.addResourceBundle(f, h, u, void 0, void 0, {
            skipCopy: !0
        }),
        this.state[s] = l ? -1 : 2,
        l && u && (this.state[s] = 0);
        const g = {};
        this.queue.forEach(m => {
            ig(m.loaded, [f], h),
            vg(m, s),
            l && m.errors.push(l),
            m.pendingCount === 0 && !m.done && (Object.keys(m.loaded).forEach(x => {
                g[x] || (g[x] = {});
                const b = m.loaded[x];
                b.length && b.forEach(w => {
                    g[x][w] === void 0 && (g[x][w] = !0)
                }
                )
            }
            ),
            m.done = !0,
            m.errors.length ? m.callback(m.errors) : m.callback())
        }
        ),
        this.emit("loaded", g),
        this.queue = this.queue.filter(m => !m.done)
    }
    read(s, l, u) {
        let d = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : 0
          , f = arguments.length > 4 && arguments[4] !== void 0 ? arguments[4] : this.retryTimeout
          , h = arguments.length > 5 ? arguments[5] : void 0;
        if (!s.length)
            return h(null, {});
        if (this.readingCalls >= this.maxParallelReads) {
            this.waitingReads.push({
                lng: s,
                ns: l,
                fcName: u,
                tried: d,
                wait: f,
                callback: h
            });
            return
        }
        this.readingCalls++;
        const g = (x, b) => {
            if (this.readingCalls--,
            this.waitingReads.length > 0) {
                const w = this.waitingReads.shift();
                this.read(w.lng, w.ns, w.fcName, w.tried, w.wait, w.callback)
            }
            if (x && b && d < this.maxRetries) {
                setTimeout( () => {
                    this.read.call(this, s, l, u, d + 1, f * 2, h)
                }
                , f);
                return
            }
            h(x, b)
        }
          , m = this.backend[u].bind(this.backend);
        if (m.length === 2) {
            try {
                const x = m(s, l);
                x && typeof x.then == "function" ? x.then(b => g(null, b)).catch(g) : g(null, x)
            } catch (x) {
                g(x)
            }
            return
        }
        return m(s, l, g)
    }
    prepareLoading(s, l) {
        let u = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : {}
          , d = arguments.length > 3 ? arguments[3] : void 0;
        if (!this.backend)
            return this.logger.warn("No backend was added via i18next.use. Will not load resources."),
            d && d();
        re(s) && (s = this.languageUtils.toResolveHierarchy(s)),
        re(l) && (l = [l]);
        const f = this.queueLoad(s, l, u, d);
        if (!f.toLoad.length)
            return f.pending.length || d(),
            null;
        f.toLoad.forEach(h => {
            this.loadOne(h)
        }
        )
    }
    load(s, l, u) {
        this.prepareLoading(s, l, {}, u)
    }
    reload(s, l, u) {
        this.prepareLoading(s, l, {
            reload: !0
        }, u)
    }
    loadOne(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : "";
        const u = s.split("|")
          , d = u[0]
          , f = u[1];
        this.read(d, f, "read", void 0, void 0, (h, g) => {
            h && this.logger.warn(`${l}loading namespace ${f} for language ${d} failed`, h),
            !h && g && this.logger.log(`${l}loaded namespace ${f} for language ${d}`, g),
            this.loaded(s, h, g)
        }
        )
    }
    saveMissing(s, l, u, d, f) {
        var m, x, b, w, v;
        let h = arguments.length > 5 && arguments[5] !== void 0 ? arguments[5] : {}
          , g = arguments.length > 6 && arguments[6] !== void 0 ? arguments[6] : () => {}
        ;
        if ((x = (m = this.services) == null ? void 0 : m.utils) != null && x.hasLoadedNamespace && !((w = (b = this.services) == null ? void 0 : b.utils) != null && w.hasLoadedNamespace(l))) {
            this.logger.warn(`did not save key "${u}" as the namespace "${l}" was not yet loaded`, "This means something IS WRONG in your setup. You access the t function before i18next.init / i18next.loadNamespace / i18next.changeLanguage was done. Wait for the callback or Promise to resolve before accessing it!!!");
            return
        }
        if (!(u == null || u === "")) {
            if ((v = this.backend) != null && v.create) {
                const R = {
                    ...h,
                    isUpdate: f
                }
                  , E = this.backend.create.bind(this.backend);
                if (E.length < 6)
                    try {
                        let _;
                        E.length === 5 ? _ = E(s, l, u, d, R) : _ = E(s, l, u, d),
                        _ && typeof _.then == "function" ? _.then(P => g(null, P)).catch(g) : g(null, _)
                    } catch (_) {
                        g(_)
                    }
                else
                    E(s, l, u, d, g, R)
            }
            !s || !s[0] || this.store.addResource(s[0], l, u, d)
        }
    }
}
const hd = () => ({
    debug: !1,
    initAsync: !0,
    ns: ["translation"],
    defaultNS: ["translation"],
    fallbackLng: ["dev"],
    fallbackNS: !1,
    supportedLngs: !1,
    nonExplicitSupportedLngs: !1,
    load: "all",
    preload: !1,
    simplifyPluralSuffix: !0,
    keySeparator: ".",
    nsSeparator: ":",
    pluralSeparator: "_",
    contextSeparator: "_",
    partialBundledLanguages: !1,
    saveMissing: !1,
    updateMissing: !1,
    saveMissingTo: "fallback",
    saveMissingPlurals: !0,
    missingKeyHandler: !1,
    missingInterpolationHandler: !1,
    postProcess: !1,
    postProcessPassResolved: !1,
    returnNull: !1,
    returnEmptyString: !0,
    returnObjects: !1,
    joinArrays: !1,
    returnedObjectHandler: !1,
    parseMissingKeyHandler: !1,
    appendNamespaceToMissingKey: !1,
    appendNamespaceToCIMode: !1,
    overloadTranslationOptionHandler: i => {
        let s = {};
        if (typeof i[1] == "object" && (s = i[1]),
        re(i[1]) && (s.defaultValue = i[1]),
        re(i[2]) && (s.tDescription = i[2]),
        typeof i[2] == "object" || typeof i[3] == "object") {
            const l = i[3] || i[2];
            Object.keys(l).forEach(u => {
                s[u] = l[u]
            }
            )
        }
        return s
    }
    ,
    interpolation: {
        escapeValue: !0,
        format: i => i,
        prefix: "{{",
        suffix: "}}",
        formatSeparator: ",",
        unescapePrefix: "-",
        nestingPrefix: "$t(",
        nestingSuffix: ")",
        nestingOptionsSeparator: ",",
        maxReplaces: 1e3,
        skipOnVariables: !0
    }
})
  , md = i => {
    var s, l;
    return re(i.ns) && (i.ns = [i.ns]),
    re(i.fallbackLng) && (i.fallbackLng = [i.fallbackLng]),
    re(i.fallbackNS) && (i.fallbackNS = [i.fallbackNS]),
    ((l = (s = i.supportedLngs) == null ? void 0 : s.indexOf) == null ? void 0 : l.call(s, "cimode")) < 0 && (i.supportedLngs = i.supportedLngs.concat(["cimode"])),
    typeof i.initImmediate == "boolean" && (i.initAsync = i.initImmediate),
    i
}
  , dl = () => {}
  , bg = i => {
    Object.getOwnPropertyNames(Object.getPrototypeOf(i)).forEach(l => {
        typeof i[l] == "function" && (i[l] = i[l].bind(i))
    }
    )
}
;
class Qr extends vl {
    constructor() {
        let s = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {}
          , l = arguments.length > 1 ? arguments[1] : void 0;
        if (super(),
        this.options = md(s),
        this.services = {},
        this.logger = Pt,
        this.modules = {
            external: []
        },
        bg(this),
        l && !this.isInitialized && !s.isClone) {
            if (!this.options.initAsync)
                return this.init(s, l),
                this;
            setTimeout( () => {
                this.init(s, l)
            }
            , 0)
        }
    }
    init() {
        var s = this;
        let l = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {}
          , u = arguments.length > 1 ? arguments[1] : void 0;
        this.isInitializing = !0,
        typeof l == "function" && (u = l,
        l = {}),
        l.defaultNS == null && l.ns && (re(l.ns) ? l.defaultNS = l.ns : l.ns.indexOf("translation") < 0 && (l.defaultNS = l.ns[0]));
        const d = hd();
        this.options = {
            ...d,
            ...this.options,
            ...md(l)
        },
        this.options.interpolation = {
            ...d.interpolation,
            ...this.options.interpolation
        },
        l.keySeparator !== void 0 && (this.options.userDefinedKeySeparator = l.keySeparator),
        l.nsSeparator !== void 0 && (this.options.userDefinedNsSeparator = l.nsSeparator);
        const f = b => b ? typeof b == "function" ? new b : b : null;
        if (!this.options.isClone) {
            this.modules.logger ? Pt.init(f(this.modules.logger), this.options) : Pt.init(null, this.options);
            let b;
            this.modules.formatter ? b = this.modules.formatter : b = yg;
            const w = new cd(this.options);
            this.store = new ad(this.options.resources,this.options);
            const v = this.services;
            v.logger = Pt,
            v.resourceStore = this.store,
            v.languageUtils = w,
            v.pluralResolver = new mg(w,{
                prepend: this.options.pluralSeparator,
                simplifyPluralSuffix: this.options.simplifyPluralSuffix
            }),
            b && (!this.options.interpolation.format || this.options.interpolation.format === d.interpolation.format) && (v.formatter = f(b),
            v.formatter.init(v, this.options),
            this.options.interpolation.format = v.formatter.format.bind(v.formatter)),
            v.interpolator = new gg(this.options),
            v.utils = {
                hasLoadedNamespace: this.hasLoadedNamespace.bind(this)
            },
            v.backendConnector = new wg(f(this.modules.backend),v.resourceStore,v,this.options),
            v.backendConnector.on("*", function(R) {
                for (var E = arguments.length, _ = new Array(E > 1 ? E - 1 : 0), P = 1; P < E; P++)
                    _[P - 1] = arguments[P];
                s.emit(R, ..._)
            }),
            this.modules.languageDetector && (v.languageDetector = f(this.modules.languageDetector),
            v.languageDetector.init && v.languageDetector.init(v, this.options.detection, this.options)),
            this.modules.i18nFormat && (v.i18nFormat = f(this.modules.i18nFormat),
            v.i18nFormat.init && v.i18nFormat.init(this)),
            this.translator = new gl(this.services,this.options),
            this.translator.on("*", function(R) {
                for (var E = arguments.length, _ = new Array(E > 1 ? E - 1 : 0), P = 1; P < E; P++)
                    _[P - 1] = arguments[P];
                s.emit(R, ..._)
            }),
            this.modules.external.forEach(R => {
                R.init && R.init(this)
            }
            )
        }
        if (this.format = this.options.interpolation.format,
        u || (u = dl),
        this.options.fallbackLng && !this.services.languageDetector && !this.options.lng) {
            const b = this.services.languageUtils.getFallbackCodes(this.options.fallbackLng);
            b.length > 0 && b[0] !== "dev" && (this.options.lng = b[0])
        }
        !this.services.languageDetector && !this.options.lng && this.logger.warn("init: no languageDetector is used and no lng is defined"),
        ["getResource", "hasResourceBundle", "getResourceBundle", "getDataByLanguage"].forEach(b => {
            this[b] = function() {
                return s.store[b](...arguments)
            }
        }
        ),
        ["addResource", "addResources", "addResourceBundle", "removeResourceBundle"].forEach(b => {
            this[b] = function() {
                return s.store[b](...arguments),
                s
            }
        }
        );
        const m = Hr()
          , x = () => {
            const b = (w, v) => {
                this.isInitializing = !1,
                this.isInitialized && !this.initializedStoreOnce && this.logger.warn("init: i18next is already initialized. You should call init just once!"),
                this.isInitialized = !0,
                this.options.isClone || this.logger.log("initialized", this.options),
                this.emit("initialized", this.options),
                m.resolve(v),
                u(w, v)
            }
            ;
            if (this.languages && !this.isInitialized)
                return b(null, this.t.bind(this));
            this.changeLanguage(this.options.lng, b)
        }
        ;
        return this.options.resources || !this.options.initAsync ? x() : setTimeout(x, 0),
        m
    }
    loadResources(s) {
        var f, h;
        let u = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : dl;
        const d = re(s) ? s : this.language;
        if (typeof s == "function" && (u = s),
        !this.options.resources || this.options.partialBundledLanguages) {
            if ((d == null ? void 0 : d.toLowerCase()) === "cimode" && (!this.options.preload || this.options.preload.length === 0))
                return u();
            const g = []
              , m = x => {
                if (!x || x === "cimode")
                    return;
                this.services.languageUtils.toResolveHierarchy(x).forEach(w => {
                    w !== "cimode" && g.indexOf(w) < 0 && g.push(w)
                }
                )
            }
            ;
            d ? m(d) : this.services.languageUtils.getFallbackCodes(this.options.fallbackLng).forEach(b => m(b)),
            (h = (f = this.options.preload) == null ? void 0 : f.forEach) == null || h.call(f, x => m(x)),
            this.services.backendConnector.load(g, this.options.ns, x => {
                !x && !this.resolvedLanguage && this.language && this.setResolvedLanguage(this.language),
                u(x)
            }
            )
        } else
            u(null)
    }
    reloadResources(s, l, u) {
        const d = Hr();
        return typeof s == "function" && (u = s,
        s = void 0),
        typeof l == "function" && (u = l,
        l = void 0),
        s || (s = this.languages),
        l || (l = this.options.ns),
        u || (u = dl),
        this.services.backendConnector.reload(s, l, f => {
            d.resolve(),
            u(f)
        }
        ),
        d
    }
    use(s) {
        if (!s)
            throw new Error("You are passing an undefined module! Please check the object you are passing to i18next.use()");
        if (!s.type)
            throw new Error("You are passing a wrong module! Please check the object you are passing to i18next.use()");
        return s.type === "backend" && (this.modules.backend = s),
        (s.type === "logger" || s.log && s.warn && s.error) && (this.modules.logger = s),
        s.type === "languageDetector" && (this.modules.languageDetector = s),
        s.type === "i18nFormat" && (this.modules.i18nFormat = s),
        s.type === "postProcessor" && Ud.addPostProcessor(s),
        s.type === "formatter" && (this.modules.formatter = s),
        s.type === "3rdParty" && this.modules.external.push(s),
        this
    }
    setResolvedLanguage(s) {
        if (!(!s || !this.languages) && !(["cimode", "dev"].indexOf(s) > -1))
            for (let l = 0; l < this.languages.length; l++) {
                const u = this.languages[l];
                if (!(["cimode", "dev"].indexOf(u) > -1) && this.store.hasLanguageSomeTranslations(u)) {
                    this.resolvedLanguage = u;
                    break
                }
            }
    }
    changeLanguage(s, l) {
        var u = this;
        this.isLanguageChangingTo = s;
        const d = Hr();
        this.emit("languageChanging", s);
        const f = m => {
            this.language = m,
            this.languages = this.services.languageUtils.toResolveHierarchy(m),
            this.resolvedLanguage = void 0,
            this.setResolvedLanguage(m)
        }
          , h = (m, x) => {
            x ? (f(x),
            this.translator.changeLanguage(x),
            this.isLanguageChangingTo = void 0,
            this.emit("languageChanged", x),
            this.logger.log("languageChanged", x)) : this.isLanguageChangingTo = void 0,
            d.resolve(function() {
                return u.t(...arguments)
            }),
            l && l(m, function() {
                return u.t(...arguments)
            })
        }
          , g = m => {
            var b, w;
            !s && !m && this.services.languageDetector && (m = []);
            const x = re(m) ? m : this.services.languageUtils.getBestMatchFromCodes(m);
            x && (this.language || f(x),
            this.translator.language || this.translator.changeLanguage(x),
            (w = (b = this.services.languageDetector) == null ? void 0 : b.cacheUserLanguage) == null || w.call(b, x)),
            this.loadResources(x, v => {
                h(v, x)
            }
            )
        }
        ;
        return !s && this.services.languageDetector && !this.services.languageDetector.async ? g(this.services.languageDetector.detect()) : !s && this.services.languageDetector && this.services.languageDetector.async ? this.services.languageDetector.detect.length === 0 ? this.services.languageDetector.detect().then(g) : this.services.languageDetector.detect(g) : g(s),
        d
    }
    getFixedT(s, l, u) {
        var d = this;
        const f = function(h, g) {
            let m;
            if (typeof g != "object") {
                for (var x = arguments.length, b = new Array(x > 2 ? x - 2 : 0), w = 2; w < x; w++)
                    b[w - 2] = arguments[w];
                m = d.options.overloadTranslationOptionHandler([h, g].concat(b))
            } else
                m = {
                    ...g
                };
            m.lng = m.lng || f.lng,
            m.lngs = m.lngs || f.lngs,
            m.ns = m.ns || f.ns,
            m.keyPrefix !== "" && (m.keyPrefix = m.keyPrefix || u || f.keyPrefix);
            const v = d.options.keySeparator || ".";
            let R;
            return m.keyPrefix && Array.isArray(h) ? R = h.map(E => `${m.keyPrefix}${v}${E}`) : R = m.keyPrefix ? `${m.keyPrefix}${v}${h}` : h,
            d.t(R, m)
        };
        return re(s) ? f.lng = s : f.lngs = s,
        f.ns = l,
        f.keyPrefix = u,
        f
    }
    t() {
        var d;
        for (var s = arguments.length, l = new Array(s), u = 0; u < s; u++)
            l[u] = arguments[u];
        return (d = this.translator) == null ? void 0 : d.translate(...l)
    }
    exists() {
        var d;
        for (var s = arguments.length, l = new Array(s), u = 0; u < s; u++)
            l[u] = arguments[u];
        return (d = this.translator) == null ? void 0 : d.exists(...l)
    }
    setDefaultNamespace(s) {
        this.options.defaultNS = s
    }
    hasLoadedNamespace(s) {
        let l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {};
        if (!this.isInitialized)
            return this.logger.warn("hasLoadedNamespace: i18next was not initialized", this.languages),
            !1;
        if (!this.languages || !this.languages.length)
            return this.logger.warn("hasLoadedNamespace: i18n.languages were undefined or empty", this.languages),
            !1;
        const u = l.lng || this.resolvedLanguage || this.languages[0]
          , d = this.options ? this.options.fallbackLng : !1
          , f = this.languages[this.languages.length - 1];
        if (u.toLowerCase() === "cimode")
            return !0;
        const h = (g, m) => {
            const x = this.services.backendConnector.state[`${g}|${m}`];
            return x === -1 || x === 0 || x === 2
        }
        ;
        if (l.precheck) {
            const g = l.precheck(this, h);
            if (g !== void 0)
                return g
        }
        return !!(this.hasResourceBundle(u, s) || !this.services.backendConnector.backend || this.options.resources && !this.options.partialBundledLanguages || h(u, s) && (!d || h(f, s)))
    }
    loadNamespaces(s, l) {
        const u = Hr();
        return this.options.ns ? (re(s) && (s = [s]),
        s.forEach(d => {
            this.options.ns.indexOf(d) < 0 && this.options.ns.push(d)
        }
        ),
        this.loadResources(d => {
            u.resolve(),
            l && l(d)
        }
        ),
        u) : (l && l(),
        Promise.resolve())
    }
    loadLanguages(s, l) {
        const u = Hr();
        re(s) && (s = [s]);
        const d = this.options.preload || []
          , f = s.filter(h => d.indexOf(h) < 0 && this.services.languageUtils.isSupportedCode(h));
        return f.length ? (this.options.preload = d.concat(f),
        this.loadResources(h => {
            u.resolve(),
            l && l(h)
        }
        ),
        u) : (l && l(),
        Promise.resolve())
    }
    dir(s) {
        var d, f;
        if (s || (s = this.resolvedLanguage || (((d = this.languages) == null ? void 0 : d.length) > 0 ? this.languages[0] : this.language)),
        !s)
            return "rtl";
        const l = ["ar", "shu", "sqr", "ssh", "xaa", "yhd", "yud", "aao", "abh", "abv", "acm", "acq", "acw", "acx", "acy", "adf", "ads", "aeb", "aec", "afb", "ajp", "apc", "apd", "arb", "arq", "ars", "ary", "arz", "auz", "avl", "ayh", "ayl", "ayn", "ayp", "bbz", "pga", "he", "iw", "ps", "pbt", "pbu", "pst", "prp", "prd", "ug", "ur", "ydd", "yds", "yih", "ji", "yi", "hbo", "men", "xmn", "fa", "jpr", "peo", "pes", "prs", "dv", "sam", "ckb"]
          , u = ((f = this.services) == null ? void 0 : f.languageUtils) || new cd(hd());
        return l.indexOf(u.getLanguagePartFromCode(s)) > -1 || s.toLowerCase().indexOf("-arab") > 1 ? "rtl" : "ltr"
    }
    static createInstance() {
        let s = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {}
          , l = arguments.length > 1 ? arguments[1] : void 0;
        return new Qr(s,l)
    }
    cloneInstance() {
        let s = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {}
          , l = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : dl;
        const u = s.forkResourceStore;
        u && delete s.forkResourceStore;
        const d = {
            ...this.options,
            ...s,
            isClone: !0
        }
          , f = new Qr(d);
        if ((s.debug !== void 0 || s.prefix !== void 0) && (f.logger = f.logger.clone(s)),
        ["store", "services", "language"].forEach(g => {
            f[g] = this[g]
        }
        ),
        f.services = {
            ...this.services
        },
        f.services.utils = {
            hasLoadedNamespace: f.hasLoadedNamespace.bind(f)
        },
        u) {
            const g = Object.keys(this.store.data).reduce( (m, x) => (m[x] = {
                ...this.store.data[x]
            },
            Object.keys(m[x]).reduce( (b, w) => (b[w] = {
                ...m[x][w]
            },
            b), {})), {});
            f.store = new ad(g,d),
            f.services.resourceStore = f.store
        }
        return f.translator = new gl(f.services,d),
        f.translator.on("*", function(g) {
            for (var m = arguments.length, x = new Array(m > 1 ? m - 1 : 0), b = 1; b < m; b++)
                x[b - 1] = arguments[b];
            f.emit(g, ...x)
        }),
        f.init(d, l),
        f.translator.options = d,
        f.translator.backendConnector.services.utils = {
            hasLoadedNamespace: f.hasLoadedNamespace.bind(f)
        },
        f
    }
    toJSON() {
        return {
            options: this.options,
            store: this.store,
            language: this.language,
            languages: this.languages,
            resolvedLanguage: this.resolvedLanguage
        }
    }
}
const He = Qr.createInstance();
He.createInstance = Qr.createInstance;
He.createInstance;
He.dir;
He.init;
He.loadResources;
He.reloadResources;
He.use;
He.changeLanguage;
He.getFixedT;
He.t;
He.exists;
He.setDefaultNamespace;
He.hasLoadedNamespace;
He.loadNamespaces;
He.loadLanguages;
const Ng = {
    title: "Yojana Setu",
    subtitle: "Government Scheme Finder & Application Guide",
    tagline: "Discover what you qualify for in under 2 minutes — with zero identity compromise.",
    privacyBadge: "Your answers stay on this device",
    disclaimer: "Independent public service tool. Not an official Government of India website. Always verify details on official portals."
}
  , jg = {
    home: "Home",
    finder: "Find Schemes",
    results: "Schemes",
    shortlist: "Saved List",
    privacy: "Privacy Guarantee",
    about: "Constitution & About",
    login: "Sign In (Optional)",
    logout: "Sign Out",
    guest: "Guest Mode",
    clearAnswers: "Clear My Answers"
}
  , kg = {
    heading: "Find Government Schemes You Qualify For",
    subheading: "Answer 6 simple questions in your language. See your eligible schemes, required documents, reasons, and how close you are to missed ones.",
    cta: "Start — takes ~2 minutes",
    continue: "Continue Checking",
    howItWorks: "How it works",
    step1: "1. Answer simple questions",
    step2: "2. View ranked schemes",
    step3: "3. Carry the right documents",
    privacyGuarantee: "Zero personal data sent. Your answers live only in your browser tab."
}
  , Sg = {
    title: "Constitutional Pillars",
    subtitle: "Schemes grounded in the ideals of the Preamble",
    all: "All Schemes",
    justice: "Justice",
    justiceSub: "Social, Economic & Political",
    liberty: "Liberty",
    libertySub: "Thought, Expression & Enterprise",
    equality: "Equality",
    equalitySub: "Status & Opportunity",
    fraternity: "Fraternity",
    fraternitySub: "Dignity & Social Security",
    filterActive: "Filtered by pillar"
}
  , Cg = {
    title: "Tell us about yourself",
    subtitle: "Takes less than two minutes. You can skip any question.",
    qAge: "What is your age?",
    qAgeHint: "In completed years (0 - 120)",
    qGender: "What is your gender?",
    female: "Woman",
    male: "Man",
    other: "Other",
    preferNot: "Prefer not to say",
    qState: "Which State or Union Territory do you live in?",
    selectState: "Select your State / UT",
    qResidence: "Where is your residence?",
    rural: "Village (Rural)",
    urban: "City / Town (Urban)",
    qIncome: "Annual household income (in Lakh ₹)",
    incomeHint: "Combined earnings of all family members in ₹ Lakh per year",
    qOccupation: "What describes your occupation / vocation?",
    farmer: "Farmer / Agriculture",
    student: "Student",
    artisan: "Traditional Artisan / Craftsman",
    street_vendor: "Street Vendor / Small Hawker",
    self_employed: "Self-employed / Business",
    salaried: "Salaried / Private Worker",
    unemployed: "Currently Unemployed",
    homemaker: "Homemaker",
    retired: "Senior Citizen / Retired",
    next: "Next",
    back: "Back",
    skip: "Skip for now",
    showSchemes: "Show My Schemes",
    coreProgress: "Question {{current}} of 6",
    refineTitle: "Improve your results",
    refineDesc: "Answer these quick optional questions to unlock more targeted schemes"
}
  , Eg = {
    category: "Social Category",
    categoryHint: "General / OBC / SC / ST",
    bpl: "Do you hold a BPL or Ration Card?",
    bplYes: "Yes (BPL / Antyodaya)",
    bplNo: "No (APL / Regular)",
    land: "Do you own agricultural land?",
    landYes: "Yes, I own land",
    landNo: "No land ownership",
    bank: "Do you have an active Bank Account?",
    bankYes: "Yes, active account",
    bankNo: "No bank account yet",
    pregnant: "Are you pregnant or nursing a child?",
    pregnantYes: "Yes",
    pregnantNo: "No",
    daughter: "Do you have a daughter under 10 years?",
    daughterYes: "Yes",
    daughterNo: "No",
    taxpayer: "Do you or family pay Income Tax?",
    taxpayerYes: "Yes, Income Tax payer",
    taxpayerNo: "No, Non-taxpayer"
}
  , Pg = {
    eligible: "Eligible",
    almost: "Almost Eligible",
    possible: "Possibly Eligible",
    not_eligible: "Not Eligible"
}
  , Lg = {
    eligible: "You appear to meet all listed eligibility requirements.",
    almost: "You are very close to qualifying. Check tolerances and easily fixable criteria.",
    possible: "Answer 1 or 2 more questions to confirm whether you qualify.",
    not_eligible: "You currently do not meet one or more criteria. See exact reasons below."
}
  , _g = {
    relevanceScore: "Relevance Score",
    benefits: "Key Benefits",
    documents: "Required Documents",
    steps: "Application Steps",
    source: "Official Guidelines & Source",
    lastVerified: "Last verified",
    applyNow: "Apply on Official Portal",
    save: "Save Scheme",
    saved: "Saved ★",
    printChecklist: "Print Document Checklist",
    whyNotTitle: "Why you did not qualify",
    nearMissTitle: "Near-Miss Gap & Action",
    scoreBreakdown: "Why this rank?",
    articles: "Constitutional Articles"
}
  , Rg = {
    "r.needFarmer": "Requires occupation to be a farmer or agriculturalist.",
    "r.needLand": "Requires agricultural cultivable land ownership.",
    "r.noTaxpayer": "Requires applicant not to be an income tax payer.",
    "r.needBpl": "Requires household to hold a BPL or SECC recognized card.",
    "r.needSenior70": "Requires age to be 70 years or above.",
    "r.needFemale": "Scheme is exclusively reserved for women applicants.",
    "r.needAge18": "Applicant must be at least 18 years of age.",
    "r.age18to40": "Applicant age must be between 18 and 40 years.",
    "r.needBank": "Requires an active savings bank account.",
    "r.needAge60": "Applicant must be aged 60 years or above.",
    "r.needPregnantOrNursing": "Requires applicant to be a pregnant woman or nursing mother.",
    "r.needDaughterUnder10": "Requires having a girl child under 10 years of age.",
    "r.needArtisan": "Applicant must be a traditional artisan or craftsperson (18 trades).",
    "r.needStudent": "Applicant must be an actively enrolled student.",
    "r.needSC": "Reserved for Scheduled Caste (SC) category.",
    "r.incomeMax25": "Family annual income must not exceed ₹2.5 Lakh.",
    "r.needSCorST": "Beneficiary must belong to Scheduled Caste (SC) or Scheduled Tribe (ST).",
    "r.needFemaleOrSCST": "Applicant must be a woman or belong to SC/ST category."
}
  , Og = {
    "fix.needBank": "Open a zero-balance PM Jan Dhan bank account at any bank branch.",
    "fix.incomeMax25": "Your income is close to the ₹2.5L limit; certain verified standard deductions may apply.",
    "fix.needAge60": "You will become eligible soon upon turning 60 years.",
    "fix.needAge18": "You will become eligible upon turning 18 years.",
    "fix.age18to40": "Age must be within 18–40 years at time of entry.",
    "fix.needSenior70": "Senior citizens turning 70 will qualify automatically."
}
  , Tg = {
    heading: "Privacy & Data Protection Guarantee",
    lead: "Yojana Setu is built on privacy-by-design under the Digital Personal Data Protection (DPDP) principles.",
    rule1Title: "Zero Answer Retention",
    rule1Desc: "None of your personal answers (age, income, caste, health, family) are ever transmitted to our server or saved in cookies, local storage, or databases.",
    rule2Title: "Client-Side Processing",
    rule2Desc: "The entire rules engine runs locally inside your browser memory. When you refresh or close this tab, all responses disappear completely.",
    rule3Title: "Optional Passwordless Auth",
    rule3Desc: "You never need to log in to find schemes or print document checklists. Login exists strictly if you want to save schemes across devices, using only a 6-digit email OTP.",
    rule4Title: "Right to Wipe",
    rule4Desc: "You can clear your answers or wipe all saved shortlist data at any time with a single tap.",
    wipeShortlist: "Wipe All My Saved Schemes",
    wipeAnswers: "Clear All Responses Now"
}
  , zg = {
    app: Ng,
    nav: jg,
    hero: kg,
    pillars: Sg,
    wizard: Cg,
    refine: Eg,
    status: Pg,
    statusDesc: Lg,
    scheme: _g,
    reasons: Rg,
    fixes: Og,
    privacy: Tg
}
  , Mg = {
    title: "योजना सेतु",
    subtitle: "सरकारी योजना खोजक एवं आवेदन मार्गदर्शिका",
    tagline: "बिना अपनी पहचान बताए 2 मिनट में जानें कि आप किन योजनाओं के पात्र हैं।",
    privacyBadge: "आपके उत्तर केवल इसी डिवाइस में रहते हैं",
    disclaimer: "स्वतंत्र जनसेवा साधन। भारत सरकार की आधिकारिक वेबसाइट नहीं। विवरण हमेशा आधिकारिक पोर्टल पर सत्यापित करें।"
}
  , Ag = {
    home: "होम",
    finder: "योजना खोजें",
    results: "योजनाएं",
    shortlist: "सहेजी गई सूची",
    privacy: "गोपनीयता सुरक्षा",
    about: "संविधान एवं परिचय",
    login: "लॉग इन (वैकल्पिक)",
    logout: "लॉग आउट",
    guest: "अतिथि मोड",
    clearAnswers: "मेरे उत्तर साफ़ करें"
}
  , Dg = {
    heading: "जानें किन सरकारी योजनाओं के लिए आप पात्र हैं",
    subheading: "अपनी भाषा में 6 सरल प्रश्नों के उत्तर दें। पात्र योजनाएं, आवश्यक दस्तावेज, कारण और यदि चूके हैं तो कितने करीब हैं, सब जानें।",
    cta: "शुरू करें — लगभग 2 मिनट",
    continue: "जाँच जारी रखें",
    howItWorks: "यह कैसे काम करता है",
    step1: "१. सरल प्रश्नों के उत्तर दें",
    step2: "२. क्रमबद्ध योजनाएं देखें",
    step3: "३. सही दस्तावेज साथ रखें",
    privacyGuarantee: "कोई भी व्यक्तिगत डेटा सर्वर पर नहीं भेजा जाता। आपके उत्तर केवल इसी ब्राउज़र टैब में रहते हैं।"
}
  , $g = {
    title: "संवैधानिक स्तंभ",
    subtitle: "संविधान की प्रस्तावना के आदर्शों पर आधारित योजनाएं",
    all: "सभी योजनाएं",
    justice: "न्याय (Justice)",
    justiceSub: "सामाजिक, आर्थिक एवं राजनीतिक",
    liberty: "स्वतंत्रता (Liberty)",
    libertySub: "विचार, अभिव्यक्ति एवं उद्यम",
    equality: "समानता (Equality)",
    equalitySub: "प्रतिष्ठा एवं अवसर",
    fraternity: "बंधुता (Fraternity)",
    fraternitySub: "गरिमा एवं सामाजिक सुरक्षा",
    filterActive: "स्तंभ अनुसार फ़िल्टर"
}
  , Ig = {
    title: "अपने बारे में बताएं",
    subtitle: "दो मिनट से भी कम समय लगता है। आप किसी भी प्रश्न को छोड़ सकते हैं।",
    qAge: "आपकी आयु कितनी है?",
    qAgeHint: "पूर्ण वर्षों में (0 - 120)",
    qGender: "आपका लिंग क्या है?",
    female: "महिला",
    male: "पुरुष",
    other: "अन्य",
    preferNot: "बताना नहीं चाहते",
    qState: "आप किस राज्य या केंद्र शासित प्रदेश में रहते हैं?",
    selectState: "राज्य / केंद्र शासित प्रदेश चुनें",
    qResidence: "आपका निवास स्थान कहाँ है?",
    rural: "गाँव (ग्रामीण)",
    urban: "शहर / कस्बा (शहरी)",
    qIncome: "पूरे परिवार की वार्षिक आय (लाख ₹ में)",
    incomeHint: "परिवार के सभी सदस्यों की कुल वार्षिक आय ₹ लाख में",
    qOccupation: "आपका व्यवसाय / पेशा क्या है?",
    farmer: "किसान / खेती",
    student: "छात्र / विद्यार्थी",
    artisan: "पारंपरिक कारीगर / शिल्पकार",
    street_vendor: "पटरी विक्रेता / फेरीवाला",
    self_employed: "स्वरोजगार / छोटा व्यवसाय",
    salaried: "वेतनभोगी / निजी कर्मचारी",
    unemployed: "वर्तमान में बेरोजगार",
    homemaker: "गृहिणी",
    retired: "वरिष्ठ नागरिक / सेवानिवृत्त",
    next: "अगला",
    back: "पीछे",
    skip: "अभी छोड़ें",
    showSchemes: "मेरी योजनाएं दिखाएं",
    coreProgress: "प्रश्न {{current}} / 6",
    refineTitle: "परिणाम और बेहतर बनाएं",
    refineDesc: "सटीक योजनाओं के लिए इन वैकल्पिक प्रश्नों के उत्तर दें"
}
  , Fg = {
    category: "सामाजिक वर्ग",
    categoryHint: "सामान्य / ओबीसी / एससी / एसटी",
    bpl: "क्या आपके पास बीपीएल या राशन कार्ड है?",
    bplYes: "हाँ (बीपीएल / अंत्योदय)",
    bplNo: "नहीं (एपीएल / सामान्य)",
    land: "क्या आपके पास कृषि भूमि का स्वामित्व है?",
    landYes: "हाँ, जमीन मेरे नाम है",
    landNo: "जमीन नहीं है",
    bank: "क्या आपका सक्रिय बैंक खाता है?",
    bankYes: "हाँ, चालू खाता है",
    bankNo: "अभी बैंक खाता नहीं है",
    pregnant: "क्या आप गर्भवती हैं या शिशु को स्तनपान करा रही हैं?",
    pregnantYes: "हाँ",
    pregnantNo: "नहीं",
    daughter: "क्या आपकी 10 वर्ष से कम उम्र की बेटी है?",
    daughterYes: "हाँ",
    daughterNo: "नहीं",
    taxpayer: "क्या आप या परिवार आयकर (Income Tax) भरते हैं?",
    taxpayerYes: "हाँ, आयकर दाता",
    taxpayerNo: "नहीं, करदाता नहीं हैं"
}
  , Ug = {
    eligible: "पात्र",
    almost: "लगभग पात्र",
    possible: "शायद पात्र",
    not_eligible: "पात्र नहीं"
}
  , Bg = {
    eligible: "आप सभी सूचीबद्ध पात्रता शर्तों को पूरा करते प्रतीत होते हैं।",
    almost: "आप पात्रता के बहुत करीब हैं। मामूली अंतर या आसानी से पूरी होने वाली शर्तें देखें।",
    possible: "यह जानने के लिए 1-2 और प्रश्नों के उत्तर दें कि आप पात्र हैं या नहीं।",
    not_eligible: "वर्तमान में आप एक या अधिक शर्तें पूरी नहीं करते हैं। नीचे कारण देखें।"
}
  , Vg = {
    relevanceScore: "प्रासंगिकता स्कोर",
    benefits: "मुख्य लाभ",
    documents: "आवश्यक दस्तावेज",
    steps: "आवेदन प्रक्रिया के चरण",
    source: "आधिकारिक दिशानिर्देश एवं स्रोत",
    lastVerified: "सत्यापन तिथि",
    applyNow: "आधिकारिक पोर्टल पर आवेदन करें",
    save: "योजना सहेजें",
    saved: "सहेजी गई ★",
    printChecklist: "दस्तावेज चेकलिस्ट प्रिंट करें",
    whyNotTitle: "आप पात्र क्यों नहीं हुए?",
    nearMissTitle: "समीप चूक अंतर एवं उपाय",
    scoreBreakdown: "यह रैंक क्यों मिली?",
    articles: "संबंधित संवैधानिक अनुच्छेद"
}
  , Hg = {
    "r.needFarmer": "व्यवसाय किसान या कृषक होना आवश्यक है।",
    "r.needLand": "कृषि योग्य भूमि का स्वामित्व आवश्यक है।",
    "r.noTaxpayer": "आवेदक का आयकर दाता न होना आवश्यक है।",
    "r.needBpl": "परिवार के पास बीपीएल या एसईसीसी मान्यता प्राप्त कार्ड होना चाहिए।",
    "r.needSenior70": "आयु 70 वर्ष या उससे अधिक होनी चाहिए।",
    "r.needFemale": "यह योजना केवल महिला आवेदकों के लिए आरक्षित है।",
    "r.needAge18": "आवेदक की आयु कम से कम 18 वर्ष होनी चाहिए।",
    "r.age18to40": "आवेदक की आयु 18 से 40 वर्ष के बीच होनी चाहिए।",
    "r.needBank": "सक्रिय बचत बैंक खाता होना आवश्यक है।",
    "r.needAge60": "आवेदक की आयु 60 वर्ष या अधिक होनी चाहिए।",
    "r.needPregnantOrNursing": "आवेदक का गर्भवती महिला या स्तनपान कराने वाली माता होना आवश्यक है।",
    "r.needDaughterUnder10": "10 वर्ष से कम आयु की बालिका का होना आवश्यक है।",
    "r.needArtisan": "आवेदक का 18 पारंपरिक व्यवसायों में से एक में कारीगर होना चाहिए।",
    "r.needStudent": "आवेदक का नियमित अध्ययनरत छात्र होना आवश्यक है।",
    "r.needSC": "अनुसूचित जाति (SC) वर्ग के लिए आरक्षित।",
    "r.incomeMax25": "पारिवारिक वार्षिक आय ₹2.5 लाख से अधिक नहीं होनी चाहिए।",
    "r.needSCorST": "लाभार्थी अनुसूचित जाति (SC) या अनुसूचित जनजाति (ST) से होना चाहिए।",
    "r.needFemaleOrSCST": "आवेदक का महिला या एससी/एसटी वर्ग से होना आवश्यक है।"
}
  , Kg = {
    "fix.needBank": "किसी भी बैंक में जाकर शून्य-शेष पीएम जन धन बैंक खाता खोलें।",
    "fix.incomeMax25": "आपकी आय ₹2.5 लाख की सीमा के बहुत करीब है; कुछ प्रमाणित कटौतियों की जांच करें।",
    "fix.needAge60": "60 वर्ष की आयु पूर्ण होते ही आप स्वतः पात्र हो जाएंगे।",
    "fix.needAge18": "18 वर्ष की आयु पूर्ण होते ही आप आवेदन कर सकते हैं।",
    "fix.age18to40": "प्रवेश के समय आयु 18-40 वर्ष के बीच होनी चाहिए।",
    "fix.needSenior70": "70 वर्ष पूर्ण करने वाले वरिष्ठ नागरिक स्वतः पात्र होंगे।"
}
  , Wg = {
    heading: "गोपनीयता एवं डेटा सुरक्षा गारंटी",
    lead: "योजना सेतु डिजिटल व्यक्तिगत डेटा संरक्षण (DPDP) सिद्धांतों के तहत पूर्णतः सुरक्षित है।",
    rule1Title: "उत्तरों का शून्य भंडारण",
    rule1Desc: "आपके किसी भी व्यक्तिगत उत्तर (आयु, आय, जाति, परिवार) को कभी हमारे सर्वर पर नहीं भेजा जाता और न ही डेटाबेस में रखा जाता है।",
    rule2Title: "ब्राउज़र में स्थानीय गणना",
    rule2Desc: "संपूर्ण पात्रता इंजन आपके ब्राउज़र की मेमोरी में चलता है। टैब बंद करते ही सारा डेटा तुरंत मिट जाता है।",
    rule3Title: "वैकल्पिक पासवर्ड-रहित लॉगिन",
    rule3Desc: "योजना खोजने या दस्तावेज सूची के लिए लॉगिन की बिल्कुल आवश्यकता नहीं है। केवल सहेजी गई सूची रखने के लिए 6-अंकों का ईमेल ओटीपी उपयोग होता है।",
    rule4Title: "डेटा मिटाने का अधिकार",
    rule4Desc: "आप एक क्लिक में अपने सभी उत्तर या सहेजी गई योजनाओं को तुरंत हटा सकते हैं।",
    wipeShortlist: "मेरी सहेजी गई योजनाएं मिटाएं",
    wipeAnswers: "अभी सभी उत्तर साफ़ करें"
}
  , qg = {
    app: Mg,
    nav: Ag,
    hero: Dg,
    pillars: $g,
    wizard: Ig,
    refine: Fg,
    status: Ug,
    statusDesc: Bg,
    scheme: Vg,
    reasons: Hg,
    fixes: Kg,
    privacy: Wg
}
  , Yg = {
    title: "योजना सेतू",
    subtitle: "शासकीय योजना शोधक आणि अर्ज मार्गदर्शक",
    tagline: "स्वतःची ओळख न सांगता अवघ्या २ मिनिटांत जाणून घ्या तुम्ही कोणत्या योजनांसाठी पात्र आहात.",
    privacyBadge: "तुमची उत्तरे याच डिव्हाइसवर सुरक्षित राहतात",
    disclaimer: "स्वतंत्र जनसेवा साधन. भारत सरकारचे अधिकृत संकेतस्थळ नाही. अधिकृत पोर्टलवर माहितीची खात्री करा."
}
  , Qg = {
    home: "मुख्यपृष्ठ",
    finder: "योजना शोधा",
    results: "योजना",
    shortlist: "जतन केलेली यादी",
    privacy: "गोपनीयता हमी",
    about: "संविधान व माहिती",
    login: "साइन इन (पर्यायी)",
    logout: "लॉग आउट",
    guest: "अतिथी मोड",
    clearAnswers: "माझी उत्तरे पुसून टाका"
}
  , Gg = {
    heading: "तुम्ही कोणत्या शासकीय योजनांसाठी पात्र आहात ते शोधा",
    subheading: "तुमच्या भाषेत ६ सोप्या प्रश्नांची उत्तरे द्या. पात्र योजना, आवश्यक कागदपत्रे, कारणे आणि जवळजवळ पात्र असलेल्या योजना जाणून घ्या.",
    cta: "सुरू करा — सुमारे २ मिनिटे",
    continue: "तपासणी सुरू ठेवा",
    howItWorks: "हे कसे कार्य करते",
    step1: "१. सोप्या प्रश्नांची उत्तरे द्या",
    step2: "२. क्रमवारीनुसार योजना पहा",
    step3: "३. योग्य कागदपत्रे सोबत ठेवा",
    privacyGuarantee: "कोणतीही वैयक्तिक माहिती सर्व्हरवर पाठवली जात नाही. तुमची उत्तरे फक्त तुमच्या ब्राउझरमध्ये राहतात."
}
  , Jg = {
    title: "संवैधानिक स्तंभ",
    subtitle: "भारतीय संविधानाच्या उद्देशिकेतील मूल्यांवर आधारित योजना",
    all: "सर्व योजना",
    justice: "न्याय (Justice)",
    justiceSub: "सामाजिक, आर्थिक आणि राजकीय",
    liberty: "स्वातंत्र्य (Liberty)",
    libertySub: "विचार, अभिव्यक्ती आणि उद्योग",
    equality: "समता (Equality)",
    equalitySub: "दर्जा व संधीची समानता",
    fraternity: "बंधुता (Fraternity)",
    fraternitySub: "व्यक्तीची प्रतिष्ठा व सामाजिक सुरक्षा",
    filterActive: "स्तंभानुसार फिल्टर"
}
  , Xg = {
    title: "आपल्याबद्दल थोडी माहिती द्या",
    subtitle: "दोन मिनिटांपेक्षा कमी वेळ लागतो. आपण कोणताही प्रश्न वगळू शकता.",
    qAge: "आपले वय किती आहे?",
    qAgeHint: "पूर्ण झालेली वर्षे (0 - 120)",
    qGender: "आपले लिंग कोणते?",
    female: "महिला",
    male: "पुरुष",
    other: "इतर",
    preferNot: "सांगू इच्छित नाही",
    qState: "आपण कोणत्या राज्यात किंवा केंद्रशासित प्रदेशात राहता?",
    selectState: "राज्य / केंद्रशासित प्रदेश निवडा",
    qResidence: "आपले राहण्याचे ठिकाण कोणते आहे?",
    rural: "गाव (ग्रामीण)",
    urban: "शहर (नागरी)",
    qIncome: "कुटुंबाचे एकूण वार्षिक उत्पन्न (लाख ₹ मध्ये)",
    incomeHint: "कुटुंबातील सर्व सदस्यांचे मिळून वार्षिक उत्पन्न ₹ लाखात",
    qOccupation: "आपला व्यवसाय / कार्यक्षेत्र काय आहे?",
    farmer: "शेतकरी / कृषी",
    student: "विद्यार्थी",
    artisan: "पारंपारिक कारागीर / शिल्पकार",
    street_vendor: "फेरीवाला / लहान दुकानदार",
    self_employed: "स्वयंरोजगार / व्यवसाय",
    salaried: "वेतनधारक / नोकरदार",
    unemployed: "सध्या बेरोजगार",
    homemaker: "गृहिणी",
    retired: "ज्येष्ठ नागरिक / सेवानिवृत्त",
    next: "पुढे",
    back: "मागे",
    skip: "सध्या वगळा",
    showSchemes: "माझ्या योजना दाखवा",
    coreProgress: "प्रश्न {{current}} / ६",
    refineTitle: "निकाल अधिक अचूक करा",
    refineDesc: "अधिक नेमक्या योजनांसाठी या पर्यायी प्रश्नांची उत्तरे द्या"
}
  , Zg = {
    category: "सामाजिक प्रवर्ग",
    categoryHint: "खुला / ओबीसी / एससी / एसटी",
    bpl: "आपल्याकडे पिवळे/केशरी बीपीएल रेशन कार्ड आहे का?",
    bplYes: "होय (बीपीएल / अंत्योदय)",
    bplNo: "नाही (नियमित रेशन कार्ड)",
    land: "आपल्या मालकीची शेतजमीन आहे का?",
    landYes: "होय, स्वतःच्या नावावर जमीन आहे",
    landNo: "जमीन नाही",
    bank: "आपले चालू बँक खाते आहे का?",
    bankYes: "होय, बँक खाते सक्रिय आहे",
    bankNo: "अद्याप बँक खाते नाही",
    pregnant: "आपण गरोदर आहात किंवा स्तनदा माता आहात का?",
    pregnantYes: "होय",
    pregnantNo: "नाही",
    daughter: "आपल्याला १० वर्षांखालील मुलगी आहे का?",
    daughterYes: "होय",
    daughterNo: "नाही",
    taxpayer: "आपण किंवा आपले कुटुंब आयकर (Income Tax) भरते का?",
    taxpayerYes: "होय, आयकर भरतो",
    taxpayerNo: "नाही, आयकर भरत नाही"
}
  , e0 = {
    eligible: "पात्र",
    almost: "जवळजवळ पात्र",
    possible: "कदाचित पात्र",
    not_eligible: "पात्र नाही"
}
  , t0 = {
    eligible: "आपण सर्व निकष पूर्ण करत आहात.",
    almost: "आपण पात्रतेच्या अगदी जवळ आहात. थोडे अंतर किंवा सोप्या अटी पहा.",
    possible: "आपण पात्र आहात की नाही हे निश्चित करण्यासाठी आणखी १-२ प्रश्नांची उत्तरे द्या.",
    not_eligible: "सध्या आपण एक किंवा अधिक अटी पूर्ण करत नाही. खालील कारणे पहा."
}
  , n0 = {
    relevanceScore: "सुसंगतता गुण",
    benefits: "योजनेचे मुख्य फायदे",
    documents: "आवश्यक कागदपत्रे",
    steps: "अर्ज करण्याची पद्धत",
    source: "अधिकृत मार्गदर्शक व स्रोत",
    lastVerified: "पडताळणी तारीख",
    applyNow: "अधिकृत पोर्टलवर अर्ज करा",
    save: "योजना जतन करा",
    saved: "जतन केली ★",
    printChecklist: "कागदपत्र चेकलिस्ट प्रिंट करा",
    whyNotTitle: "आपण अपात्र का ठरलात?",
    nearMissTitle: "जवळपासचे अंतर आणि उपाय",
    scoreBreakdown: "हा क्रमांक का मिळाला?",
    articles: "संबंधित घटनात्मक कलमे"
}
  , r0 = {
    "r.needFarmer": "व्यवसाय शेतकरी असणे आवश्यक आहे.",
    "r.needLand": "लागवडीयोग्य शेतजमिनीची मालकी आवश्यक आहे.",
    "r.noTaxpayer": "अर्जदार आयकर भरणारा नसावा.",
    "r.needBpl": "कुटुंबाकडे बीपीएल किंवा अंत्योदय रेशन कार्ड असणे आवश्यक आहे.",
    "r.needSenior70": "वय ७० वर्षे किंवा त्याहून अधिक असणे आवश्यक आहे.",
    "r.needFemale": "ही योजना केवळ महिला अर्जदारांसाठी राखीव आहे.",
    "r.needAge18": "अर्जदाराचे वय किमान १८ वर्षे असावे.",
    "r.age18to40": "अर्जदाराचे वय १८ ते ४० वर्षांच्या दरम्यान असणे आवश्यक आहे.",
    "r.needBank": "सक्रिय बचत बँक खाते असणे आवश्यक आहे.",
    "r.needAge60": "अर्जदाराचे वय ६० वर्षे किंवा त्याहून अधिक असावे.",
    "r.needPregnantOrNursing": "अर्जदार गरोदर स्त्री किंवा स्तनदा माता असणे आवश्यक आहे.",
    "r.needDaughterUnder10": "१० वर्षांखालील मुलगी असणे आवश्यक आहे.",
    "r.needArtisan": "१८ पारंपारिक व्यवसायांपैकी एकातील कारागीर असणे आवश्यक आहे.",
    "r.needStudent": "अर्जदार नियमित शिक्षण घेणारा विद्यार्थी असावा.",
    "r.needSC": "अनुसूचित जाती (SC) प्रवर्गासाठी राखीव.",
    "r.incomeMax25": "कौटुंबिक वार्षिक उत्पन्न ₹२.५ लाखांपेक्षा जास्त नसावे.",
    "r.needSCorST": "लाभार्थी अनुसूचित जाती (SC) किंवा जमाती (ST) मधील असावा.",
    "r.needFemaleOrSCST": "अर्जदार महिला किंवा अनुसूचित जाती/जमातीतील असावी."
}
  , s0 = {
    "fix.needBank": "कोणत्याही बँकेत जाऊन शून्य रकमेचे पीएम जन धन बँक खाते उघडा.",
    "fix.incomeMax25": "आपले उत्पन्न ₹२.५ लाखांच्या मर्यादेजवळ आहे; अधिकृत सवलतींची तपासणी करा.",
    "fix.needAge60": "वय ६० वर्षे पूर्ण होताच आपण आपोआप पात्र व्हाल.",
    "fix.needAge18": "वय १८ वर्षे पूर्ण होताच आपण अर्ज करू शकता.",
    "fix.age18to40": "प्रवेशाच्या वेळी वय १८-४० वर्षांच्या दरम्यान असणे आवश्यक आहे.",
    "fix.needSenior70": "७० वर्षे पूर्ण करणारे ज्येष्ठ नागरिक त्वरित पात्र ठरतील."
}
  , l0 = {
    heading: "गोपनीयता आणि डेटा संरक्षण हमी",
    lead: "योजना सेतू डिजिटल वैयक्तिक डेटा संरक्षण (DPDP) नियमांनुसार पूर्ण सुरक्षित आहे.",
    rule1Title: "उत्तरांची शून्य साठवणूक",
    rule1Desc: "आपली कोणतीही वैयक्तिक उत्तरे (वय, उत्पन्न, जात, कुटुंब) कधीही आमच्या सर्व्हरवर किंवा डेटाबेसमध्ये जतन केली जात नाहीत.",
    rule2Title: "ब्राउझरमध्येच स्थानिक प्रक्रिया",
    rule2Desc: "संपूर्ण पात्रता तपासणी आपल्या फोन किंवा संगणकाच्या मेमरीमध्येच होते. टॅब बंद करताच सर्व माहिती नष्ट होते.",
    rule3Title: "पर्यायी पासवर्ड-मुक्त लॉगिन",
    rule3Desc: "योजना पाहण्यासाठी किंवा कागदपत्रे तपासण्यासाठी लॉगिनची गरज नाही. केवळ योजना सेव्ह करण्यासाठी ६-अंकी ईमेल ओटीपी वापरला जातो.",
    rule4Title: "डेटा नष्ट करण्याचा अधिकार",
    rule4Desc: "आपण एका क्लिकवर आपले सर्व उत्तरे किंवा सेव्ह केलेल्या योजना कायमच्या हटवू शकता.",
    wipeShortlist: "माझ्या जतन केलेल्या योजना हटवा",
    wipeAnswers: "आत्ताच सर्व उत्तरे पुसून टाका"
}
  , i0 = {
    app: Yg,
    nav: Qg,
    hero: Gg,
    pillars: Jg,
    wizard: Xg,
    refine: Zg,
    status: e0,
    statusDesc: t0,
    scheme: n0,
    reasons: r0,
    fixes: s0,
    privacy: l0
}
  , a0 = typeof window < "u" && localStorage.getItem("yojana_lang") || "en";
He.use(Zm).init({
    resources: {
        en: {
            translation: zg
        },
        hi: {
            translation: qg
        },
        mr: {
            translation: i0
        }
    },
    lng: a0,
    fallbackLng: "en",
    interpolation: {
        escapeValue: !1
    }
});
const o0 = i => {
    He.changeLanguage(i),
    typeof window < "u" && (localStorage.setItem("yojana_lang", i),
    document.documentElement.lang = i)
}
  , gd = i => {
    let s;
    const l = new Set
      , u = (x, b) => {
        const w = typeof x == "function" ? x(s) : x;
        if (!Object.is(w, s)) {
            const v = s;
            s = b ?? (typeof w != "object" || w === null) ? w : Object.assign({}, s, w),
            l.forEach(R => R(s, v))
        }
    }
      , d = () => s
      , g = {
        setState: u,
        getState: d,
        getInitialState: () => m,
        subscribe: x => (l.add(x),
        () => l.delete(x))
    }
      , m = s = i(u, d, g);
    return g
}
  , u0 = (i => i ? gd(i) : gd)
  , c0 = i => i;
function d0(i, s=c0) {
    const l = tr.useSyncExternalStore(i.subscribe, tr.useCallback( () => s(i.getState()), [i, s]), tr.useCallback( () => s(i.getInitialState()), [i, s]));
    return tr.useDebugValue(l),
    l
}
const xd = i => {
    const s = u0(i)
      , l = u => d0(s, u);
    return Object.assign(l, s),
    l
}
  , Bd = (i => i ? xd(i) : xd)
  , f0 = {}
  , _t = Bd(i => ({
    profile: f0,
    hasStarted: !1,
    selectedPillars: [],
    consentAccepted: !1,
    searchQuery: "",
    setProfileField: (s, l) => i(u => ({
        profile: {
            ...u.profile,
            [s]: l
        }
    })),
    updateProfile: s => i(l => ({
        profile: {
            ...l.profile,
            ...s
        }
    })),
    resetProfile: () => i({
        profile: {},
        hasStarted: !1,
        selectedPillars: [],
        searchQuery: ""
    }),
    setHasStarted: s => i({
        hasStarted: s
    }),
    togglePillar: s => i(l => ({
        selectedPillars: l.selectedPillars.includes(s) ? l.selectedPillars.filter(d => d !== s) : [...l.selectedPillars, s]
    })),
    clearPillars: () => i({
        selectedPillars: []
    }),
    setConsentAccepted: s => i({
        consentAccepted: s
    }),
    setSearchQuery: s => i({
        searchQuery: s
    })
}));
typeof window < "u" && window.addEventListener("pagehide", () => {
    _t.getState().resetProfile()
}
);
const un = Bd( (i, s) => ({
    status: "guest",
    userEmail: null,
    userId: null,
    shortlist: [],
    isLoading: !1,
    errorMessage: null,
    initAuth: async () => {}
    ,
    requestOtp: async l => (i({
        isLoading: !0,
        errorMessage: null
    }),
    i({
        isLoading: !1,
        status: "otp_sent",
        userEmail: l
    }),
    !0),
    verifyOtp: async l => {
        const {userEmail: u} = s();
        return u ? (i({
            isLoading: !0,
            errorMessage: null
        }),
        l.length === 6 ? (i({
            isLoading: !1,
            status: "authenticated",
            userId: "mock-user-123"
        }),
        !0) : (i({
            isLoading: !1,
            errorMessage: "Invalid 6-digit code. For demo, enter 123456."
        }),
        !1)) : !1
    }
    ,
    signOut: async () => {
        i({
            status: "guest",
            userEmail: null,
            userId: null,
            shortlist: []
        })
    }
    ,
    toggleShortlist: async l => {
        const {shortlist: u, userId: d} = s()
          , h = u.includes(l) ? u.filter(g => g !== l) : [...u, l];
        i({
            shortlist: h
        })
    }
    ,
    deleteMyData: async () => (i({
        isLoading: !0
    }),
    i({
        shortlist: [],
        isLoading: !1
    }),
    !0),
    clearError: () => i({
        errorMessage: null
    })
}));
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const p0 = i => i == null ? void 0 : i.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase();
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
function h0(i, s, l=[]) {
    if (s == null)
        throw new Error("[lucide]: iconNode is required when icon name is used");
    return {
        name: p0(i),
        size: 24,
        node: s,
        ...l.length > 0 ? {
            aliases: l
        } : {}
    }
}
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const m0 = i => {
    let s = ""
      , l = !1;
    for (const u of i) {
        if (u === "-" || u === "_" || u <= " ") {
            l = s.length > 0;
            continue
        }
        s.length === 0 ? s += u.toLowerCase() : s += l ? u.toUpperCase() : u,
        l = !1
    }
    return s
}
;
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const g0 = i => {
    const s = m0(i);
    return s.charAt(0).toUpperCase() + s.slice(1)
}
;
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const _a = (...i) => i.filter( (s, l, u) => !!s && s.trim() !== "" && u.indexOf(s) === l).join(" ").trim();
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const kn = {
    xmlns: "http://www.w3.org/2000/svg",
    width: 24,
    height: 24,
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    "stroke-width": 2,
    "stroke-linecap": "round",
    "stroke-linejoin": "round"
};
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
function Na(i) {
    return i != null
}
function x0(i, s={}) {
    var v, R;
    const l = s.attributeNames ?? {}
      , u = E => l[E] ?? E
      , d = i.size ?? i.width ?? kn.width
      , f = i.size ?? i.height ?? kn.height
      , h = ((v = i.aliases) == null ? void 0 : v.filter(E => typeof E == "string" && E.trim() !== "").map(E => `lucide-${E}`)) ?? []
      , g = [...i.name ? [`lucide-${i.name}`] : [], ...h]
      , m = ((R = s.className) == null ? void 0 : R.split(" ").filter(Boolean)) ?? []
      , x = s.includeDefaultClasses === !1 ? _a(...m) : _a("lucide", ...g, ...m)
      , b = s.absoluteStrokeWidth ? Number(s.strokeWidth ?? kn["stroke-width"]) * Number(i.size ?? i.width ?? kn.width) / Number(s.size ?? s.width ?? kn.width) : s.strokeWidth ?? kn["stroke-width"];
    return ["svg", {
        ...Object.entries(kn).reduce( (E, [_,P]) => (E[u(_)] = P,
        E), {}),
        ..."color" in s && s.color && {
            [u("stroke")]: s.color
        },
        ..."size" in s && Na(s.size) && {
            [u("width")]: s.size,
            [u("height")]: s.size
        },
        ..."width" in s && Na(s.width) && {
            [u("width")]: s.width
        },
        ..."height" in s && Na(s.height) && {
            [u("height")]: s.height
        },
        [u("stroke-width")]: b,
        ...x && {
            [u("class")]: x
        },
        [u("viewBox")]: `0 0 ${d} ${f}`,
        ...s.hasA11yProp === !1 ? {
            [u("aria-hidden")]: "true"
        } : {},
        ..."attributes" in s && s.attributes
    }, i.node.map(E => {
        const [_,P,$] = E
          , I = s.nonScalingStroke ? {
            [u("vector-effect")]: "non-scaling-stroke",
            ...P
        } : P;
        return $ ? [_, I, $] : [_, I]
    }
    )]
}
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
function y0(i, s={}) {
    return x0(i, {
        ...s,
        attributeNames: {
            ...s.attributeNames,
            class: "className",
            "stroke-width": "strokeWidth",
            "stroke-linecap": "strokeLinecap",
            "stroke-linejoin": "strokeLinejoin",
            "vector-effect": "vectorEffect"
        }
    })
}
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const v0 = i => {
    for (const s in i)
        if (s.startsWith("aria-") || s === "role" || s === "title")
            return !0;
    return !1
}
  , w0 = O.createContext({})
  , b0 = () => O.useContext(w0)
  , N0 = O.forwardRef( ({color: i, size: s, width: l, height: u, strokeWidth: d, absoluteStrokeWidth: f, nonScalingStroke: h, className: g="", children: m, iconNode: x=[], icon: b={
    node: x,
    aliases: [],
    size: 24
}, ...w}, v) => {
    const {size: R=24, strokeWidth: E=2, absoluteStrokeWidth: _=!1, nonScalingStroke: P=!1, color: $="currentColor", className: I=""} = b0() ?? {}
      , V = !!m || v0(w)
      , [H,se,K=[]] = y0(b, {
        color: i ?? $,
        width: l ?? s ?? R,
        height: u ?? s ?? R,
        strokeWidth: d ?? E,
        absoluteStrokeWidth: f ?? _,
        nonScalingStroke: h ?? P,
        className: _a(I, g),
        hasA11yProp: V,
        attributes: w
    });
    return O.createElement(H, {
        ref: v,
        ...se
    }, [...K.map( ([te,ee]) => O.createElement(te, ee)), ...Array.isArray(m) ? m : [m]])
}
);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
function oe(i, s=[], l=[]) {
    const u = typeof i == "string" ? h0(i, s, l) : i
      , d = O.forwardRef( ({className: f, ...h}, g) => O.createElement(N0, {
        ref: g,
        icon: u,
        className: f,
        ...h
    }));
    return u.name && (d.displayName = g0(u.name)),
    d
}
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Vd = {
    name: "arrow-left",
    size: 24,
    node: [["path", {
        d: "m12 19-7-7 7-7",
        key: "1l729n"
    }], ["path", {
        d: "M19 12H5",
        key: "x3x0zl"
    }]]
};
Vd.node;
const Ra = oe(Vd);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Hd = {
    name: "arrow-right",
    size: 24,
    node: [["path", {
        d: "M5 12h14",
        key: "1ays0h"
    }], ["path", {
        d: "m12 5 7 7-7 7",
        key: "xquz4c"
    }]]
};
Hd.node;
const Cn = oe(Hd);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Kd = {
    name: "award",
    size: 24,
    node: [["path", {
        d: "m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526",
        key: "1yiouv"
    }], ["circle", {
        cx: "12",
        cy: "8",
        r: "6",
        key: "1vp47v"
    }]]
};
Kd.node;
const Wd = oe(Kd);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const qd = {
    name: "book-open",
    size: 24,
    node: [["path", {
        d: "M12 5v16",
        key: "1f6ucr"
    }], ["path", {
        d: "M20.001 19A2 2 0 0022 17V5a2 2 0 00-1.999-2L16 3.002A5 5 0 0012 5a5 5 0 00-4-2H4a2 2 0 00-2 2v12a2 2 0 001.999 2H8a5 5 0 014 2 5 5 0 014-2z",
        key: "1fyvmf"
    }]]
};
qd.node;
const Yd = oe(qd);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Qd = {
    name: "bookmark",
    size: 24,
    node: [["path", {
        d: "M17 3a2 2 0 0 1 2 2v15a1 1 0 0 1-1.496.868l-4.512-2.578a2 2 0 0 0-1.984 0l-4.512 2.578A1 1 0 0 1 5 20V5a2 2 0 0 1 2-2z",
        key: "oz39mx"
    }]]
};
Qd.node;
const Gr = oe(Qd);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Gd = {
    name: "calendar",
    size: 24,
    node: [["path", {
        d: "M8 2v3",
        key: "1ioesn"
    }], ["path", {
        d: "M16 2v3",
        key: "otl347"
    }], ["rect", {
        x: "3",
        y: "3",
        width: "18",
        height: "18",
        rx: "2",
        key: "h1oib"
    }], ["path", {
        d: "M3 9h18",
        key: "1pudct"
    }]]
};
Gd.node;
const Jd = oe(Gd);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Xd = {
    name: "check",
    size: 24,
    node: [["path", {
        d: "M20 6 9 17l-5-5",
        key: "1gmf2c"
    }]]
};
Xd.node;
const j0 = oe(Xd);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Zd = {
    name: "chevron-right",
    size: 24,
    node: [["path", {
        d: "m9 18 6-6-6-6",
        key: "mthhwq"
    }]]
};
Zd.node;
const k0 = oe(Zd);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const ef = {
    name: "circle-alert",
    size: 24,
    node: [["circle", {
        cx: "12",
        cy: "12",
        r: "10",
        key: "1mglay"
    }], ["line", {
        x1: "12",
        x2: "12",
        y1: "8",
        y2: "12",
        key: "1pkeuh"
    }], ["line", {
        x1: "12",
        x2: "12.01",
        y1: "16",
        y2: "16",
        key: "4dfq90"
    }]],
    aliases: ["alert-circle"]
};
ef.node;
const xl = oe(ef);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const tf = {
    name: "circle-check",
    size: 24,
    node: [["circle", {
        cx: "12",
        cy: "12",
        r: "10",
        key: "1mglay"
    }], ["path", {
        d: "m16 9-5.5 5.5L8 12",
        key: "xofnsj"
    }]],
    aliases: ["check-circle-2"]
};
tf.node;
const mt = oe(tf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const nf = {
    name: "circle-question-mark",
    size: 24,
    node: [["circle", {
        cx: "12",
        cy: "12",
        r: "10",
        key: "1mglay"
    }], ["path", {
        d: "M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3",
        key: "1u773s"
    }], ["path", {
        d: "M12 17h.01",
        key: "p32p05"
    }]],
    aliases: ["help-circle", "circle-help"]
};
nf.node;
const wl = oe(nf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const rf = {
    name: "clock",
    size: 24,
    node: [["circle", {
        cx: "12",
        cy: "12",
        r: "10",
        key: "1mglay"
    }], ["path", {
        d: "M12 6v6l4 2",
        key: "mmk7yg"
    }]]
};
rf.node;
const S0 = oe(rf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const sf = {
    name: "compass",
    size: 24,
    node: [["circle", {
        cx: "12",
        cy: "12",
        r: "10",
        key: "1mglay"
    }], ["path", {
        d: "m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z",
        key: "9ktpf1"
    }]]
};
sf.node;
const C0 = oe(sf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const lf = {
    name: "cpu",
    size: 24,
    node: [["path", {
        d: "M12 20v2",
        key: "1lh1kg"
    }], ["path", {
        d: "M12 2v2",
        key: "tus03m"
    }], ["path", {
        d: "M17 20v2",
        key: "1rnc9c"
    }], ["path", {
        d: "M17 2v2",
        key: "11trls"
    }], ["path", {
        d: "M2 12h2",
        key: "1t8f8n"
    }], ["path", {
        d: "M2 17h2",
        key: "7oei6x"
    }], ["path", {
        d: "M2 7h2",
        key: "asdhe0"
    }], ["path", {
        d: "M20 12h2",
        key: "1q8mjw"
    }], ["path", {
        d: "M20 17h2",
        key: "1fpfkl"
    }], ["path", {
        d: "M20 7h2",
        key: "1o8tra"
    }], ["path", {
        d: "M7 20v2",
        key: "4gnj0m"
    }], ["path", {
        d: "M7 2v2",
        key: "1i4yhu"
    }], ["rect", {
        x: "4",
        y: "4",
        width: "16",
        height: "16",
        rx: "2",
        key: "1vbyd7"
    }], ["rect", {
        x: "8",
        y: "8",
        width: "8",
        height: "8",
        rx: "1",
        key: "z9xiuo"
    }]]
};
lf.node;
const E0 = oe(lf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const af = {
    name: "external-link",
    size: 24,
    node: [["path", {
        d: "M15 3h6v6",
        key: "1q9fwt"
    }], ["path", {
        d: "M10 14 21 3",
        key: "gplh6r"
    }], ["path", {
        d: "M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6",
        key: "a6xqqp"
    }]]
};
af.node;
const Oa = oe(af);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const of = {
    name: "file-check-corner",
    size: 24,
    node: [["path", {
        d: "M10.5 22H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.706.706l3.588 3.588A2.4 2.4 0 0 1 20 8v6",
        key: "g5mvt7"
    }], ["path", {
        d: "M14 2v5a1 1 0 0 0 1 1h5",
        key: "wfsgrz"
    }], ["path", {
        d: "m14 20 2 2 4-4",
        key: "15kota"
    }]],
    aliases: ["file-check-2"]
};
of.node;
const P0 = oe(of);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const uf = {
    name: "file-text",
    size: 24,
    node: [["path", {
        d: "M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z",
        key: "1oefj6"
    }], ["path", {
        d: "M14 2v5a1 1 0 0 0 1 1h5",
        key: "wfsgrz"
    }], ["path", {
        d: "M10 9H8",
        key: "b1mrlr"
    }], ["path", {
        d: "M16 13H8",
        key: "t4e002"
    }], ["path", {
        d: "M16 17H8",
        key: "z1uh3a"
    }]]
};
uf.node;
const Ta = oe(uf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const cf = {
    name: "globe",
    size: 24,
    node: [["circle", {
        cx: "12",
        cy: "12",
        r: "10",
        key: "1mglay"
    }], ["path", {
        d: "M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20",
        key: "13o1zl"
    }], ["path", {
        d: "M2 12h20",
        key: "9i4pu4"
    }]]
};
cf.node;
const L0 = oe(cf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const df = {
    name: "heart-handshake",
    size: 24,
    node: [["path", {
        d: "M19.414 14.414C21 12.828 22 11.5 22 9.5a5.5 5.5 0 0 0-9.591-3.676.6.6 0 0 1-.818.001A5.5 5.5 0 0 0 2 9.5c0 2.3 1.5 4 3 5.5l5.535 5.362a2 2 0 0 0 2.879.052 2.12 2.12 0 0 0-.004-3 2.124 2.124 0 1 0 3-3 2.124 2.124 0 0 0 3.004 0 2 2 0 0 0 0-2.828l-1.881-1.882a2.41 2.41 0 0 0-3.409 0l-1.71 1.71a2 2 0 0 1-2.828 0 2 2 0 0 1 0-2.828l2.823-2.762",
        key: "17lmqv"
    }]]
};
df.node;
const _0 = oe(df);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const ff = {
    name: "key-round",
    size: 24,
    node: [["path", {
        d: "M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z",
        key: "1s6t7t"
    }], ["circle", {
        cx: "16.5",
        cy: "7.5",
        r: ".5",
        fill: "currentColor",
        key: "w0ekpg"
    }]]
};
ff.node;
const R0 = oe(ff);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const pf = {
    name: "layers",
    size: 24,
    node: [["path", {
        d: "M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z",
        key: "zw3jo"
    }], ["path", {
        d: "M2 12a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 12",
        key: "1wduqc"
    }], ["path", {
        d: "M2 17a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 17",
        key: "kqbvx6"
    }]],
    aliases: ["layers-3"]
};
pf.node;
const O0 = oe(pf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const hf = {
    name: "list-ordered",
    size: 24,
    node: [["path", {
        d: "M11 5h10",
        key: "1cz7ny"
    }], ["path", {
        d: "M11 12h10",
        key: "1438ji"
    }], ["path", {
        d: "M11 19h10",
        key: "11t30w"
    }], ["path", {
        d: "M4 4h1v5",
        key: "10yrso"
    }], ["path", {
        d: "M4 9h2",
        key: "r1h2o0"
    }], ["path", {
        d: "M6.5 20H3.4c0-1 2.6-1.925 2.6-3.5a1.5 1.5 0 0 0-2.6-1.02",
        key: "xtkcd5"
    }]]
};
hf.node;
const yd = oe(hf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const mf = {
    name: "lock",
    size: 24,
    node: [["rect", {
        width: "18",
        height: "11",
        x: "3",
        y: "11",
        rx: "2",
        ry: "2",
        key: "1w4ew1"
    }], ["path", {
        d: "M7 11V7a5 5 0 0 1 10 0v4",
        key: "fwvmzm"
    }]]
};
mf.node;
const Ia = oe(mf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const gf = {
    name: "mail",
    size: 24,
    node: [["path", {
        d: "m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7",
        key: "132q7q"
    }], ["rect", {
        x: "2",
        y: "4",
        width: "20",
        height: "16",
        rx: "2",
        key: "izxlao"
    }]]
};
gf.node;
const vd = oe(gf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const xf = {
    name: "pen-line",
    size: 24,
    node: [["path", {
        d: "M13 21h8",
        key: "1jsn5i"
    }], ["path", {
        d: "M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z",
        key: "1a8usu"
    }]],
    aliases: ["edit-3"]
};
xf.node;
const T0 = oe(xf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const yf = {
    name: "printer",
    size: 24,
    node: [["path", {
        d: "M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2",
        key: "143wyd"
    }], ["path", {
        d: "M6 9V3a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v6",
        key: "1itne7"
    }], ["rect", {
        x: "6",
        y: "14",
        width: "12",
        height: "8",
        rx: "1",
        key: "1ue0tg"
    }]]
};
yf.node;
const vf = oe(yf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const wf = {
    name: "rotate-ccw",
    size: 24,
    node: [["path", {
        d: "M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8",
        key: "1357e3"
    }], ["path", {
        d: "M3 3v5h5",
        key: "1xhq8a"
    }]]
};
wf.node;
const Fa = oe(wf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const bf = {
    name: "scale",
    size: 24,
    node: [["path", {
        d: "M12 3v18",
        key: "108xh3"
    }], ["path", {
        d: "m19 8 3 8a5 5 0 0 1-6 0zV7",
        key: "zcdpyk"
    }], ["path", {
        d: "M3 7h1a17 17 0 0 0 8-2 17 17 0 0 0 8 2h1",
        key: "1yorad"
    }], ["path", {
        d: "m5 8 3 8a5 5 0 0 1-6 0zV7",
        key: "eua70x"
    }], ["path", {
        d: "M7 21h10",
        key: "1b0cd5"
    }]]
};
bf.node;
const Zr = oe(bf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Nf = {
    name: "search",
    size: 24,
    node: [["path", {
        d: "m21 21-4.34-4.34",
        key: "14j7rj"
    }], ["circle", {
        cx: "11",
        cy: "11",
        r: "8",
        key: "4ej97u"
    }]]
};
Nf.node;
const z0 = oe(Nf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const jf = {
    name: "shield-check",
    size: 24,
    node: [["path", {
        d: "M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z",
        key: "oel41y"
    }], ["path", {
        d: "m9 12 2 2 4-4",
        key: "dzmm74"
    }]]
};
jf.node;
const Lt = oe(jf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const kf = {
    name: "sliders-horizontal",
    size: 24,
    node: [["path", {
        d: "M10 5H3",
        key: "1qgfaw"
    }], ["path", {
        d: "M12 19H3",
        key: "yhmn1j"
    }], ["path", {
        d: "M14 3v4",
        key: "1sua03"
    }], ["path", {
        d: "M16 17v4",
        key: "1q0r14"
    }], ["path", {
        d: "M21 12h-9",
        key: "1o4lsq"
    }], ["path", {
        d: "M21 19h-5",
        key: "1rlt1p"
    }], ["path", {
        d: "M21 5h-7",
        key: "1oszz2"
    }], ["path", {
        d: "M8 10v4",
        key: "tgpxqk"
    }], ["path", {
        d: "M8 12H3",
        key: "a7s4jb"
    }]]
};
kf.node;
const M0 = oe(kf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Sf = {
    name: "sliders-vertical",
    size: 24,
    node: [["path", {
        d: "M10 8h4",
        key: "1sr2af"
    }], ["path", {
        d: "M12 21v-9",
        key: "17s77i"
    }], ["path", {
        d: "M12 8V3",
        key: "13r4qs"
    }], ["path", {
        d: "M17 16h4",
        key: "h1uq16"
    }], ["path", {
        d: "M19 12V3",
        key: "o1uvq1"
    }], ["path", {
        d: "M19 21v-5",
        key: "qua636"
    }], ["path", {
        d: "M3 14h4",
        key: "bcjad9"
    }], ["path", {
        d: "M5 10V3",
        key: "cb8scm"
    }], ["path", {
        d: "M5 21v-7",
        key: "1w1uti"
    }]],
    aliases: ["sliders"]
};
Sf.node;
const Cf = oe(Sf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Ef = {
    name: "sparkles",
    size: 24,
    node: [["path", {
        d: "M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z",
        key: "1s2grr"
    }], ["path", {
        d: "M20 2v4",
        key: "1rf3ol"
    }], ["path", {
        d: "M22 4h-4",
        key: "gwowj6"
    }], ["circle", {
        cx: "4",
        cy: "20",
        r: "2",
        key: "6kqj1y"
    }]],
    aliases: ["stars"]
};
Ef.node;
const an = oe(Ef);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Pf = {
    name: "trash",
    size: 24,
    node: [["path", {
        d: "M10 11v6",
        key: "nco0om"
    }], ["path", {
        d: "M14 11v6",
        key: "outv1u"
    }], ["path", {
        d: "M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6",
        key: "miytrc"
    }], ["path", {
        d: "M3 6h18",
        key: "d0wm0j"
    }], ["path", {
        d: "M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2",
        key: "e791ji"
    }]],
    aliases: ["trash-2"]
};
Pf.node;
const za = oe(Pf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Lf = {
    name: "triangle-alert",
    size: 24,
    node: [["path", {
        d: "m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3",
        key: "wmoenq"
    }], ["path", {
        d: "M12 9v4",
        key: "juzpu7"
    }], ["path", {
        d: "M12 17h.01",
        key: "p32p05"
    }]],
    aliases: ["alert-triangle"]
};
Lf.node;
const A0 = oe(Lf);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const _f = {
    name: "user-check",
    size: 24,
    node: [["path", {
        d: "m16 11 2 2 4-4",
        key: "9rsbq5"
    }], ["path", {
        d: "M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2",
        key: "1yyitq"
    }], ["circle", {
        cx: "9",
        cy: "7",
        r: "4",
        key: "nufk8"
    }]]
};
_f.node;
const D0 = oe(_f);
/**
 * @license lucide-react v1.51.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Rf = {
    name: "x",
    size: 24,
    node: [["path", {
        d: "M18 6 6 18",
        key: "1bl5f8"
    }], ["path", {
        d: "m6 6 12 12",
        key: "d8bk6v"
    }]]
};
Rf.node;
const Of = oe(Rf)
  , $0 = () => {
    const {t: i, i18n: s} = Je()
      , l = Xr()
      , {profile: u, resetProfile: d} = _t()
      , {status: f, shortlist: h, signOut: g} = un()
      , m = Object.values(u).some(w => w !== void 0 && w !== "")
      , x = w => {
        o0(w)
    }
      , b = () => {
        window.confirm("Clear all your answers from this device?") && d()
    }
    ;
    return a.jsxs("header", {
        className: "sticky top-0 z-40 bg-white/95 backdrop-blur border-b border-slate-200 shadow-sm",
        children: [a.jsxs("div", {
            className: "h-1.5 w-full flex",
            children: [a.jsx("div", {
                className: "flex-1 bg-orange-500"
            }), a.jsx("div", {
                className: "flex-1 bg-white border-y border-slate-200"
            }), a.jsx("div", {
                className: "flex-1 bg-green-600"
            })]
        }), a.jsxs("div", {
            className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between gap-4",
            children: [a.jsxs(Ue, {
                to: "/",
                className: "flex items-center gap-3 group",
                children: [a.jsx("div", {
                    className: "relative w-10 h-10 rounded-full bg-slate-900 border-2 border-orange-500 flex items-center justify-center p-1 text-white shadow group-hover:scale-105 transition-transform",
                    children: a.jsx(Zr, {
                        className: "w-5 h-5 text-orange-400"
                    })
                }), a.jsxs("div", {
                    children: [a.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [a.jsx("span", {
                            className: "font-extrabold text-xl tracking-tight text-slate-900",
                            children: i("app.title")
                        }), a.jsxs("span", {
                            className: "hidden md:inline-flex items-center gap-1 text-[11px] font-semibold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200",
                            children: [a.jsx(Lt, {
                                className: "w-3.5 h-3.5 text-emerald-600"
                            }), i("app.privacyBadge")]
                        })]
                    }), a.jsx("p", {
                        className: "text-xs text-slate-500 hidden sm:block",
                        children: i("app.subtitle")
                    })]
                })]
            }), a.jsxs("div", {
                className: "flex items-center gap-2 sm:gap-3",
                children: [m && a.jsxs("button", {
                    onClick: b,
                    title: i("nav.clearAnswers"),
                    className: "inline-flex items-center gap-1.5 px-2.5 py-1.5 text-xs font-medium text-rose-700 bg-rose-50 hover:bg-rose-100 rounded-lg border border-rose-200 transition-colors",
                    children: [a.jsx(Fa, {
                        className: "w-3.5 h-3.5 text-rose-600"
                    }), a.jsx("span", {
                        className: "hidden lg:inline",
                        children: i("nav.clearAnswers")
                    })]
                }), a.jsxs(Ue, {
                    to: "/shortlist",
                    className: `inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold rounded-lg transition-colors ${l.pathname === "/shortlist" ? "bg-orange-50 text-orange-700 border border-orange-200" : "text-slate-600 hover:bg-slate-100"}`,
                    children: [a.jsx(Gr, {
                        className: "w-4 h-4 text-orange-600"
                    }), a.jsx("span", {
                        className: "hidden sm:inline",
                        children: i("nav.shortlist")
                    }), h.length > 0 && a.jsx("span", {
                        className: "bg-orange-600 text-white text-[10px] font-bold px-1.5 py-0.2 rounded-full",
                        children: h.length
                    })]
                }), a.jsxs("div", {
                    className: "inline-flex items-center bg-slate-100 p-0.5 rounded-lg border border-slate-200",
                    children: [a.jsx(L0, {
                        className: "w-3.5 h-3.5 ml-1.5 text-slate-400 hidden sm:block"
                    }), a.jsx("button", {
                        type: "button",
                        onClick: () => x("en"),
                        className: `px-2 py-1 text-xs font-medium rounded-md transition-colors ${s.language === "en" ? "bg-white text-slate-900 shadow-xs font-bold" : "text-slate-600 hover:text-slate-900"}`,
                        children: "EN"
                    }), a.jsx("button", {
                        type: "button",
                        onClick: () => x("hi"),
                        className: `px-2 py-1 text-xs font-medium rounded-md transition-colors ${s.language === "hi" ? "bg-white text-slate-900 shadow-xs font-bold" : "text-slate-600 hover:text-slate-900"}`,
                        children: "हिन्दी"
                    }), a.jsx("button", {
                        type: "button",
                        onClick: () => x("mr"),
                        className: `px-2 py-1 text-xs font-medium rounded-md transition-colors ${s.language === "mr" ? "bg-white text-slate-900 shadow-xs font-bold" : "text-slate-600 hover:text-slate-900"}`,
                        children: "मराठी"
                    })]
                }), f === "authenticated" ? a.jsxs("button", {
                    onClick: () => g(),
                    className: "inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-700 hover:bg-slate-100 rounded-lg border border-slate-200",
                    children: [a.jsx(D0, {
                        className: "w-3.5 h-3.5 text-emerald-600"
                    }), a.jsx("span", {
                        className: "hidden sm:inline",
                        children: i("nav.logout")
                    })]
                }) : a.jsx(Ue, {
                    to: "/login",
                    className: "inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-700 hover:bg-slate-100 rounded-lg border border-slate-200",
                    children: a.jsx("span", {
                        children: i("nav.login")
                    })
                })]
            })]
        })]
    })
}
  , I0 = ({lastVerified: i="2026-09-15", source: s="fallback"}) => {
    const {t: l} = Je();
    return a.jsx("footer", {
        className: "mt-auto bg-slate-900 text-slate-300 border-t border-slate-800 text-xs",
        children: a.jsxs("div", {
            className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8",
            children: [a.jsxs("div", {
                className: "grid grid-cols-1 md:grid-cols-4 gap-6 mb-8",
                children: [a.jsxs("div", {
                    className: "md:col-span-2 space-y-3",
                    children: [a.jsxs("div", {
                        className: "flex items-center gap-2",
                        children: [a.jsx("span", {
                            className: "font-extrabold text-white text-base",
                            children: l("app.title")
                        }), a.jsx("span", {
                            className: "text-[10px] uppercase tracking-wider text-orange-400 font-semibold px-2 py-0.5 rounded bg-orange-950/60 border border-orange-800/60",
                            children: "PS-19 Open Source"
                        })]
                    }), a.jsx("p", {
                        className: "text-slate-400 max-w-md leading-relaxed text-xs",
                        children: l("app.tagline")
                    }), a.jsxs("div", {
                        className: "inline-flex items-center gap-2 text-emerald-400 bg-emerald-950/50 px-3 py-1.5 rounded-lg border border-emerald-800/50 text-[11px]",
                        children: [a.jsx(Lt, {
                            className: "w-4 h-4 text-emerald-400 shrink-0"
                        }), a.jsx("span", {
                            children: l("privacy.rule1Desc")
                        })]
                    })]
                }), a.jsxs("div", {
                    children: [a.jsx("h4", {
                        className: "text-white font-semibold mb-3 tracking-wide",
                        children: "Navigation"
                    }), a.jsxs("ul", {
                        className: "space-y-2 text-slate-400",
                        children: [a.jsx("li", {
                            children: a.jsx(Ue, {
                                to: "/",
                                className: "hover:text-white transition-colors",
                                children: l("nav.home")
                            })
                        }), a.jsx("li", {
                            children: a.jsx(Ue, {
                                to: "/find",
                                className: "hover:text-white transition-colors",
                                children: l("nav.finder")
                            })
                        }), a.jsx("li", {
                            children: a.jsx(Ue, {
                                to: "/results",
                                className: "hover:text-white transition-colors",
                                children: l("nav.results")
                            })
                        }), a.jsx("li", {
                            children: a.jsx(Ue, {
                                to: "/shortlist",
                                className: "hover:text-white transition-colors",
                                children: l("nav.shortlist")
                            })
                        })]
                    })]
                }), a.jsxs("div", {
                    children: [a.jsx("h4", {
                        className: "text-white font-semibold mb-3 tracking-wide",
                        children: "Constitutional Rights"
                    }), a.jsxs("ul", {
                        className: "space-y-2 text-slate-400",
                        children: [a.jsx("li", {
                            children: a.jsxs(Ue, {
                                to: "/about",
                                className: "hover:text-white transition-colors flex items-center gap-1",
                                children: [a.jsx(Yd, {
                                    className: "w-3.5 h-3.5"
                                }), a.jsx("span", {
                                    children: "The 4 Pillars"
                                })]
                            })
                        }), a.jsx("li", {
                            children: a.jsxs(Ue, {
                                to: "/privacy",
                                className: "hover:text-white transition-colors flex items-center gap-1",
                                children: [a.jsx(Lt, {
                                    className: "w-3.5 h-3.5"
                                }), a.jsx("span", {
                                    children: "DPDP Privacy Guarantee"
                                })]
                            })
                        }), a.jsx("li", {
                            children: a.jsxs("a", {
                                href: "https://india.gov.in",
                                target: "_blank",
                                rel: "noopener noreferrer",
                                className: "hover:text-white transition-colors flex items-center gap-1",
                                children: [a.jsx(Oa, {
                                    className: "w-3.5 h-3.5"
                                }), a.jsx("span", {
                                    children: "National Portal of India"
                                })]
                            })
                        })]
                    })]
                })]
            }), a.jsxs("div", {
                className: "border-t border-slate-800 pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-slate-400",
                children: [a.jsx("p", {
                    className: "text-[11px] text-center sm:text-left max-w-xl",
                    children: l("app.disclaimer")
                }), a.jsxs("div", {
                    className: "flex items-center gap-3 text-[11px] shrink-0",
                    children: [a.jsxs("span", {
                        className: "inline-flex items-center gap-1.5 text-slate-400",
                        children: [a.jsx(Jd, {
                            className: "w-3.5 h-3.5 text-slate-500"
                        }), a.jsxs("span", {
                            children: [l("scheme.lastVerified"), ": ", a.jsx("strong", {
                                className: "text-slate-200",
                                children: i
                            })]
                        })]
                    }), a.jsx("span", {
                        className: "text-slate-600",
                        children: "|"
                    }), a.jsx("span", {
                        className: "text-slate-400",
                        children: s === "supabase" ? "Online Catalog" : "Offline Verified Cache"
                    })]
                })]
            })]
        })
    })
}
  , F0 = () => {
    const {t: i} = Je()
      , {consentAccepted: s, setConsentAccepted: l} = _t();
    return s ? null : a.jsx("div", {
        className: "fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4",
        children: a.jsxs("div", {
            className: "bg-white rounded-2xl max-w-lg w-full p-6 shadow-2xl border border-slate-200 animate-in fade-in zoom-in-95 duration-200",
            children: [a.jsx("div", {
                className: "w-12 h-12 rounded-xl bg-emerald-50 border border-emerald-200 flex items-center justify-center text-emerald-600 mb-4",
                children: a.jsx(Lt, {
                    className: "w-6 h-6"
                })
            }), a.jsx("h3", {
                className: "text-lg font-bold text-slate-900 mb-2",
                children: i("privacy.heading")
            }), a.jsx("p", {
                className: "text-xs text-slate-600 leading-relaxed mb-4",
                children: i("privacy.lead")
            }), a.jsxs("div", {
                className: "space-y-2.5 mb-6 text-xs bg-slate-50 p-3.5 rounded-xl border border-slate-200",
                children: [a.jsxs("div", {
                    className: "flex items-start gap-2.5",
                    children: [a.jsx(Ia, {
                        className: "w-4 h-4 text-emerald-600 shrink-0 mt-0.5"
                    }), a.jsxs("div", {
                        children: [a.jsx("strong", {
                            className: "text-slate-900 block font-semibold",
                            children: i("privacy.rule1Title")
                        }), a.jsx("span", {
                            className: "text-slate-600",
                            children: i("privacy.rule1Desc")
                        })]
                    })]
                }), a.jsxs("div", {
                    className: "flex items-start gap-2.5",
                    children: [a.jsx(Lt, {
                        className: "w-4 h-4 text-emerald-600 shrink-0 mt-0.5"
                    }), a.jsxs("div", {
                        children: [a.jsx("strong", {
                            className: "text-slate-900 block font-semibold",
                            children: i("privacy.rule2Title")
                        }), a.jsx("span", {
                            className: "text-slate-600",
                            children: i("privacy.rule2Desc")
                        })]
                    })]
                })]
            }), a.jsxs("div", {
                className: "flex flex-col sm:flex-row items-center justify-between gap-3",
                children: [a.jsx(Ue, {
                    to: "/privacy",
                    onClick: () => l(!0),
                    className: "text-xs font-semibold text-slate-600 hover:text-slate-900 order-2 sm:order-1",
                    children: "Read Full Privacy Notice"
                }), a.jsxs("button", {
                    onClick: () => l(!0),
                    className: "w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 py-2.5 bg-orange-600 hover:bg-orange-700 text-white text-xs font-bold rounded-xl shadow transition-colors order-1 sm:order-2",
                    children: [a.jsx("span", {
                        children: "Continue as Guest"
                    }), a.jsx(Cn, {
                        className: "w-3.5 h-3.5"
                    })]
                })]
            })]
        })
    })
}
  , U0 = () => {
    const {t: i} = Je()
      , s = rr()
      , {profile: l} = _t()
      , u = Object.values(l).some(d => d !== void 0 && d !== "");
    return a.jsxs("div", {
        className: "space-y-16 pb-16",
        children: [a.jsx("section", {
            className: "relative overflow-hidden bg-gradient-to-b from-orange-50/50 via-white to-slate-50 pt-12 pb-16 border-b border-slate-200",
            children: a.jsxs("div", {
                className: "max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6",
                children: [a.jsxs("div", {
                    className: "inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200 text-xs font-bold shadow-xs",
                    children: [a.jsx(Lt, {
                        className: "w-4 h-4 text-emerald-600"
                    }), a.jsx("span", {
                        children: i("app.privacyBadge")
                    })]
                }), a.jsx("h1", {
                    className: "text-3xl sm:text-5xl font-black text-slate-900 tracking-tight leading-tight",
                    children: i("hero.heading")
                }), a.jsx("p", {
                    className: "text-base sm:text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed",
                    children: i("hero.subheading")
                }), a.jsxs("div", {
                    className: "pt-4 flex flex-col sm:flex-row items-center justify-center gap-4",
                    children: [a.jsxs("button", {
                        onClick: () => s("/find"),
                        className: "w-full sm:w-auto inline-flex items-center justify-center gap-2.5 px-8 py-4 bg-orange-600 hover:bg-orange-700 text-white font-extrabold text-base rounded-2xl shadow-lg hover:shadow-orange-600/25 transition-all transform hover:-translate-y-0.5",
                        children: [a.jsx("span", {
                            children: i(u ? "hero.continue" : "hero.cta")
                        }), a.jsx(Cn, {
                            className: "w-5 h-5"
                        })]
                    }), a.jsx(Ue, {
                        to: "/results",
                        className: "w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-4 bg-white hover:bg-slate-50 text-slate-700 font-bold text-base rounded-2xl border border-slate-300 shadow-xs transition-colors",
                        children: a.jsx("span", {
                            children: "Browse All Schemes"
                        })
                    })]
                }), a.jsxs("div", {
                    className: "pt-8 grid grid-cols-1 sm:grid-cols-3 gap-4 max-w-3xl mx-auto text-left",
                    children: [a.jsxs("div", {
                        className: "bg-white p-4 rounded-xl border border-slate-200 shadow-xs flex items-start gap-3",
                        children: [a.jsx(S0, {
                            className: "w-5 h-5 text-orange-600 shrink-0 mt-0.5"
                        }), a.jsxs("div", {
                            children: [a.jsx("strong", {
                                className: "block text-xs font-bold text-slate-900",
                                children: "Under 2 Minutes"
                            }), a.jsx("span", {
                                className: "text-[11px] text-slate-500",
                                children: "6 core questions; instant offline ranking"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "bg-white p-4 rounded-xl border border-slate-200 shadow-xs flex items-start gap-3",
                        children: [a.jsx(Ia, {
                            className: "w-5 h-5 text-emerald-600 shrink-0 mt-0.5"
                        }), a.jsxs("div", {
                            children: [a.jsx("strong", {
                                className: "block text-xs font-bold text-slate-900",
                                children: "Zero Retention"
                            }), a.jsx("span", {
                                className: "text-[11px] text-slate-500",
                                children: "No login, Aadhaar, or phone required"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "bg-white p-4 rounded-xl border border-slate-200 shadow-xs flex items-start gap-3",
                        children: [a.jsx(Ta, {
                            className: "w-5 h-5 text-blue-600 shrink-0 mt-0.5"
                        }), a.jsxs("div", {
                            children: [a.jsx("strong", {
                                className: "block text-xs font-bold text-slate-900",
                                children: "Document Checklist"
                            }), a.jsx("span", {
                                className: "text-[11px] text-slate-500",
                                children: "Know exactly what papers to carry"
                            })]
                        })]
                    })]
                })]
            })
        }), a.jsxs("section", {
            className: "max-w-5xl mx-auto px-4 sm:px-6 lg:px-8",
            children: [a.jsxs("div", {
                className: "text-center space-y-2 mb-10",
                children: [a.jsx("h2", {
                    className: "text-2xl sm:text-3xl font-bold text-slate-900",
                    children: i("hero.howItWorks")
                }), a.jsx("p", {
                    className: "text-xs sm:text-sm text-slate-500",
                    children: "Three simple steps to unlock government support for your household"
                })]
            }), a.jsxs("div", {
                className: "grid grid-cols-1 md:grid-cols-3 gap-6",
                children: [a.jsxs("div", {
                    className: "bg-white p-6 rounded-2xl border border-slate-200 shadow-xs text-center space-y-3",
                    children: [a.jsx("div", {
                        className: "w-12 h-12 rounded-2xl bg-orange-50 text-orange-600 font-black text-xl flex items-center justify-center mx-auto border border-orange-200",
                        children: "1"
                    }), a.jsx("h3", {
                        className: "font-bold text-slate-900 text-sm",
                        children: i("hero.step1")
                    }), a.jsx("p", {
                        className: "text-xs text-slate-600 leading-relaxed",
                        children: "Answer basic questions about age, location, occupation, and family in English, Hindi, or Marathi."
                    })]
                }), a.jsxs("div", {
                    className: "bg-white p-6 rounded-2xl border border-slate-200 shadow-xs text-center space-y-3",
                    children: [a.jsx("div", {
                        className: "w-12 h-12 rounded-2xl bg-blue-50 text-blue-600 font-black text-xl flex items-center justify-center mx-auto border border-blue-200",
                        children: "2"
                    }), a.jsx("h3", {
                        className: "font-bold text-slate-900 text-sm",
                        children: i("hero.step2")
                    }), a.jsx("p", {
                        className: "text-xs text-slate-600 leading-relaxed",
                        children: "See instant results grouped into Eligible, Almost Eligible (near-misses), and clear reasons for any missed criteria."
                    })]
                }), a.jsxs("div", {
                    className: "bg-white p-6 rounded-2xl border border-slate-200 shadow-xs text-center space-y-3",
                    children: [a.jsx("div", {
                        className: "w-12 h-12 rounded-2xl bg-emerald-50 text-emerald-600 font-black text-xl flex items-center justify-center mx-auto border border-emerald-200",
                        children: "3"
                    }), a.jsx("h3", {
                        className: "font-bold text-slate-900 text-sm",
                        children: i("hero.step3")
                    }), a.jsx("p", {
                        className: "text-xs text-slate-600 leading-relaxed",
                        children: "Print a unified document checklist with hints on where to obtain certificates, then apply directly on the official portal."
                    })]
                })]
            })]
        }), a.jsx("section", {
            className: "max-w-5xl mx-auto px-4 sm:px-6 lg:px-8",
            children: a.jsx("div", {
                className: "bg-gradient-to-r from-slate-900 via-chakra-900 to-slate-900 text-white rounded-3xl p-8 sm:p-10 shadow-xl relative overflow-hidden",
                children: a.jsxs("div", {
                    className: "relative z-10 space-y-4 max-w-2xl",
                    children: [a.jsxs("div", {
                        className: "inline-flex items-center gap-2 bg-orange-500/20 text-orange-300 px-3 py-1 rounded-full text-xs font-bold border border-orange-500/30",
                        children: [a.jsx(Zr, {
                            className: "w-3.5 h-3.5"
                        }), a.jsx("span", {
                            children: "Grounded in Constitutional Values"
                        })]
                    }), a.jsx("h2", {
                        className: "text-2xl sm:text-3xl font-black",
                        children: "The Four Pillars of Citizen Welfare"
                    }), a.jsx("p", {
                        className: "text-xs sm:text-sm text-slate-300 leading-relaxed",
                        children: "Every scheme in Yojana Setu is mapped to the Directive Principles and Fundamental Rights of the Indian Constitution — Justice (Articles 38, 39), Liberty (Articles 19, 21A), Equality (Articles 14, 15), and Fraternity (Articles 41, 43)."
                    }), a.jsx("div", {
                        className: "pt-2",
                        children: a.jsxs(Ue, {
                            to: "/about",
                            className: "inline-flex items-center gap-2 text-xs font-bold text-orange-400 hover:text-orange-300 hover:underline",
                            children: [a.jsx("span", {
                                children: "Read Constitutional Mapping & Methodology"
                            }), a.jsx(Cn, {
                                className: "w-4 h-4"
                            })]
                        })
                    })]
                })
            })
        })]
    })
}
  , B0 = ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh", "Chhattisgarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
  , V0 = [{
    id: "farmer",
    labelKey: "wizard.farmer",
    icon: "🌾"
}, {
    id: "student",
    labelKey: "wizard.student",
    icon: "🎓"
}, {
    id: "artisan",
    labelKey: "wizard.artisan",
    icon: "🛠"
}, {
    id: "street_vendor",
    labelKey: "wizard.street_vendor",
    icon: "🛒"
}, {
    id: "self_employed",
    labelKey: "wizard.self_employed",
    icon: "💼"
}, {
    id: "salaried",
    labelKey: "wizard.salaried",
    icon: "🏢"
}, {
    id: "unemployed",
    labelKey: "wizard.unemployed",
    icon: "🔎"
}, {
    id: "homemaker",
    labelKey: "wizard.homemaker",
    icon: "🏠"
}, {
    id: "retired",
    labelKey: "wizard.retired",
    icon: "👴"
}]
  , H0 = () => {
    const {t: i} = Je()
      , s = rr()
      , {profile: l, setProfileField: u, setHasStarted: d} = _t()
      , [f,h] = O.useState(1)
      , g = 6
      , m = () => {
        f < g ? h(f + 1) : (d(!0),
        s("/results"))
    }
      , x = () => {
        f > 1 && h(f - 1)
    }
      , b = () => {
        m()
    }
      , w = v => {
        const R = l.occupation || []
          , _ = R.includes(v) ? R.filter(P => P !== v) : [...R, v];
        u("occupation", _)
    }
    ;
    return a.jsxs("div", {
        className: "max-w-2xl mx-auto w-full bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden",
        children: [a.jsxs("div", {
            className: "bg-slate-50 border-b border-slate-200 px-6 py-4 flex items-center justify-between",
            children: [a.jsxs("div", {
                className: "flex items-center gap-2",
                children: [a.jsx("span", {
                    className: "w-6 h-6 rounded-full bg-orange-600 text-white text-xs font-bold flex items-center justify-center",
                    children: f
                }), a.jsx("span", {
                    className: "text-xs font-semibold text-slate-700",
                    children: i("wizard.coreProgress", {
                        current: f
                    })
                })]
            }), a.jsx("div", {
                className: "flex items-center gap-1.5",
                children: Array.from({
                    length: g
                }).map( (v, R) => a.jsx("button", {
                    type: "button",
                    onClick: () => h(R + 1),
                    className: `h-2 rounded-full transition-all duration-300 ${R + 1 === f ? "w-6 bg-orange-600" : R + 1 < f ? "w-2 bg-emerald-500" : "w-2 bg-slate-200"}`
                }, R))
            })]
        }), a.jsxs("div", {
            className: "p-6 sm:p-8 min-h-[320px] flex flex-col justify-between",
            children: [a.jsxs("div", {
                children: [f === 1 && a.jsxs("div", {
                    className: "space-y-4 animate-in fade-in duration-200",
                    children: [a.jsxs("div", {
                        children: [a.jsx("h3", {
                            className: "text-xl font-bold text-slate-900 mb-1",
                            children: i("wizard.qAge")
                        }), a.jsx("p", {
                            className: "text-xs text-slate-500",
                            children: i("wizard.qAgeHint")
                        })]
                    }), a.jsxs("div", {
                        className: "pt-4 flex flex-col sm:flex-row sm:items-center gap-4",
                        children: [a.jsx("input", {
                            type: "number",
                            min: 0,
                            max: 120,
                            placeholder: "e.g. 35",
                            value: l.age ?? "",
                            onChange: v => {
                                const R = v.target.value === "" ? void 0 : parseInt(v.target.value, 10);
                                u("age", R)
                            }
                            ,
                            className: "w-full sm:w-40 px-4 py-3 text-2xl font-bold text-slate-900 bg-slate-50 border border-slate-300 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-orange-500 focus:bg-white"
                        }), a.jsx("div", {
                            className: "flex flex-wrap gap-2",
                            children: [18, 25, 45, 60, 70].map(v => a.jsxs("button", {
                                type: "button",
                                onClick: () => u("age", v),
                                className: `px-3 py-1.5 text-xs font-semibold rounded-lg border transition-colors ${l.age === v ? "bg-orange-600 text-white border-orange-600" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                children: [v, " yrs"]
                            }, v))
                        })]
                    })]
                }), f === 2 && a.jsxs("div", {
                    className: "space-y-4 animate-in fade-in duration-200",
                    children: [a.jsxs("div", {
                        children: [a.jsx("h3", {
                            className: "text-xl font-bold text-slate-900 mb-1",
                            children: i("wizard.qGender")
                        }), a.jsx("p", {
                            className: "text-xs text-slate-500",
                            children: "Many schemes offer dedicated benefits for women or transgender persons."
                        })]
                    }), a.jsx("div", {
                        className: "grid grid-cols-1 sm:grid-cols-2 gap-3 pt-3",
                        children: [{
                            id: "female",
                            labelKey: "wizard.female",
                            icon: "👩"
                        }, {
                            id: "male",
                            labelKey: "wizard.male",
                            icon: "👨"
                        }, {
                            id: "other",
                            labelKey: "wizard.other",
                            icon: "⚧"
                        }].map(v => a.jsxs("button", {
                            type: "button",
                            onClick: () => u("gender", v.id),
                            className: `flex items-center gap-3 p-4 rounded-xl border text-left font-medium transition-all ${l.gender === v.id ? "border-orange-600 bg-orange-50/60 ring-2 ring-orange-500/30 text-orange-950 font-bold" : "border-slate-200 bg-white hover:bg-slate-50 text-slate-700"}`,
                            children: [a.jsx("span", {
                                className: "text-2xl",
                                children: v.icon
                            }), a.jsx("span", {
                                children: i(v.labelKey)
                            }), l.gender === v.id && a.jsx(mt, {
                                className: "w-5 h-5 text-orange-600 ml-auto"
                            })]
                        }, v.id))
                    })]
                }), f === 3 && a.jsxs("div", {
                    className: "space-y-4 animate-in fade-in duration-200",
                    children: [a.jsxs("div", {
                        children: [a.jsx("h3", {
                            className: "text-xl font-bold text-slate-900 mb-1",
                            children: i("wizard.qState")
                        }), a.jsx("p", {
                            className: "text-xs text-slate-500",
                            children: "Filters both Central all-India schemes and state-specific portals."
                        })]
                    }), a.jsx("div", {
                        className: "pt-2",
                        children: a.jsxs("select", {
                            value: l.state ?? "",
                            onChange: v => u("state", v.target.value || void 0),
                            className: "w-full px-4 py-3 text-sm font-medium bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-orange-500 focus:bg-white",
                            children: [a.jsxs("option", {
                                value: "",
                                children: ["-- ", i("wizard.selectState"), " --"]
                            }), B0.map(v => a.jsx("option", {
                                value: v,
                                children: v
                            }, v))]
                        })
                    })]
                }), f === 4 && a.jsxs("div", {
                    className: "space-y-4 animate-in fade-in duration-200",
                    children: [a.jsxs("div", {
                        children: [a.jsx("h3", {
                            className: "text-xl font-bold text-slate-900 mb-1",
                            children: i("wizard.qResidence")
                        }), a.jsx("p", {
                            className: "text-xs text-slate-500",
                            children: "Certain schemes focus specifically on rural development or urban poor."
                        })]
                    }), a.jsx("div", {
                        className: "grid grid-cols-1 sm:grid-cols-2 gap-3 pt-3",
                        children: [{
                            id: "rural",
                            labelKey: "wizard.rural",
                            icon: "🏡"
                        }, {
                            id: "urban",
                            labelKey: "wizard.urban",
                            icon: "🏙"
                        }].map(v => a.jsxs("button", {
                            type: "button",
                            onClick: () => u("residence", v.id),
                            className: `flex items-center gap-3 p-4 rounded-xl border text-left font-medium transition-all ${l.residence === v.id ? "border-orange-600 bg-orange-50/60 ring-2 ring-orange-500/30 text-orange-950 font-bold" : "border-slate-200 bg-white hover:bg-slate-50 text-slate-700"}`,
                            children: [a.jsx("span", {
                                className: "text-2xl",
                                children: v.icon
                            }), a.jsx("span", {
                                children: i(v.labelKey)
                            }), l.residence === v.id && a.jsx(mt, {
                                className: "w-5 h-5 text-orange-600 ml-auto"
                            })]
                        }, v.id))
                    })]
                }), f === 5 && a.jsxs("div", {
                    className: "space-y-4 animate-in fade-in duration-200",
                    children: [a.jsxs("div", {
                        children: [a.jsx("h3", {
                            className: "text-xl font-bold text-slate-900 mb-1",
                            children: i("wizard.qIncome")
                        }), a.jsx("p", {
                            className: "text-xs text-slate-500",
                            children: i("wizard.incomeHint")
                        })]
                    }), a.jsxs("div", {
                        className: "pt-2 space-y-4",
                        children: [a.jsxs("div", {
                            className: "flex flex-col sm:flex-row sm:items-center gap-3",
                            children: [a.jsxs("div", {
                                className: "relative w-full sm:w-48",
                                children: [a.jsx("span", {
                                    className: "absolute left-3.5 top-1/2 -translate-y-1/2 font-bold text-slate-400",
                                    children: "₹"
                                }), a.jsx("input", {
                                    type: "number",
                                    step: "0.1",
                                    min: 0,
                                    max: 100,
                                    placeholder: "e.g. 1.8",
                                    value: l.incomeLakh ?? "",
                                    onChange: v => {
                                        const R = v.target.value === "" ? void 0 : parseFloat(v.target.value);
                                        u("incomeLakh", R)
                                    }
                                    ,
                                    className: "w-full pl-8 pr-4 py-3 text-2xl font-bold text-slate-900 bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-orange-500 focus:bg-white"
                                })]
                            }), a.jsx("span", {
                                className: "text-xs sm:text-sm font-semibold text-slate-500",
                                children: "Lakh / year"
                            })]
                        }), a.jsx("div", {
                            className: "flex flex-wrap gap-2",
                            children: [{
                                label: "< ₹1 Lakh",
                                val: .8
                            }, {
                                label: "₹1.5 - ₹2.5 Lakh",
                                val: 2
                            }, {
                                label: "₹2.5 - ₹5 Lakh",
                                val: 3.5
                            }, {
                                label: "₹5 - ₹8 Lakh",
                                val: 6
                            }, {
                                label: "₹8+ Lakh",
                                val: 9
                            }].map(v => a.jsx("button", {
                                type: "button",
                                onClick: () => u("incomeLakh", v.val),
                                className: `px-3 py-1.5 text-xs font-semibold rounded-lg border transition-colors ${l.incomeLakh === v.val ? "bg-orange-600 text-white border-orange-600" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                children: v.label
                            }, v.label))
                        })]
                    })]
                }), f === 6 && a.jsxs("div", {
                    className: "space-y-4 animate-in fade-in duration-200",
                    children: [a.jsxs("div", {
                        children: [a.jsx("h3", {
                            className: "text-xl font-bold text-slate-900 mb-1",
                            children: i("wizard.qOccupation")
                        }), a.jsx("p", {
                            className: "text-xs text-slate-500",
                            children: "Select all that describe you or family members (multiple allowed)."
                        })]
                    }), a.jsx("div", {
                        className: "grid grid-cols-2 sm:grid-cols-3 gap-2.5 pt-2 max-h-[300px] overflow-y-auto pr-1",
                        children: V0.map(v => {
                            var E;
                            const R = (E = l.occupation) == null ? void 0 : E.includes(v.id);
                            return a.jsxs("button", {
                                type: "button",
                                onClick: () => w(v.id),
                                className: `p-3 rounded-xl border text-left flex items-center gap-2.5 transition-all text-xs font-medium ${R ? "border-orange-600 bg-orange-50/70 text-orange-950 font-bold ring-1 ring-orange-500/40" : "border-slate-200 bg-white hover:bg-slate-50 text-slate-700"}`,
                                children: [a.jsx("span", {
                                    className: "text-lg",
                                    children: v.icon
                                }), a.jsx("span", {
                                    className: "truncate",
                                    children: i(v.labelKey)
                                }), R && a.jsx(mt, {
                                    className: "w-3.5 h-3.5 text-orange-600 ml-auto shrink-0"
                                })]
                            }, v.id)
                        }
                        )
                    })]
                })]
            }), a.jsxs("div", {
                className: "mt-8 pt-4 border-t border-slate-100 flex items-center justify-between gap-3",
                children: [a.jsx("div", {
                    children: f > 1 ? a.jsxs("button", {
                        type: "button",
                        onClick: x,
                        className: "inline-flex items-center gap-1.5 px-3.5 py-2 text-xs font-semibold text-slate-600 hover:text-slate-900 bg-slate-100 hover:bg-slate-200 rounded-xl transition-colors",
                        children: [a.jsx(Ra, {
                            className: "w-3.5 h-3.5"
                        }), a.jsx("span", {
                            children: i("wizard.back")
                        })]
                    }) : a.jsxs("button", {
                        type: "button",
                        onClick: b,
                        className: "inline-flex items-center gap-1.5 text-xs font-medium text-slate-500 hover:text-slate-700",
                        children: [a.jsx(wl, {
                            className: "w-3.5 h-3.5"
                        }), a.jsx("span", {
                            children: i("wizard.skip")
                        })]
                    })
                }), a.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [f < g && a.jsx("button", {
                        type: "button",
                        onClick: b,
                        className: "px-3 py-2 text-xs font-medium text-slate-500 hover:text-slate-700",
                        children: i("wizard.skip")
                    }), a.jsxs("button", {
                        type: "button",
                        onClick: m,
                        className: "inline-flex items-center gap-2 px-5 py-2.5 bg-orange-600 hover:bg-orange-700 text-white text-xs font-bold rounded-xl shadow transition-colors",
                        children: [a.jsx("span", {
                            children: i(f === g ? "wizard.showSchemes" : "wizard.next")
                        }), f === g ? a.jsx(an, {
                            className: "w-4 h-4 text-orange-200"
                        }) : a.jsx(Cn, {
                            className: "w-3.5 h-3.5"
                        })]
                    })]
                })]
            })]
        })]
    })
}
  , K0 = () => {
    const {t: i} = Je();
    return a.jsxs("div", {
        className: "max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6",
        children: [a.jsxs("div", {
            className: "text-center space-y-2",
            children: [a.jsxs("div", {
                className: "inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200 text-xs font-bold shadow-xs",
                children: [a.jsx(Lt, {
                    className: "w-3.5 h-3.5 text-emerald-600"
                }), a.jsx("span", {
                    children: i("app.privacyBadge")
                })]
            }), a.jsx("h1", {
                className: "text-2xl sm:text-3xl font-extrabold text-slate-900",
                children: i("wizard.title")
            }), a.jsx("p", {
                className: "text-xs sm:text-sm text-slate-500 max-w-md mx-auto",
                children: i("wizard.subtitle")
            })]
        }), a.jsx(H0, {})]
    })
}
;
function W0(i, s, l=[]) {
    const u = s.length || 1
      , d = s.filter(H => H.status === "pass").length
      , f = s.filter(H => H.status === "near").length
      , h = s.filter(H => H.status === "unknown").length
      , g = (d * 1 + f * .5 + h * .25) / u
      , m = Number((g * 40).toFixed(1));
    let x = .5;
    l.length > 0 && (x = l.includes(i.category_id) ? 1 : 0);
    const b = Number((x * 25).toFixed(1))
      , v = ((i.benefit_tier || 2) - 1) / 2
      , R = Number((v * 15).toFixed(1))
      , _ = ((i.ease || 2) - 1) / 2
      , P = Number((_ * 10).toFixed(1));
    let $ = 1;
    i.status === "unknown" && ($ = .5),
    i.status === "closed" && ($ = 0);
    const I = Number(($ * 10).toFixed(1))
      , V = Math.min(100, Math.max(0, Math.round(m + b + R + P + I)));
    return {
        totalScore: V,
        breakdown: {
            matchStrength: m,
            needFit: b,
            benefitValue: R,
            ease: P,
            openness: I,
            total: V
        }
    }
}
function q0(i, s, l) {
    if (i == null)
        return !1;
    switch (s) {
    case "eq":
        return i === l;
    case "neq":
        return i !== l;
    case "in":
        return Array.isArray(l) ? l.includes(i) : !1;
    case "nin":
        return Array.isArray(l) ? !l.includes(i) : !0;
    case "gte":
        return typeof i == "number" && typeof l == "number" && i >= l;
    case "lte":
        return typeof i == "number" && typeof l == "number" && i <= l;
    case "between":
        if (Array.isArray(l) && l.length === 2 && typeof i == "number") {
            const [u,d] = l;
            return i >= u && i <= d
        }
        return !1;
    case "includes":
        return Array.isArray(i) ? i.includes(l) : !1;
    default:
        return !1
    }
}
function Y0(i, s) {
    if (typeof i != "number" || !s.tolerance)
        return {
            within: !1
        };
    const {abs: l, pct: u} = s.tolerance;
    if (s.op === "lte" && typeof s.value == "number") {
        const d = s.value
          , f = Math.max(l !== void 0 ? d + l : d, u !== void 0 ? d * (1 + u) : d);
        if (i <= f)
            return {
                within: !0,
                gap: Number((i - d).toFixed(2))
            }
    }
    if (s.op === "gte" && typeof s.value == "number") {
        const d = s.value
          , f = Math.min(l !== void 0 ? d - l : d, u !== void 0 ? d * (1 - u) : d);
        if (i >= f)
            return {
                within: !0,
                gap: Number((d - i).toFixed(2))
            }
    }
    if (s.op === "between" && Array.isArray(s.value) && s.value.length === 2) {
        const [d,f] = s.value;
        if (i < d) {
            const h = Math.min(l !== void 0 ? d - l : d, u !== void 0 ? d * (1 - u) : d);
            if (i >= h)
                return {
                    within: !0,
                    gap: Number((d - i).toFixed(2))
                }
        } else if (i > f) {
            const h = Math.max(l !== void 0 ? f + l : f, u !== void 0 ? f * (1 + u) : f);
            if (i <= h)
                return {
                    within: !0,
                    gap: Number((i - f).toFixed(2))
                }
        }
    }
    return {
        within: !1
    }
}
function Q0(i, s) {
    const l = s[i.field];
    if (l == null)
        return {
            id: i.id,
            field: i.field,
            status: "unknown",
            actual: void 0,
            expected: i.value,
            tolerance: i.tolerance,
            fixable: i.fixable,
            reasonKey: i.reasonKey,
            fixKey: i.fixKey
        };
    if (q0(l, i.op, i.value))
        return {
            id: i.id,
            field: i.field,
            status: "pass",
            actual: l,
            expected: i.value,
            tolerance: i.tolerance,
            fixable: i.fixable,
            reasonKey: i.reasonKey,
            fixKey: i.fixKey
        };
    const d = Y0(l, i);
    return d.within ? {
        id: i.id,
        field: i.field,
        status: "near",
        actual: l,
        expected: i.value,
        tolerance: i.tolerance,
        fixable: i.fixable,
        reasonKey: i.reasonKey,
        fixKey: i.fixKey,
        gap: d.gap
    } : i.fixable ? {
        id: i.id,
        field: i.field,
        status: "near",
        actual: l,
        expected: i.value,
        tolerance: i.tolerance,
        fixable: !0,
        reasonKey: i.reasonKey,
        fixKey: i.fixKey
    } : {
        id: i.id,
        field: i.field,
        status: "fail",
        actual: l,
        expected: i.value,
        tolerance: i.tolerance,
        fixable: i.fixable,
        reasonKey: i.reasonKey,
        fixKey: i.fixKey
    }
}
function Ma(i, s) {
    if ("field" in i) {
        const l = Q0(i, s);
        return {
            status: l.status,
            leaves: [l]
        }
    }
    if ("all" in i) {
        const l = i.all.map(d => Ma(d, s))
          , u = l.flatMap(d => d.leaves);
        return l.some(d => d.status === "fail") ? {
            status: "fail",
            leaves: u
        } : l.some(d => d.status === "unknown") ? {
            status: "unknown",
            leaves: u
        } : l.some(d => d.status === "near") ? {
            status: "near",
            leaves: u
        } : {
            status: "pass",
            leaves: u
        }
    }
    if ("any" in i) {
        const l = i.any.map(d => Ma(d, s))
          , u = l.flatMap(d => d.leaves);
        return l.some(d => d.status === "pass") ? {
            status: "pass",
            leaves: u
        } : l.some(d => d.status === "unknown") ? {
            status: "unknown",
            leaves: u
        } : l.some(d => d.status === "near") ? {
            status: "near",
            leaves: u
        } : {
            status: "fail",
            leaves: u
        }
    }
    return {
        status: "unknown",
        leaves: []
    }
}
function G0(i, s) {
    return i === "pass" ? "eligible" : i === "near" ? s <= 2 ? "almost" : "not_eligible" : i === "unknown" ? "possible" : "not_eligible"
}
function Ua(i, s, l=[]) {
    if (i.state_code && s.state && i.state_code !== s.state)
        return null;
    const {status: u, leaves: d} = Ma(i.rules, s)
      , f = d.filter(v => v.status === "fail")
      , h = d.filter(v => v.status === "near")
      , g = d.filter(v => v.status === "unknown")
      , m = Array.from(new Set(g.map(v => v.field)))
      , x = G0(u, h.length)
      , {totalScore: b, breakdown: w} = W0(i, d, l);
    return {
        schemeId: i.id,
        slug: i.slug,
        verdict: x,
        leaves: d,
        missingFields: m,
        failedRules: f,
        nearRules: h,
        relevanceScore: b,
        scoreBreakdown: w
    }
}
function J0(i, s, l=[]) {
    const u = [];
    for (const h of i) {
        if (!h.is_published)
            continue;
        const g = Ua(h, s, l);
        g && u.push(g)
    }
    const d = {
        eligible: 4,
        almost: 3,
        possible: 2,
        not_eligible: 1
    };
    u.sort( (h, g) => d[g.verdict] !== d[h.verdict] ? d[g.verdict] - d[h.verdict] : g.relevanceScore !== h.relevanceScore ? g.relevanceScore - h.relevanceScore : h.slug.localeCompare(g.slug));
    const f = {
        eligible: u.filter(h => h.verdict === "eligible"),
        almost: u.filter(h => h.verdict === "almost"),
        possible: u.filter(h => h.verdict === "possible"),
        not_eligible: u.filter(h => h.verdict === "not_eligible")
    };
    return {
        evaluations: u,
        grouped: f
    }
}
let Kr = null
  , wd = "fallback";
async function bl() {
    if (Kr && Kr.length > 0) {
        const i = bd(Kr);
        return {
            schemes: Kr,
            source: wd,
            lastVerified: i
        }
    }
    try {
        const i = await fetch("/schemes.fallback.json");
        if (i.ok) {
            const s = await i.json();
            return Kr = s,
            wd = "fallback",
            {
                schemes: s,
                source: "fallback",
                lastVerified: bd(s)
            }
        }
    } catch (i) {
        console.error("Failed to load fallback schemes:", i)
    }
    return {
        schemes: [],
        source: "fallback",
        lastVerified: "2026-09-15"
    }
}
function bd(i) {
    if (!i || i.length === 0)
        return "2026-09-15";
    const s = i.map(l => l.last_verified).filter(Boolean);
    return s.length === 0 ? "2026-09-15" : s.reduce( (l, u) => u > l ? u : l, s[0])
}
const X0 = [{
    id: "justice",
    titleKey: "pillars.justice",
    subKey: "pillars.justiceSub",
    icon: Zr,
    articles: ["Art. 38", "Art. 39(b)", "Art. 41", "Art. 47"],
    color: {
        bg: "bg-blue-50/60",
        border: "border-blue-200",
        text: "text-blue-900",
        activeBg: "bg-blue-600 text-white",
        badge: "bg-blue-100 text-blue-800"
    }
}, {
    id: "liberty",
    titleKey: "pillars.liberty",
    subKey: "pillars.libertySub",
    icon: C0,
    articles: ["Art. 19(1)(g)", "Art. 21A", "Art. 43", "Art. 46"],
    color: {
        bg: "bg-amber-50/60",
        border: "border-amber-200",
        text: "text-amber-900",
        activeBg: "bg-amber-600 text-white",
        badge: "bg-amber-100 text-amber-800"
    }
}, {
    id: "equality",
    titleKey: "pillars.equality",
    subKey: "pillars.equalitySub",
    icon: Wd,
    articles: ["Art. 14", "Art. 15(3)", "Art. 39(a)", "Art. 42"],
    color: {
        bg: "bg-emerald-50/60",
        border: "border-emerald-200",
        text: "text-emerald-900",
        activeBg: "bg-emerald-600 text-white",
        badge: "bg-emerald-100 text-emerald-800"
    }
}, {
    id: "fraternity",
    titleKey: "pillars.fraternity",
    subKey: "pillars.fraternitySub",
    icon: _0,
    articles: ["Art. 41", "Art. 43", "Preamble"],
    color: {
        bg: "bg-purple-50/60",
        border: "border-purple-200",
        text: "text-purple-900",
        activeBg: "bg-purple-600 text-white",
        badge: "bg-purple-100 text-purple-800"
    }
}]
  , Z0 = ({schemes: i, className: s=""}) => {
    const {t: l} = Je()
      , {selectedPillars: u, togglePillar: d, clearPillars: f} = _t()
      , h = g => i.filter(m => {
        var x;
        return ((x = m.category) == null ? void 0 : x.pillar) === g
    }
    ).length;
    return a.jsxs("aside", {
        className: `pillar-rail space-y-4 ${s}`,
        children: [a.jsxs("div", {
            className: "flex items-center justify-between pb-2 border-b border-slate-200",
            children: [a.jsxs("div", {
                children: [a.jsx("h3", {
                    className: "text-xs font-bold uppercase tracking-wider text-slate-500",
                    children: l("pillars.title")
                }), a.jsx("p", {
                    className: "text-[11px] text-slate-400",
                    children: l("pillars.subtitle")
                })]
            }), u.length > 0 && a.jsx("button", {
                onClick: f,
                className: "text-[11px] font-semibold text-orange-600 hover:text-orange-700",
                children: "Show All"
            })]
        }), a.jsx("div", {
            className: "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-1 gap-2.5",
            children: X0.map(g => {
                const m = u.includes(g.id)
                  , x = h(g.id)
                  , b = g.icon;
                return a.jsxs("div", {
                    onClick: () => d(g.id),
                    role: "button",
                    tabIndex: 0,
                    onKeyDown: w => {
                        (w.key === "Enter" || w.key === " ") && (w.preventDefault(),
                        d(g.id))
                    }
                    ,
                    className: `p-3 rounded-xl border text-left cursor-pointer transition-all duration-150 select-none ${m ? "bg-slate-900 text-white border-slate-900 shadow-md ring-2 ring-orange-500/40" : "bg-white hover:bg-slate-50/80 border-slate-200 text-slate-800 shadow-xs"}`,
                    children: [a.jsxs("div", {
                        className: "flex items-start justify-between gap-2",
                        children: [a.jsxs("div", {
                            className: "flex items-center gap-2",
                            children: [a.jsx("div", {
                                className: `w-7 h-7 rounded-lg flex items-center justify-center ${m ? "bg-orange-500 text-white" : g.color.bg + " " + g.color.text}`,
                                children: a.jsx(b, {
                                    className: "w-4 h-4"
                                })
                            }), a.jsxs("div", {
                                children: [a.jsx("h4", {
                                    className: "text-xs font-bold leading-tight",
                                    children: l(g.titleKey)
                                }), a.jsx("p", {
                                    className: `text-[10px] leading-tight ${m ? "text-slate-300" : "text-slate-500"}`,
                                    children: l(g.subKey)
                                })]
                            })]
                        }), a.jsxs("div", {
                            className: "flex items-center gap-1.5 shrink-0",
                            children: [a.jsx("span", {
                                className: `text-[11px] font-bold px-1.5 py-0.5 rounded-full ${m ? "bg-white/20 text-white" : "bg-slate-100 text-slate-700"}`,
                                children: x
                            }), m && a.jsx(j0, {
                                className: "w-3.5 h-3.5 text-orange-400"
                            })]
                        })]
                    }), a.jsx("div", {
                        className: "mt-2.5 pt-2 border-t border-slate-100/20 flex flex-wrap gap-1",
                        children: g.articles.map(w => a.jsx("span", {
                            className: `text-[9px] px-1.5 py-0.5 rounded font-mono ${m ? "bg-slate-800 text-slate-300 border border-slate-700" : "bg-slate-100 text-slate-600"}`,
                            children: w
                        }, w))
                    })]
                }, g.id)
            }
            )
        })]
    })
}
  , ex = ({isOpen: i, onClose: s, schemeName: l, totalScore: u, breakdown: d}) => {
    if (!i)
        return null;
    const f = [{
        label: "Criteria Match Strength",
        score: d.matchStrength,
        max: 40,
        description: "Proportion of scheme eligibility rules fully satisfied by your answers.",
        color: "bg-emerald-500"
    }, {
        label: "Constitutional Pillar / Need Fit",
        score: d.needFit,
        max: 25,
        description: "Alignment with your active pillar filters and category preferences.",
        color: "bg-blue-500"
    }, {
        label: "Benefit Impact Tier",
        score: d.benefitValue,
        max: 15,
        description: "Significance of monetary support, insurance, or livelihood assistance.",
        color: "bg-orange-500"
    }, {
        label: "Application Ease",
        score: d.ease,
        max: 10,
        description: "Simplicity of application steps, paperless eKYC and processing speed.",
        color: "bg-purple-500"
    }, {
        label: "Portal Openness",
        score: d.openness,
        max: 10,
        description: "Active enrollment status on the official Government portal.",
        color: "bg-amber-500"
    }];
    return a.jsx("div", {
        className: "fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-xs flex items-center justify-center p-4",
        children: a.jsxs("div", {
            className: "bg-white rounded-2xl max-w-md w-full p-6 shadow-xl border border-slate-200 animate-in fade-in zoom-in-95 duration-150",
            children: [a.jsxs("div", {
                className: "flex items-center justify-between pb-3 border-b border-slate-100",
                children: [a.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [a.jsx(Cf, {
                        className: "w-5 h-5 text-orange-600"
                    }), a.jsx("h3", {
                        className: "font-bold text-base text-slate-900",
                        children: "Why this Rank?"
                    })]
                }), a.jsx("button", {
                    onClick: s,
                    className: "p-1 text-slate-400 hover:text-slate-600 rounded-lg hover:bg-slate-100",
                    children: a.jsx(Of, {
                        className: "w-5 h-5"
                    })
                })]
            }), a.jsxs("div", {
                className: "py-4",
                children: [a.jsxs("p", {
                    className: "text-xs font-semibold text-slate-500 mb-1",
                    children: ["Scheme: ", a.jsx("span", {
                        className: "text-slate-900",
                        children: l
                    })]
                }), a.jsxs("div", {
                    className: "flex items-baseline gap-2 mb-4 bg-orange-50 p-3 rounded-xl border border-orange-200",
                    children: [a.jsx(Wd, {
                        className: "w-6 h-6 text-orange-600"
                    }), a.jsxs("div", {
                        children: [a.jsx("span", {
                            className: "text-2xl font-black text-orange-950",
                            children: u
                        }), a.jsx("span", {
                            className: "text-xs text-orange-700 font-bold ml-1",
                            children: "/ 100"
                        }), a.jsx("p", {
                            className: "text-[11px] text-orange-800",
                            children: "Deterministic algorithmic score (same answers always yield exact same ranking)."
                        })]
                    })]
                }), a.jsx("div", {
                    className: "space-y-3",
                    children: f.map(h => {
                        const g = Math.round(h.score / h.max * 100);
                        return a.jsxs("div", {
                            className: "text-xs",
                            children: [a.jsxs("div", {
                                className: "flex justify-between items-center mb-1",
                                children: [a.jsx("span", {
                                    className: "font-semibold text-slate-700",
                                    children: h.label
                                }), a.jsxs("span", {
                                    className: "font-bold text-slate-900",
                                    children: [h.score, " ", a.jsxs("span", {
                                        className: "text-slate-400 font-normal",
                                        children: ["/ ", h.max]
                                    })]
                                })]
                            }), a.jsx("div", {
                                className: "w-full h-2 bg-slate-100 rounded-full overflow-hidden",
                                children: a.jsx("div", {
                                    className: `h-full rounded-full ${h.color} transition-all duration-300`,
                                    style: {
                                        width: `${g}%`
                                    }
                                })
                            }), a.jsx("p", {
                                className: "text-[10px] text-slate-500 mt-0.5",
                                children: h.description
                            })]
                        }, h.label)
                    }
                    )
                })]
            }), a.jsx("div", {
                className: "mt-4 pt-3 border-t border-slate-100 flex justify-end",
                children: a.jsx("button", {
                    onClick: s,
                    className: "px-4 py-2 bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold rounded-xl transition-colors",
                    children: "Close Breakdown"
                })
            })]
        })
    })
}
  , tx = ({scheme: i, evaluation: s, isSelected: l=!1, onSelect: u}) => {
    var I;
    const {t: d, i18n: f} = Je()
      , h = f.language || "en"
      , {shortlist: g, toggleShortlist: m} = un()
      , [x,b] = O.useState(!1)
      , w = g.includes(i.id) || g.includes(i.slug)
      , v = i.name_i18n[h] || i.name_i18n.en || i.slug
      , R = i.benefit_i18n[h] || i.benefit_i18n.en
      , E = i.summary_i18n[h] || i.summary_i18n.en
      , P = ( () => {
        switch (s.verdict) {
        case "eligible":
            return {
                label: d("status.eligible"),
                bg: "bg-emerald-50 text-emerald-700 border-emerald-200",
                icon: mt
            };
        case "almost":
            return {
                label: d("status.almost"),
                bg: "bg-amber-50 text-amber-700 border-amber-200",
                icon: an
            };
        case "possible":
            return {
                label: d("status.possible"),
                bg: "bg-sky-50 text-sky-700 border-sky-200",
                icon: wl
            };
        default:
            return {
                label: d("status.not_eligible"),
                bg: "bg-slate-100 text-slate-600 border-slate-200",
                icon: xl
            }
        }
    }
    )()
      , $ = P.icon;
    return a.jsxs(a.Fragment, {
        children: [a.jsxs("div", {
            onClick: u,
            role: "button",
            tabIndex: 0,
            onKeyDown: V => {
                (V.key === "Enter" || V.key === " ") && (V.preventDefault(),
                u())
            }
            ,
            className: `group p-4 sm:p-5 rounded-2xl border text-left cursor-pointer transition-all duration-200 ${l ? "bg-white border-orange-500 shadow-md ring-2 ring-orange-500/20" : "bg-white hover:bg-slate-50/70 border-slate-200 shadow-xs hover:border-slate-300"}`,
            children: [a.jsxs("div", {
                className: "flex items-center justify-between gap-2 mb-2",
                children: [a.jsxs("div", {
                    className: "flex items-center flex-wrap gap-1.5",
                    children: [a.jsxs("span", {
                        className: `inline-flex items-center gap-1 text-[11px] font-bold px-2 py-0.5 rounded-full border ${P.bg}`,
                        children: [a.jsx($, {
                            className: "w-3.5 h-3.5"
                        }), a.jsx("span", {
                            children: P.label
                        })]
                    }), ((I = i.category) == null ? void 0 : I.pillar) && a.jsx("span", {
                        className: "text-[10px] font-semibold uppercase tracking-wider text-slate-500 bg-slate-100 px-2 py-0.5 rounded-full",
                        children: i.category.pillar
                    })]
                }), a.jsx("button", {
                    type: "button",
                    onClick: V => {
                        V.stopPropagation(),
                        m(i.id)
                    }
                    ,
                    title: w ? "Remove from shortlist" : "Save to shortlist",
                    className: `p-1.5 rounded-lg border transition-colors ${w ? "bg-orange-50 text-orange-600 border-orange-200" : "text-slate-400 hover:text-slate-600 border-transparent hover:border-slate-200"}`,
                    children: a.jsx(Gr, {
                        className: `w-4 h-4 ${w ? "fill-orange-600" : ""}`
                    })
                })]
            }), a.jsx("h4", {
                className: "font-bold text-base text-slate-900 group-hover:text-orange-950 transition-colors mb-1.5 leading-snug",
                children: v
            }), a.jsx("p", {
                className: "text-xs text-slate-600 line-clamp-2 leading-relaxed mb-3",
                children: E
            }), a.jsxs("div", {
                className: "bg-slate-50 p-2.5 rounded-xl border border-slate-200/80 mb-3 text-xs flex items-baseline gap-1.5",
                children: [a.jsx("span", {
                    className: "font-bold text-slate-900 shrink-0",
                    children: "Benefit:"
                }), a.jsx("span", {
                    className: "text-slate-700 truncate",
                    children: R
                })]
            }), a.jsxs("div", {
                className: "flex items-center justify-between pt-2 border-t border-slate-100 text-xs",
                children: [a.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [a.jsx("span", {
                        className: "text-slate-500 font-medium",
                        children: "Relevance:"
                    }), a.jsxs("span", {
                        className: "font-extrabold text-slate-900 bg-slate-100 px-2 py-0.5 rounded-md",
                        children: [s.relevanceScore, "/100"]
                    }), a.jsxs("button", {
                        type: "button",
                        onClick: V => {
                            V.stopPropagation(),
                            b(!0)
                        }
                        ,
                        title: "View deterministic score breakdown",
                        className: "text-[11px] text-orange-600 hover:text-orange-700 font-semibold inline-flex items-center gap-1 hover:underline",
                        children: [a.jsx(Cf, {
                            className: "w-3 h-3"
                        }), a.jsx("span", {
                            children: "Why?"
                        })]
                    })]
                }), a.jsxs("div", {
                    className: "flex items-center gap-1 text-slate-400 group-hover:text-orange-600 text-xs font-semibold",
                    children: [a.jsx("span", {
                        children: "Details"
                    }), a.jsx(k0, {
                        className: "w-4 h-4 group-hover:translate-x-0.5 transition-transform"
                    })]
                })]
            })]
        }), a.jsx(ex, {
            isOpen: x,
            onClose: () => b(!1),
            schemeName: v,
            totalScore: s.relevanceScore,
            breakdown: s.scoreBreakdown
        })]
    })
}
  , Tf = ({scheme: i, evaluation: s, onClose: l, initialTab: u="documents"}) => {
    var se;
    const {t: d, i18n: f} = Je()
      , h = f.language || "en"
      , {shortlist: g, toggleShortlist: m} = un()
      , [x,b] = O.useState(u)
      , [w,v] = O.useState({})
      , R = g.includes(i.id) || g.includes(i.slug)
      , E = i.name_i18n[h] || i.name_i18n.en || i.slug
      , _ = i.benefit_i18n[h] || i.benefit_i18n.en
      , P = i.summary_i18n[h] || i.summary_i18n.en
      , $ = i.scheme_documents || []
      , I = i.scheme_steps || []
      , V = K => {
        v(te => ({
            ...te,
            [K]: !te[K]
        }))
    }
      , H = () => {
        window.print()
    }
    ;
    return a.jsxs("div", {
        className: "bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden text-slate-800",
        children: [a.jsxs("div", {
            className: "p-4 sm:p-6 border-b border-slate-100 bg-slate-50/70",
            children: [a.jsxs("div", {
                className: "flex items-center justify-between gap-3 mb-2",
                children: [a.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [a.jsxs("span", {
                        className: "text-xs font-bold uppercase tracking-wider text-orange-600 bg-orange-50 px-2.5 py-1 rounded-md border border-orange-200",
                        children: [i.level.toUpperCase(), " SCHEME"]
                    }), ((se = i.category) == null ? void 0 : se.pillar) && a.jsx("span", {
                        className: "text-xs font-semibold text-slate-600 bg-slate-200/80 px-2.5 py-1 rounded-md",
                        children: i.category.pillar.toUpperCase()
                    })]
                }), a.jsxs("div", {
                    className: "flex items-center gap-1.5 sm:gap-2",
                    children: [a.jsxs("button", {
                        type: "button",
                        onClick: () => m(i.id),
                        className: `inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold rounded-xl border transition-colors ${R ? "bg-orange-50 text-orange-600 border-orange-200" : "bg-white text-slate-700 hover:bg-slate-100 border-slate-200"}`,
                        children: [a.jsx(Gr, {
                            className: `w-3.5 h-3.5 ${R ? "fill-orange-600" : ""}`
                        }), a.jsx("span", {
                            children: d(R ? "scheme.saved" : "scheme.save")
                        })]
                    }), a.jsxs("button", {
                        type: "button",
                        onClick: H,
                        title: "Print checklist",
                        className: "inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold bg-white hover:bg-slate-100 text-slate-700 rounded-xl border border-slate-200 transition-colors",
                        children: [a.jsx(vf, {
                            className: "w-3.5 h-3.5 text-slate-600"
                        }), a.jsx("span", {
                            className: "hidden sm:inline",
                            children: "Print"
                        })]
                    }), l && a.jsx("button", {
                        type: "button",
                        onClick: l,
                        title: "Close Details",
                        className: "p-1.5 text-slate-400 hover:text-slate-700 hover:bg-slate-200 rounded-xl transition-colors ml-1",
                        children: a.jsx(Of, {
                            className: "w-5 h-5"
                        })
                    })]
                })]
            }), a.jsx("h2", {
                className: "text-xl sm:text-2xl font-extrabold text-slate-900 leading-snug",
                children: E
            }), a.jsx("p", {
                className: "text-xs sm:text-sm text-slate-600 mt-2 leading-relaxed",
                children: P
            }), a.jsx("div", {
                className: "mt-3 flex items-center gap-3",
                children: a.jsxs(Ue, {
                    to: `/scheme/${i.slug}`,
                    className: "text-xs font-semibold text-orange-600 hover:text-orange-700 inline-flex items-center gap-1 hover:underline",
                    children: [a.jsx("span", {
                        children: "Open in dedicated full page"
                    }), a.jsx(Oa, {
                        className: "w-3.5 h-3.5"
                    })]
                })
            })]
        }), a.jsx("div", {
            className: "bg-slate-100 p-2 border-b border-slate-200",
            children: a.jsxs("div", {
                className: "flex items-center gap-1 overflow-x-auto text-xs font-bold scrollbar-none",
                children: [a.jsxs("button", {
                    type: "button",
                    onClick: () => b("documents"),
                    className: `px-3 py-2 rounded-xl transition-all flex items-center gap-1.5 shrink-0 ${x === "documents" ? "bg-white text-orange-700 shadow-xs border border-orange-200 ring-1 ring-orange-500/20" : "text-slate-600 hover:text-slate-900 hover:bg-white/60"}`,
                    children: [a.jsx(Ta, {
                        className: "w-3.5 h-3.5 text-orange-600"
                    }), a.jsx("span", {
                        children: "Required Documents"
                    }), a.jsx("span", {
                        className: `px-1.5 py-0.2 rounded-full text-[10px] ${x === "documents" ? "bg-orange-100 text-orange-800" : "bg-slate-200 text-slate-700"}`,
                        children: $.length
                    })]
                }), a.jsxs("button", {
                    type: "button",
                    onClick: () => b("steps"),
                    className: `px-3 py-2 rounded-xl transition-all flex items-center gap-1.5 shrink-0 ${x === "steps" ? "bg-white text-orange-700 shadow-xs border border-orange-200 ring-1 ring-orange-500/20" : "text-slate-600 hover:text-slate-900 hover:bg-white/60"}`,
                    children: [a.jsx(yd, {
                        className: "w-3.5 h-3.5 text-orange-600"
                    }), a.jsx("span", {
                        children: "How to Apply"
                    }), a.jsx("span", {
                        className: `px-1.5 py-0.2 rounded-full text-[10px] ${x === "steps" ? "bg-orange-100 text-orange-800" : "bg-slate-200 text-slate-700"}`,
                        children: I.length
                    })]
                }), a.jsxs("button", {
                    type: "button",
                    onClick: () => b("eligibility"),
                    className: `px-3 py-2 rounded-xl transition-all flex items-center gap-1.5 shrink-0 ${x === "eligibility" ? "bg-white text-orange-700 shadow-xs border border-orange-200 ring-1 ring-orange-500/20" : "text-slate-600 hover:text-slate-900 hover:bg-white/60"}`,
                    children: [a.jsx(mt, {
                        className: "w-3.5 h-3.5 text-orange-600"
                    }), a.jsx("span", {
                        children: "Eligibility"
                    })]
                }), a.jsxs("button", {
                    type: "button",
                    onClick: () => b("benefits"),
                    className: `px-3 py-2 rounded-xl transition-all flex items-center gap-1.5 shrink-0 ${x === "benefits" ? "bg-white text-orange-700 shadow-xs border border-orange-200 ring-1 ring-orange-500/20" : "text-slate-600 hover:text-slate-900 hover:bg-white/60"}`,
                    children: [a.jsx(an, {
                        className: "w-3.5 h-3.5 text-orange-600"
                    }), a.jsx("span", {
                        children: "Benefits"
                    })]
                }), a.jsxs("button", {
                    type: "button",
                    onClick: () => b("all"),
                    className: `px-3 py-2 rounded-xl transition-all flex items-center gap-1.5 shrink-0 ml-auto ${x === "all" ? "bg-slate-800 text-white shadow-xs" : "text-slate-600 hover:text-slate-900 hover:bg-white/60"}`,
                    children: [a.jsx(O0, {
                        className: "w-3.5 h-3.5"
                    }), a.jsx("span", {
                        children: "All"
                    })]
                })]
            })
        }), a.jsxs("div", {
            className: "p-4 sm:p-6 space-y-6",
            children: [a.jsxs("div", {
                className: `p-4 rounded-xl border flex items-start gap-3 ${s.verdict === "eligible" ? "bg-emerald-50 border-emerald-200 text-emerald-950" : s.verdict === "almost" ? "bg-amber-50 border-amber-200 text-amber-950" : s.verdict === "possible" ? "bg-sky-50 border-sky-200 text-sky-950" : "bg-slate-100 border-slate-200 text-slate-800"}`,
                children: [s.verdict === "eligible" ? a.jsx(mt, {
                    className: "w-5 h-5 text-emerald-600 shrink-0 mt-0.5"
                }) : s.verdict === "almost" ? a.jsx(an, {
                    className: "w-5 h-5 text-amber-600 shrink-0 mt-0.5"
                }) : s.verdict === "possible" ? a.jsx(wl, {
                    className: "w-5 h-5 text-sky-600 shrink-0 mt-0.5"
                }) : a.jsx(xl, {
                    className: "w-5 h-5 text-slate-600 shrink-0 mt-0.5"
                }), a.jsxs("div", {
                    children: [a.jsx("span", {
                        className: "font-bold text-sm block",
                        children: d(`status.${s.verdict}`)
                    }), a.jsx("p", {
                        className: "text-xs mt-0.5 opacity-90 leading-relaxed",
                        children: d(`statusDesc.${s.verdict}`)
                    })]
                })]
            }), (x === "documents" || x === "all") && a.jsxs("div", {
                className: "space-y-3 animate-in fade-in duration-150",
                children: [a.jsxs("div", {
                    className: "flex items-center justify-between pb-1 border-b border-slate-100",
                    children: [a.jsxs("h4", {
                        className: "text-sm font-bold text-slate-900 flex items-center gap-2",
                        children: [a.jsx(Ta, {
                            className: "w-4 h-4 text-orange-600"
                        }), a.jsx("span", {
                            children: d("scheme.documents")
                        }), a.jsxs("span", {
                            className: "text-xs bg-orange-100 text-orange-800 px-2 py-0.5 rounded-full font-bold",
                            children: [$.length, " Required"]
                        })]
                    }), a.jsx("span", {
                        className: "text-[11px] text-slate-500 font-medium",
                        children: "Tap to check off"
                    })]
                }), $.length === 0 ? a.jsx("p", {
                    className: "text-xs text-slate-500 bg-slate-50 p-4 rounded-xl border border-slate-200",
                    children: "No specific documents listed for this scheme. Standard government photo ID (Aadhaar/Voter ID) applies."
                }) : a.jsx("div", {
                    className: "space-y-2",
                    children: $.map(K => {
                        const te = K.name_i18n[h] || K.name_i18n.en
                          , ee = K.hint_i18n ? K.hint_i18n[h] || K.hint_i18n.en : null
                          , J = !!w[K.id];
                        return a.jsxs("div", {
                            onClick: () => V(K.id),
                            className: `p-3.5 rounded-xl border text-xs cursor-pointer transition-all flex items-start gap-3 select-none ${J ? "bg-emerald-50/70 border-emerald-300 ring-1 ring-emerald-400/20" : "bg-slate-50 hover:bg-slate-100/90 border-slate-200"}`,
                            children: [a.jsx("input", {
                                type: "checkbox",
                                checked: J,
                                onChange: () => {}
                                ,
                                className: "mt-0.5 rounded border-slate-300 text-emerald-600 focus:ring-emerald-500 w-4 h-4 cursor-pointer"
                            }), a.jsxs("div", {
                                className: "flex-1",
                                children: [a.jsxs("div", {
                                    className: "flex items-center gap-2 flex-wrap",
                                    children: [a.jsx("span", {
                                        className: `font-bold text-sm ${J ? "text-emerald-950 line-through" : "text-slate-900"}`,
                                        children: te
                                    }), K.mandatory ? a.jsx("span", {
                                        className: "text-[10px] font-bold text-rose-700 bg-rose-50 px-1.5 py-0.2 rounded border border-rose-200",
                                        children: "Mandatory"
                                    }) : a.jsx("span", {
                                        className: "text-[10px] font-medium text-slate-600 bg-slate-200 px-1.5 py-0.2 rounded",
                                        children: "Alternative"
                                    })]
                                }), ee && a.jsxs("p", {
                                    className: "text-[11px] text-slate-600 mt-1",
                                    children: [a.jsx("strong", {
                                        className: "text-slate-700",
                                        children: "Where to get:"
                                    }), " ", ee]
                                })]
                            })]
                        }, K.id)
                    }
                    )
                })]
            }), (x === "steps" || x === "all") && a.jsxs("div", {
                className: "space-y-3 animate-in fade-in duration-150",
                children: [a.jsxs("h4", {
                    className: "text-sm font-bold text-slate-900 flex items-center gap-2 pb-1 border-b border-slate-100",
                    children: [a.jsx(yd, {
                        className: "w-4 h-4 text-orange-600"
                    }), a.jsx("span", {
                        children: d("scheme.steps")
                    })]
                }), I.length === 0 ? a.jsx("p", {
                    className: "text-xs text-slate-500 bg-slate-50 p-4 rounded-xl border border-slate-200",
                    children: "Please follow application guidelines on the official portal link below."
                }) : a.jsx("div", {
                    className: "space-y-2.5",
                    children: I.map(K => {
                        const te = K.text_i18n[h] || K.text_i18n.en;
                        return a.jsxs("div", {
                            className: "flex items-start gap-3 text-xs bg-slate-50 p-3.5 rounded-xl border border-slate-200",
                            children: [a.jsx("span", {
                                className: "w-6 h-6 rounded-full bg-slate-900 text-white font-bold flex items-center justify-center text-xs shrink-0 mt-0.5",
                                children: K.sort
                            }), a.jsx("span", {
                                className: "text-slate-700 leading-relaxed font-medium",
                                children: te
                            })]
                        }, K.id)
                    }
                    )
                })]
            }), (x === "eligibility" || x === "all") && a.jsxs("div", {
                className: "space-y-4 animate-in fade-in duration-150",
                children: [a.jsxs("h4", {
                    className: "text-sm font-bold text-slate-900 flex items-center gap-2 pb-1 border-b border-slate-100",
                    children: [a.jsx(mt, {
                        className: "w-4 h-4 text-orange-600"
                    }), a.jsx("span", {
                        children: "Eligibility Evaluation"
                    })]
                }), s.nearRules.length > 0 && a.jsxs("div", {
                    className: "bg-amber-50/70 border border-amber-200 p-4 rounded-xl space-y-2",
                    children: [a.jsxs("div", {
                        className: "flex items-center gap-2 text-amber-900 font-bold text-xs",
                        children: [a.jsx(an, {
                            className: "w-4 h-4 text-amber-600"
                        }), a.jsx("span", {
                            children: d("scheme.nearMissTitle")
                        })]
                    }), s.nearRules.map(K => {
                        const te = d(K.reasonKey, {
                            value: K.actual,
                            limit: K.expected,
                            gap: K.gap
                        })
                          , ee = K.fixKey ? d(K.fixKey) : null;
                        return a.jsxs("div", {
                            className: "text-xs bg-white p-3 rounded-lg border border-amber-200/80",
                            children: [a.jsx("p", {
                                className: "text-slate-800 font-medium",
                                children: te
                            }), K.gap !== void 0 && a.jsxs("p", {
                                className: "text-amber-800 font-bold mt-1",
                                children: ["Gap: ", K.gap, " ", K.field === "incomeLakh" ? "Lakh" : "years"]
                            }), ee && a.jsxs("div", {
                                className: "mt-2 text-slate-600 bg-amber-50/50 p-2 rounded flex items-center gap-1.5 font-medium",
                                children: [a.jsx(Cn, {
                                    className: "w-3.5 h-3.5 text-amber-600 shrink-0"
                                }), a.jsxs("span", {
                                    children: ["Action: ", ee]
                                })]
                            })]
                        }, K.id)
                    }
                    )]
                }), s.failedRules.length > 0 && a.jsxs("div", {
                    className: "bg-rose-50/60 border border-rose-200 p-4 rounded-xl space-y-2",
                    children: [a.jsxs("div", {
                        className: "flex items-center gap-2 text-rose-900 font-bold text-xs",
                        children: [a.jsx(xl, {
                            className: "w-4 h-4 text-rose-600"
                        }), a.jsx("span", {
                            children: d("scheme.whyNotTitle")
                        })]
                    }), a.jsx("div", {
                        className: "space-y-1.5",
                        children: s.failedRules.map(K => {
                            const te = d(K.reasonKey, {
                                value: K.actual,
                                limit: K.expected
                            });
                            return a.jsxs("div", {
                                className: "text-xs bg-white p-2.5 rounded-lg border border-rose-100 flex items-start gap-2",
                                children: [a.jsx("span", {
                                    className: "text-rose-500 font-bold shrink-0",
                                    children: "✕"
                                }), a.jsx("span", {
                                    className: "text-slate-700",
                                    children: te
                                })]
                            }, K.id)
                        }
                        )
                    })]
                }), s.failedRules.length === 0 && s.nearRules.length === 0 && a.jsxs("div", {
                    className: "bg-emerald-50 border border-emerald-200 p-4 rounded-xl text-xs text-emerald-900 font-medium flex items-center gap-2",
                    children: [a.jsx(mt, {
                        className: "w-4 h-4 text-emerald-600 shrink-0"
                    }), a.jsx("span", {
                        children: "All listed eligibility criteria have been satisfied based on your answers!"
                    })]
                })]
            }), (x === "benefits" || x === "all") && a.jsxs("div", {
                className: "space-y-4 animate-in fade-in duration-150",
                children: [a.jsxs("h4", {
                    className: "text-sm font-bold text-slate-900 flex items-center gap-2 pb-1 border-b border-slate-100",
                    children: [a.jsx(an, {
                        className: "w-4 h-4 text-orange-600"
                    }), a.jsx("span", {
                        children: d("scheme.benefits")
                    })]
                }), a.jsx("div", {
                    className: "bg-gradient-to-r from-orange-50 to-amber-50 p-4 rounded-xl border border-orange-200",
                    children: a.jsx("p", {
                        className: "text-sm font-semibold text-slate-900 leading-relaxed",
                        children: _
                    })
                }), a.jsxs("div", {
                    className: "grid grid-cols-2 gap-3 text-xs",
                    children: [a.jsxs("div", {
                        className: "p-3 bg-slate-50 rounded-xl border border-slate-200",
                        children: [a.jsx("span", {
                            className: "text-slate-500 block",
                            children: "Benefit Impact:"
                        }), a.jsx("span", {
                            className: "font-bold text-slate-900",
                            children: i.benefit_tier === 3 ? "High (₹5 Lakh+ / Enterprise)" : i.benefit_tier === 2 ? "Medium (Direct Cash / Pension)" : "Standard"
                        })]
                    }), a.jsxs("div", {
                        className: "p-3 bg-slate-50 rounded-xl border border-slate-200",
                        children: [a.jsx("span", {
                            className: "text-slate-500 block",
                            children: "Application Ease:"
                        }), a.jsx("span", {
                            className: "font-bold text-slate-900",
                            children: i.ease === 3 ? "Easy (Paperless / CSC / Online)" : i.ease === 2 ? "Moderate" : "Standard Document Review"
                        })]
                    })]
                })]
            }), a.jsx("div", {
                className: "pt-2",
                children: a.jsxs("a", {
                    href: i.apply_url,
                    target: "_blank",
                    rel: "noopener noreferrer",
                    className: "w-full inline-flex items-center justify-center gap-2 py-3.5 px-6 bg-orange-600 hover:bg-orange-700 text-white font-bold text-sm rounded-xl shadow transition-colors",
                    children: [a.jsx("span", {
                        children: d("scheme.applyNow")
                    }), a.jsx(Oa, {
                        className: "w-4 h-4"
                    })]
                })
            }), a.jsxs("div", {
                className: "pt-4 border-t border-slate-100 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs text-slate-500",
                children: [i.articles && i.articles.length > 0 && a.jsxs("div", {
                    className: "flex items-center gap-1.5 flex-wrap",
                    children: [a.jsx(Zr, {
                        className: "w-3.5 h-3.5 text-slate-400"
                    }), a.jsxs("span", {
                        className: "font-semibold text-slate-600",
                        children: [d("scheme.articles"), ":"]
                    }), i.articles.map(K => a.jsxs("span", {
                        className: "bg-slate-100 text-slate-700 px-1.5 py-0.5 rounded font-mono text-[10px]",
                        children: ["Art. ", K]
                    }, K))]
                }), a.jsxs("div", {
                    className: "flex items-center gap-3",
                    children: [a.jsxs("span", {
                        className: "inline-flex items-center gap-1 text-slate-400 text-[11px]",
                        children: [a.jsx(Jd, {
                            className: "w-3.5 h-3.5"
                        }), a.jsxs("span", {
                            children: [d("scheme.lastVerified"), ": ", i.last_verified]
                        })]
                    }), a.jsxs("a", {
                        href: i.source_url,
                        target: "_blank",
                        rel: "noopener noreferrer",
                        className: "text-orange-600 hover:text-orange-700 font-semibold inline-flex items-center gap-1 text-[11px]",
                        children: [a.jsx(Yd, {
                            className: "w-3.5 h-3.5"
                        }), a.jsx("span", {
                            children: d("scheme.source")
                        })]
                    })]
                })]
            })]
        })]
    })
}
  , nx = () => {
    const {t: i, i18n: s} = Je()
      , l = s.language || "en"
      , u = rr()
      , {profile: d, resetProfile: f, setProfileField: h, selectedPillars: g, searchQuery: m, setSearchQuery: x} = _t()
      , [b,w] = O.useState([])
      , [v,R] = O.useState(!0)
      , [E,_] = O.useState("eligible")
      , [P,$] = O.useState(null);
    O.useEffect( () => {
        bl().then(J => {
            w(J.schemes),
            R(!1)
        }
        )
    }
    , []);
    const I = O.useMemo( () => g.length === 0 ? b : b.filter(J => J.category && g.includes(J.category.pillar)), [b, g])
      , {evaluations: V, grouped: H} = O.useMemo( () => J0(I, d), [I, d])
      , se = O.useMemo( () => {
        const J = H[E] || [];
        if (!m.trim())
            return J;
        const ue = m.toLowerCase();
        return J.filter(ce => {
            const me = b.find(Pe => Pe.slug === ce.slug);
            if (!me)
                return !1;
            const De = (me.name_i18n[l] || me.name_i18n.en || "").toLowerCase()
              , je = (me.summary_i18n[l] || me.summary_i18n.en || "").toLowerCase();
            return De.includes(ue) || je.includes(ue) || me.category_id.includes(ue)
        }
        )
    }
    , [H, E, m, b, l]);
    O.useEffect( () => {
        se.length > 0 ? (!P || !se.some(J => J.slug === P)) && $(se[0].slug) : $(null)
    }
    , [se, P]),
    O.useEffect( () => {
        H.eligible.length > 0 ? _("eligible") : H.almost.length > 0 ? _("almost") : H.possible.length > 0 ? _("possible") : H.not_eligible.length > 0 && _("not_eligible")
    }
    , [b.length]);
    const K = V.find(J => J.slug === P)
      , te = b.find(J => J.slug === P)
      , ee = () => {
        window.confirm("Clear all responses? All information will be wiped immediately.") && (f(),
        u("/find"))
    }
    ;
    return v ? a.jsxs("div", {
        className: "min-h-[60vh] flex flex-col items-center justify-center",
        children: [a.jsx("div", {
            className: "w-10 h-10 border-4 border-orange-500 border-t-transparent rounded-full animate-spin mb-3"
        }), a.jsx("p", {
            className: "text-xs text-slate-500 font-medium",
            children: "Loading verified government schemes..."
        })]
    }) : a.jsx("div", {
        className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6",
        children: a.jsxs("div", {
            className: "grid grid-cols-1 lg:grid-cols-12 gap-6 items-start",
            children: [a.jsx("div", {
                className: "lg:col-span-2",
                children: a.jsx(Z0, {
                    schemes: b
                })
            }), a.jsx("div", {
                className: "lg:col-span-3 space-y-4",
                children: a.jsxs("div", {
                    className: "bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-xs space-y-4",
                    children: [a.jsxs("div", {
                        className: "flex items-center justify-between pb-3 border-b border-slate-100",
                        children: [a.jsx("h3", {
                            className: "text-xs font-bold uppercase tracking-wider text-slate-500",
                            children: "A. Your Details"
                        }), a.jsxs("div", {
                            className: "flex items-center gap-1",
                            children: [a.jsxs("button", {
                                onClick: () => u("/find"),
                                className: "p-1.5 text-slate-500 hover:text-slate-800 hover:bg-slate-100 rounded-lg text-xs font-semibold inline-flex items-center gap-1",
                                title: "Edit Answers",
                                children: [a.jsx(T0, {
                                    className: "w-3.5 h-3.5"
                                }), a.jsx("span", {
                                    children: "Edit"
                                })]
                            }), a.jsx("button", {
                                onClick: ee,
                                className: "p-1.5 text-rose-600 hover:text-rose-700 hover:bg-rose-50 rounded-lg text-xs font-semibold inline-flex items-center gap-1",
                                title: "Clear Answers",
                                children: a.jsx(Fa, {
                                    className: "w-3.5 h-3.5"
                                })
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "flex flex-wrap gap-1.5 text-xs",
                        children: [d.age !== void 0 && a.jsxs("span", {
                            className: "bg-slate-100 text-slate-800 px-2.5 py-1 rounded-lg font-medium",
                            children: ["Age: ", a.jsx("strong", {
                                children: d.age
                            })]
                        }), d.gender && a.jsx("span", {
                            className: "bg-slate-100 text-slate-800 px-2.5 py-1 rounded-lg font-medium capitalize",
                            children: d.gender
                        }), d.state && a.jsx("span", {
                            className: "bg-slate-100 text-slate-800 px-2.5 py-1 rounded-lg font-medium",
                            children: d.state
                        }), d.residence && a.jsx("span", {
                            className: "bg-slate-100 text-slate-800 px-2.5 py-1 rounded-lg font-medium capitalize",
                            children: d.residence
                        }), d.incomeLakh !== void 0 && a.jsxs("span", {
                            className: "bg-slate-100 text-slate-800 px-2.5 py-1 rounded-lg font-medium",
                            children: ["Income: ", a.jsxs("strong", {
                                children: ["₹", d.incomeLakh, "L"]
                            })]
                        }), d.occupation && d.occupation.length > 0 && a.jsx("span", {
                            className: "bg-slate-100 text-slate-800 px-2.5 py-1 rounded-lg font-medium capitalize",
                            children: d.occupation.join(", ")
                        })]
                    }), a.jsxs("div", {
                        className: "pt-3 border-t border-slate-100 space-y-3",
                        children: [a.jsxs("div", {
                            className: "flex items-center gap-1.5 text-xs font-bold text-slate-800",
                            children: [a.jsx(M0, {
                                className: "w-3.5 h-3.5 text-orange-600"
                            }), a.jsx("span", {
                                children: i("wizard.refineTitle")
                            })]
                        }), a.jsx("p", {
                            className: "text-[11px] text-slate-500 leading-tight",
                            children: i("wizard.refineDesc")
                        }), a.jsxs("div", {
                            className: "space-y-3 text-xs pt-1",
                            children: [a.jsxs("div", {
                                children: [a.jsx("label", {
                                    className: "text-slate-600 block mb-1 font-medium",
                                    children: i("refine.bpl")
                                }), a.jsxs("div", {
                                    className: "grid grid-cols-2 gap-1.5",
                                    children: [a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("bpl", d.bpl === "yes" ? void 0 : "yes"),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.bpl === "yes" ? "bg-orange-600 text-white border-orange-600" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.bplYes")
                                    }), a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("bpl", d.bpl === "no" ? void 0 : "no"),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.bpl === "no" ? "bg-slate-800 text-white border-slate-800" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.bplNo")
                                    })]
                                })]
                            }), a.jsxs("div", {
                                children: [a.jsx("label", {
                                    className: "text-slate-600 block mb-1 font-medium",
                                    children: i("refine.land")
                                }), a.jsxs("div", {
                                    className: "grid grid-cols-2 gap-1.5",
                                    children: [a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("landOwner", d.landOwner === !0 ? void 0 : !0),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.landOwner === !0 ? "bg-orange-600 text-white border-orange-600" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.landYes")
                                    }), a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("landOwner", d.landOwner === !1 ? void 0 : !1),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.landOwner === !1 ? "bg-slate-800 text-white border-slate-800" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.landNo")
                                    })]
                                })]
                            }), a.jsxs("div", {
                                children: [a.jsx("label", {
                                    className: "text-slate-600 block mb-1 font-medium",
                                    children: i("refine.category")
                                }), a.jsx("div", {
                                    className: "grid grid-cols-4 gap-1",
                                    children: ["general", "obc", "sc", "st"].map(J => a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("category", d.category === J ? void 0 : J),
                                        className: `py-1.5 rounded-lg border text-center font-bold uppercase transition-colors ${d.category === J ? "bg-orange-600 text-white border-orange-600" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: J
                                    }, J))
                                })]
                            }), a.jsxs("div", {
                                children: [a.jsx("label", {
                                    className: "text-slate-600 block mb-1 font-medium",
                                    children: i("refine.bank")
                                }), a.jsxs("div", {
                                    className: "grid grid-cols-2 gap-1.5",
                                    children: [a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("hasBankAccount", d.hasBankAccount === !0 ? void 0 : !0),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.hasBankAccount === !0 ? "bg-orange-600 text-white border-orange-600" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.bankYes")
                                    }), a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("hasBankAccount", d.hasBankAccount === !1 ? void 0 : !1),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.hasBankAccount === !1 ? "bg-slate-800 text-white border-slate-800" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.bankNo")
                                    })]
                                })]
                            }), a.jsxs("div", {
                                children: [a.jsx("label", {
                                    className: "text-slate-600 block mb-1 font-medium",
                                    children: i("refine.daughter")
                                }), a.jsxs("div", {
                                    className: "grid grid-cols-2 gap-1.5",
                                    children: [a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("daughterUnder10", d.daughterUnder10 === !0 ? void 0 : !0),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.daughterUnder10 === !0 ? "bg-orange-600 text-white border-orange-600" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.daughterYes")
                                    }), a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("daughterUnder10", d.daughterUnder10 === !1 ? void 0 : !1),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.daughterUnder10 === !1 ? "bg-slate-800 text-white border-slate-800" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.daughterNo")
                                    })]
                                })]
                            }), a.jsxs("div", {
                                children: [a.jsx("label", {
                                    className: "text-slate-600 block mb-1 font-medium",
                                    children: i("refine.pregnant")
                                }), a.jsxs("div", {
                                    className: "grid grid-cols-2 gap-1.5",
                                    children: [a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("pregnantOrNursing", d.pregnantOrNursing === !0 ? void 0 : !0),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.pregnantOrNursing === !0 ? "bg-orange-600 text-white border-orange-600" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.pregnantYes")
                                    }), a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("pregnantOrNursing", d.pregnantOrNursing === !1 ? void 0 : !1),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.pregnantOrNursing === !1 ? "bg-slate-800 text-white border-slate-800" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.pregnantNo")
                                    })]
                                })]
                            }), a.jsxs("div", {
                                children: [a.jsx("label", {
                                    className: "text-slate-600 block mb-1 font-medium",
                                    children: i("refine.taxpayer")
                                }), a.jsxs("div", {
                                    className: "grid grid-cols-2 gap-1.5",
                                    children: [a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("incomeTaxPayer", d.incomeTaxPayer === !1 ? void 0 : !1),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.incomeTaxPayer === !1 ? "bg-emerald-600 text-white border-emerald-600" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.taxpayerNo")
                                    }), a.jsx("button", {
                                        type: "button",
                                        onClick: () => h("incomeTaxPayer", d.incomeTaxPayer === !0 ? void 0 : !0),
                                        className: `py-1.5 px-2 rounded-lg border text-center font-semibold transition-colors ${d.incomeTaxPayer === !0 ? "bg-slate-800 text-white border-slate-800" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                                        children: i("refine.taxpayerYes")
                                    })]
                                })]
                            })]
                        })]
                    })]
                })
            }), a.jsxs("div", {
                className: "lg:col-span-3 space-y-4",
                children: [a.jsxs("div", {
                    className: "bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-xs space-y-3",
                    children: [a.jsxs("div", {
                        className: "flex items-center justify-between",
                        children: [a.jsx("h3", {
                            className: "text-xs font-bold uppercase tracking-wider text-slate-500",
                            children: "B. Your Schemes"
                        }), a.jsxs("span", {
                            className: "text-xs font-bold text-slate-700",
                            children: [se.length, " total"]
                        })]
                    }), a.jsxs("div", {
                        className: "relative",
                        children: [a.jsx(z0, {
                            className: "w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"
                        }), a.jsx("input", {
                            type: "text",
                            placeholder: "Search schemes or benefits...",
                            value: m,
                            onChange: J => x(J.target.value),
                            className: "w-full pl-8 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-1 focus:ring-orange-500"
                        })]
                    }), a.jsxs("div", {
                        className: "grid grid-cols-2 gap-1.5 pt-1",
                        children: [a.jsxs("button", {
                            type: "button",
                            onClick: () => _("eligible"),
                            className: `py-2 px-2.5 rounded-xl text-xs font-bold flex items-center justify-between border transition-all ${E === "eligible" ? "bg-emerald-600 text-white border-emerald-600 shadow-xs" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                            children: [a.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [a.jsx(mt, {
                                    className: "w-3.5 h-3.5"
                                }), a.jsx("span", {
                                    children: i("status.eligible")
                                })]
                            }), a.jsx("span", {
                                className: `px-1.5 py-0.2 rounded-full text-[10px] ${E === "eligible" ? "bg-white/25 text-white" : "bg-slate-200 text-slate-800"}`,
                                children: H.eligible.length
                            })]
                        }), a.jsxs("button", {
                            type: "button",
                            onClick: () => _("almost"),
                            className: `py-2 px-2.5 rounded-xl text-xs font-bold flex items-center justify-between border transition-all ${E === "almost" ? "bg-amber-600 text-white border-amber-600 shadow-xs" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                            children: [a.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [a.jsx(an, {
                                    className: "w-3.5 h-3.5"
                                }), a.jsx("span", {
                                    children: i("status.almost")
                                })]
                            }), a.jsx("span", {
                                className: `px-1.5 py-0.2 rounded-full text-[10px] ${E === "almost" ? "bg-white/25 text-white" : "bg-slate-200 text-slate-800"}`,
                                children: H.almost.length
                            })]
                        }), a.jsxs("button", {
                            type: "button",
                            onClick: () => _("possible"),
                            className: `py-2 px-2.5 rounded-xl text-xs font-bold flex items-center justify-between border transition-all ${E === "possible" ? "bg-sky-600 text-white border-sky-600 shadow-xs" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                            children: [a.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [a.jsx(wl, {
                                    className: "w-3.5 h-3.5"
                                }), a.jsx("span", {
                                    children: i("status.possible")
                                })]
                            }), a.jsx("span", {
                                className: `px-1.5 py-0.2 rounded-full text-[10px] ${E === "possible" ? "bg-white/25 text-white" : "bg-slate-200 text-slate-800"}`,
                                children: H.possible.length
                            })]
                        }), a.jsxs("button", {
                            type: "button",
                            onClick: () => _("not_eligible"),
                            className: `py-2 px-2.5 rounded-xl text-xs font-bold flex items-center justify-between border transition-all ${E === "not_eligible" ? "bg-slate-800 text-white border-slate-800 shadow-xs" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100"}`,
                            children: [a.jsxs("span", {
                                className: "flex items-center gap-1.5",
                                children: [a.jsx(xl, {
                                    className: "w-3.5 h-3.5"
                                }), a.jsx("span", {
                                    children: i("status.not_eligible")
                                })]
                            }), a.jsx("span", {
                                className: `px-1.5 py-0.2 rounded-full text-[10px] ${E === "not_eligible" ? "bg-white/25 text-white" : "bg-slate-200 text-slate-800"}`,
                                children: H.not_eligible.length
                            })]
                        })]
                    })]
                }), a.jsx("div", {
                    className: "space-y-3",
                    children: se.length === 0 ? a.jsxs("div", {
                        className: "bg-white rounded-2xl p-6 text-center border border-slate-200",
                        children: [a.jsx("p", {
                            className: "text-xs text-slate-500 font-medium",
                            children: "No schemes in this group right now."
                        }), a.jsx("p", {
                            className: "text-[11px] text-slate-400 mt-1",
                            children: "Try answering the refine questions in Column A or switching tabs."
                        })]
                    }) : se.map(J => {
                        const ue = b.find(ce => ce.slug === J.slug);
                        return ue ? a.jsx(tx, {
                            scheme: ue,
                            evaluation: J,
                            isSelected: P === ue.slug,
                            onSelect: () => $(ue.slug)
                        }, ue.slug) : null
                    }
                    )
                })]
            }), a.jsx("div", {
                className: "lg:col-span-4 sticky top-20",
                children: te && K ? a.jsx(Tf, {
                    scheme: te,
                    evaluation: K
                }) : a.jsx("div", {
                    className: "bg-white rounded-2xl p-8 text-center border border-slate-200 text-slate-400",
                    children: a.jsx("p", {
                        className: "text-xs font-semibold",
                        children: "Select a scheme from Column B to inspect required documents and application steps."
                    })
                })
            })]
        })
    })
}
  , rx = () => {
    const {slug: i} = mm()
      , {t: s} = Je()
      , l = rr()
      , {profile: u} = _t()
      , [d,f] = O.useState([])
      , [h,g] = O.useState(!0);
    O.useEffect( () => {
        bl().then(w => {
            f(w.schemes),
            g(!1)
        }
        )
    }
    , []);
    const m = d.find(w => w.slug === i);
    if (h)
        return a.jsx("div", {
            className: "min-h-[50vh] flex items-center justify-center",
            children: a.jsx("div", {
                className: "w-8 h-8 border-4 border-orange-500 border-t-transparent rounded-full animate-spin"
            })
        });
    if (!m)
        return a.jsxs("div", {
            className: "max-w-2xl mx-auto px-4 py-16 text-center space-y-4",
            children: [a.jsx("h2", {
                className: "text-xl font-bold text-slate-800",
                children: "Scheme not found"
            }), a.jsx("p", {
                className: "text-xs text-slate-500",
                children: "The scheme you are looking for does not exist in our catalog."
            }), a.jsxs(Ue, {
                to: "/results",
                className: "inline-flex items-center gap-2 px-4 py-2 bg-orange-600 text-white rounded-xl text-xs font-bold",
                children: [a.jsx(Ra, {
                    className: "w-4 h-4"
                }), a.jsx("span", {
                    children: "Back to Schemes"
                })]
            })]
        });
    const x = Ua(m, u) || {
        schemeId: m.id,
        slug: m.slug,
        verdict: "possible",
        leaves: [],
        missingFields: [],
        failedRules: [],
        nearRules: [],
        relevanceScore: 50,
        scoreBreakdown: {
            matchStrength: 20,
            needFit: 12.5,
            benefitValue: 7.5,
            ease: 5,
            openness: 5,
            total: 50
        }
    }
      , b = Object.values(u).some(w => w !== void 0 && w !== "");
    return a.jsxs("div", {
        className: "max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6",
        children: [a.jsxs("div", {
            className: "flex items-center justify-between",
            children: [a.jsxs("button", {
                onClick: () => l(-1),
                className: "inline-flex items-center gap-1.5 text-xs font-bold text-slate-600 hover:text-slate-900",
                children: [a.jsx(Ra, {
                    className: "w-4 h-4"
                }), a.jsx("span", {
                    children: "Back"
                })]
            }), !b && a.jsxs(Ue, {
                to: "/find",
                className: "inline-flex items-center gap-1.5 px-3 py-1.5 bg-orange-50 text-orange-700 border border-orange-200 rounded-xl text-xs font-bold hover:bg-orange-100",
                children: [a.jsx(an, {
                    className: "w-3.5 h-3.5 text-orange-600"
                }), a.jsx("span", {
                    children: "Check My Eligibility"
                })]
            })]
        }), a.jsx(Tf, {
            scheme: m,
            evaluation: x
        })]
    })
}
  , sx = () => {
    const {t: i, i18n: s} = Je()
      , l = s.language || "en"
      , {shortlist: u, toggleShortlist: d, status: f} = un()
      , {profile: h} = _t()
      , [g,m] = O.useState([])
      , [x,b] = O.useState(!0);
    O.useEffect( () => {
        bl().then(E => {
            m(E.schemes),
            b(!1)
        }
        )
    }
    , []);
    const w = O.useMemo( () => g.filter(E => u.includes(E.id) || u.includes(E.slug)), [g, u])
      , v = O.useMemo( () => {
        const E = new Map;
        return w.forEach(_ => {
            var $;
            const P = _.name_i18n[l] || _.name_i18n.en || _.slug;
            ($ = _.scheme_documents) == null || $.forEach(I => {
                const V = I.name_i18n[l] || I.name_i18n.en
                  , H = V.toLowerCase().trim();
                if (E.has(H)) {
                    const se = E.get(H);
                    se.schemes.includes(P) || se.schemes.push(P),
                    I.mandatory && (se.mandatory = !0)
                } else
                    E.set(H, {
                        name: V,
                        hint: I.hint_i18n ? I.hint_i18n[l] || I.hint_i18n.en : void 0,
                        mandatory: I.mandatory,
                        schemes: [P]
                    })
            }
            )
        }
        ),
        Array.from(E.values())
    }
    , [w, l])
      , R = () => {
        window.print()
    }
    ;
    return x ? a.jsx("div", {
        className: "min-h-[50vh] flex items-center justify-center",
        children: a.jsx("div", {
            className: "w-8 h-8 border-4 border-orange-500 border-t-transparent rounded-full animate-spin"
        })
    }) : a.jsxs("div", {
        className: "max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8",
        children: [a.jsxs("div", {
            className: "flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 pb-6 border-b border-slate-200",
            children: [a.jsxs("div", {
                children: [a.jsxs("div", {
                    className: "flex items-center gap-2",
                    children: [a.jsx(Gr, {
                        className: "w-6 h-6 text-orange-600"
                    }), a.jsx("h1", {
                        className: "text-2xl sm:text-3xl font-extrabold text-slate-900",
                        children: i("nav.shortlist")
                    })]
                }), a.jsxs("p", {
                    className: "text-xs text-slate-500 mt-1",
                    children: [w.length, " schemes saved in your shortlist"]
                })]
            }), a.jsxs("div", {
                className: "flex items-center gap-3",
                children: [w.length > 0 && a.jsxs("button", {
                    onClick: R,
                    className: "inline-flex items-center gap-2 px-4 py-2 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-bold shadow transition-colors",
                    children: [a.jsx(vf, {
                        className: "w-4 h-4"
                    }), a.jsx("span", {
                        children: "Print Merged Checklist"
                    })]
                }), f !== "authenticated" && a.jsx(Ue, {
                    to: "/login",
                    className: "inline-flex items-center gap-1.5 px-3 py-2 bg-orange-50 text-orange-700 hover:bg-orange-100 rounded-xl text-xs font-bold border border-orange-200",
                    children: a.jsx("span", {
                        children: "Sync with Email"
                    })
                })]
            })]
        }), w.length === 0 ? a.jsxs("div", {
            className: "bg-white rounded-2xl p-12 text-center border border-slate-200 space-y-4",
            children: [a.jsx("div", {
                className: "w-12 h-12 rounded-full bg-orange-50 text-orange-600 flex items-center justify-center mx-auto",
                children: a.jsx(Gr, {
                    className: "w-6 h-6"
                })
            }), a.jsx("h3", {
                className: "text-base font-bold text-slate-900",
                children: "No schemes saved yet"
            }), a.jsx("p", {
                className: "text-xs text-slate-500 max-w-sm mx-auto",
                children: "Browse through your matched schemes and tap the bookmark star to save schemes for quick reference."
            }), a.jsxs(Ue, {
                to: "/results",
                className: "inline-flex items-center gap-2 px-5 py-2.5 bg-orange-600 hover:bg-orange-700 text-white text-xs font-bold rounded-xl transition-colors",
                children: [a.jsx("span", {
                    children: "Explore Schemes"
                }), a.jsx(Cn, {
                    className: "w-4 h-4"
                })]
            })]
        }) : a.jsxs("div", {
            className: "grid grid-cols-1 lg:grid-cols-3 gap-8 items-start",
            children: [a.jsxs("div", {
                className: "lg:col-span-1 space-y-3",
                children: [a.jsxs("h3", {
                    className: "text-xs font-bold uppercase tracking-wider text-slate-500",
                    children: ["Saved Schemes (", w.length, ")"]
                }), a.jsx("div", {
                    className: "space-y-2.5",
                    children: w.map(E => {
                        const _ = E.name_i18n[l] || E.name_i18n.en || E.slug
                          , P = Ua(E, h);
                        return a.jsxs("div", {
                            className: "p-3.5 bg-white rounded-xl border border-slate-200 shadow-xs flex items-center justify-between gap-3 text-xs",
                            children: [a.jsxs("div", {
                                className: "flex-1",
                                children: [a.jsx(Ue, {
                                    to: `/scheme/${E.slug}`,
                                    className: "font-bold text-slate-900 hover:text-orange-600 block line-clamp-1",
                                    children: _
                                }), P && a.jsxs("span", {
                                    className: "text-[10px] font-semibold text-emerald-700",
                                    children: ["Status: ", i(`status.${P.verdict}`)]
                                })]
                            }), a.jsx("button", {
                                onClick: () => d(E.id),
                                className: "p-1.5 text-slate-400 hover:text-rose-600 rounded-lg hover:bg-rose-50 transition-colors",
                                title: "Remove from shortlist",
                                children: a.jsx(za, {
                                    className: "w-3.5 h-3.5"
                                })
                            })]
                        }, E.id)
                    }
                    )
                })]
            }), a.jsxs("div", {
                className: "lg:col-span-2 print-sheet bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-6",
                children: [a.jsxs("div", {
                    className: "flex items-center justify-between pb-4 border-b border-slate-100",
                    children: [a.jsxs("div", {
                        children: [a.jsxs("h3", {
                            className: "text-base font-bold text-slate-900 flex items-center gap-2",
                            children: [a.jsx(P0, {
                                className: "w-5 h-5 text-orange-600"
                            }), a.jsx("span", {
                                children: "Consolidated Document Checklist"
                            })]
                        }), a.jsx("p", {
                            className: "text-xs text-slate-500 mt-0.5",
                            children: "Carry these papers to apply for all your saved schemes without duplicate visits."
                        })]
                    }), a.jsxs("span", {
                        className: "text-xs font-bold bg-slate-100 text-slate-700 px-2.5 py-1 rounded-lg",
                        children: [v.length, " Documents"]
                    })]
                }), a.jsx("div", {
                    className: "space-y-3",
                    children: v.map( (E, _) => a.jsxs("div", {
                        className: "p-3.5 rounded-xl border border-slate-200 bg-slate-50/50 flex items-start gap-3 text-xs",
                        children: [a.jsx("input", {
                            type: "checkbox",
                            className: "mt-0.5 rounded border-slate-300 text-emerald-600 focus:ring-emerald-500"
                        }), a.jsxs("div", {
                            className: "flex-1",
                            children: [a.jsxs("div", {
                                className: "flex items-center gap-2 flex-wrap",
                                children: [a.jsx("span", {
                                    className: "font-bold text-slate-900 text-sm",
                                    children: E.name
                                }), E.mandatory ? a.jsx("span", {
                                    className: "text-[10px] font-bold text-rose-700 bg-rose-50 px-1.5 py-0.2 rounded border border-rose-200",
                                    children: "Mandatory"
                                }) : a.jsx("span", {
                                    className: "text-[10px] font-semibold text-slate-500 bg-slate-200 px-1.5 py-0.2 rounded",
                                    children: "Alternative"
                                })]
                            }), E.hint && a.jsxs("p", {
                                className: "text-slate-500 text-[11px] mt-0.5",
                                children: ["Where to get: ", E.hint]
                            }), a.jsxs("div", {
                                className: "mt-1.5 flex items-center gap-1 flex-wrap text-[10px] text-slate-500",
                                children: [a.jsx("span", {
                                    children: "Needed for:"
                                }), E.schemes.map(P => a.jsx("span", {
                                    className: "bg-white text-slate-700 font-medium px-1.5 py-0.5 rounded border border-slate-200",
                                    children: P
                                }, P))]
                            })]
                        })]
                    }, _))
                }), a.jsxs("div", {
                    className: "pt-4 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-400",
                    children: [a.jsxs("span", {
                        children: ["Generated by Yojana Setu • Print date: ", new Date().toLocaleDateString()]
                    }), a.jsx("span", {
                        children: "Zero personal answers stored on server"
                    })]
                })]
            })]
        })]
    })
}
  , lx = () => {
    const {t: i} = Je()
      , s = rr()
      , {status: l, userEmail: u, requestOtp: d, verifyOtp: f, isLoading: h, errorMessage: g, clearError: m} = un()
      , [x,b] = O.useState(u || "")
      , [w,v] = O.useState("")
      , [R,E] = O.useState(0);
    O.useEffect( () => {
        l === "authenticated" && s("/shortlist")
    }
    , [l, s]),
    O.useEffect( () => {
        let $;
        return R > 0 && ($ = setTimeout( () => E(R - 1), 1e3)),
        () => clearTimeout($)
    }
    , [R]);
    const _ = async $ => {
        if ($.preventDefault(),
        m(),
        !x.trim())
            return;
        await d(x.trim()) && E(60)
    }
      , P = async $ => {
        if ($.preventDefault(),
        m(),
        w.length !== 6)
            return;
        await f(w) && s("/shortlist")
    }
    ;
    return a.jsxs("div", {
        className: "max-w-md mx-auto px-4 py-16 space-y-6",
        children: [a.jsxs("div", {
            className: "text-center space-y-2",
            children: [a.jsx("div", {
                className: "w-12 h-12 bg-orange-50 text-orange-600 rounded-2xl flex items-center justify-center mx-auto border border-orange-200",
                children: a.jsx(vd, {
                    className: "w-6 h-6"
                })
            }), a.jsx("h1", {
                className: "text-2xl font-extrabold text-slate-900",
                children: "Sign In with Email OTP"
            }), a.jsx("p", {
                className: "text-xs text-slate-500 max-w-xs mx-auto",
                children: "Passwordless login to save and access your scheme shortlist from any device."
            })]
        }), a.jsxs("div", {
            className: "bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm space-y-6",
            children: [g && a.jsx("div", {
                className: "p-3 bg-rose-50 border border-rose-200 text-rose-800 rounded-xl text-xs font-medium",
                children: g
            }), l === "otp_sent" ? a.jsxs("form", {
                onSubmit: P,
                className: "space-y-4",
                children: [a.jsxs("div", {
                    children: [a.jsxs("label", {
                        className: "block text-xs font-bold text-slate-700 mb-1",
                        children: ["Enter 6-digit Code sent to ", a.jsx("span", {
                            className: "text-slate-900",
                            children: u
                        })]
                    }), a.jsxs("div", {
                        className: "relative",
                        children: [a.jsx(R0, {
                            className: "w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400"
                        }), a.jsx("input", {
                            type: "text",
                            maxLength: 6,
                            inputMode: "numeric",
                            autoComplete: "one-time-code",
                            placeholder: "123456",
                            value: w,
                            onChange: $ => v($.target.value.replace(/\D/g, "")),
                            className: "w-full pl-10 pr-4 py-3 text-xl font-mono tracking-widest text-center bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-orange-500 font-bold",
                            autoFocus: !0
                        })]
                    })]
                }), a.jsxs("button", {
                    type: "submit",
                    disabled: h || w.length !== 6,
                    className: "w-full inline-flex items-center justify-center gap-2 py-3 px-4 bg-orange-600 hover:bg-orange-700 disabled:opacity-50 text-white font-bold text-xs rounded-xl shadow transition-colors",
                    children: [h ? "Verifying..." : "Verify & Log In", a.jsx(mt, {
                        className: "w-4 h-4"
                    })]
                }), a.jsxs("div", {
                    className: "flex items-center justify-between pt-2 text-xs",
                    children: [a.jsx("button", {
                        type: "button",
                        disabled: R > 0 || h,
                        onClick: _,
                        className: "text-orange-600 hover:text-orange-700 disabled:text-slate-400 font-semibold",
                        children: R > 0 ? `Resend code in ${R}s` : "Resend code"
                    }), a.jsx("button", {
                        type: "button",
                        onClick: () => un.setState({
                            status: "guest"
                        }),
                        className: "text-slate-500 hover:text-slate-800",
                        children: "Change email"
                    })]
                })]
            }) : a.jsxs("form", {
                onSubmit: _,
                className: "space-y-4",
                children: [a.jsxs("div", {
                    children: [a.jsx("label", {
                        className: "block text-xs font-bold text-slate-700 mb-1",
                        children: "Your Email Address"
                    }), a.jsxs("div", {
                        className: "relative",
                        children: [a.jsx(vd, {
                            className: "w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400"
                        }), a.jsx("input", {
                            type: "email",
                            required: !0,
                            placeholder: "name@example.com",
                            value: x,
                            onChange: $ => b($.target.value),
                            className: "w-full pl-10 pr-4 py-2.5 text-xs bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-orange-500"
                        })]
                    })]
                }), a.jsxs("button", {
                    type: "submit",
                    disabled: h || !x,
                    className: "w-full inline-flex items-center justify-center gap-2 py-3 px-4 bg-orange-600 hover:bg-orange-700 disabled:opacity-50 text-white font-bold text-xs rounded-xl shadow transition-colors",
                    children: [h ? "Sending Code..." : "Send 6-Digit Code", a.jsx(Cn, {
                        className: "w-4 h-4"
                    })]
                })]
            }), a.jsxs("div", {
                className: "pt-4 border-t border-slate-100 flex items-start gap-2.5 text-slate-500 text-[11px] leading-relaxed",
                children: [a.jsx(Lt, {
                    className: "w-4 h-4 text-emerald-600 shrink-0 mt-0.5"
                }), a.jsx("span", {
                    children: "We only use your email to save your shortlist. Your profile questionnaire answers never leave this device."
                })]
            })]
        })]
    })
}
  , ix = () => {
    const {t: i} = Je()
      , {resetProfile: s} = _t()
      , {deleteMyData: l, status: u} = un()
      , [d,f] = O.useState(null)
      , h = () => {
        s(),
        f("All temporary questionnaire responses have been cleared from memory."),
        setTimeout( () => f(null), 4e3)
    }
      , g = async () => {
        window.confirm("Are you sure you want to delete all saved schemes from your account?") && (await l(),
        f("All saved shortlist data has been permanently deleted."),
        setTimeout( () => f(null), 4e3))
    }
    ;
    return a.jsxs("div", {
        className: "max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8",
        children: [a.jsxs("div", {
            className: "space-y-3",
            children: [a.jsxs("div", {
                className: "inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200 text-xs font-bold shadow-xs",
                children: [a.jsx(Lt, {
                    className: "w-4 h-4 text-emerald-600"
                }), a.jsx("span", {
                    children: "DPDP Act Compliance"
                })]
            }), a.jsx("h1", {
                className: "text-3xl font-extrabold text-slate-900",
                children: i("privacy.heading")
            }), a.jsx("p", {
                className: "text-sm text-slate-600 leading-relaxed max-w-2xl",
                children: i("privacy.lead")
            })]
        }), d && a.jsxs("div", {
            className: "p-4 bg-emerald-50 border border-emerald-200 text-emerald-900 rounded-xl text-xs font-semibold flex items-center gap-2",
            children: [a.jsx(mt, {
                className: "w-4 h-4 text-emerald-600"
            }), a.jsx("span", {
                children: d
            })]
        }), a.jsxs("div", {
            className: "grid grid-cols-1 md:grid-cols-2 gap-4",
            children: [a.jsxs("div", {
                className: "p-5 bg-white rounded-2xl border border-slate-200 shadow-xs space-y-2",
                children: [a.jsx("div", {
                    className: "w-8 h-8 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center",
                    children: a.jsx(Ia, {
                        className: "w-4 h-4"
                    })
                }), a.jsx("h3", {
                    className: "font-bold text-slate-900 text-sm",
                    children: i("privacy.rule1Title")
                }), a.jsx("p", {
                    className: "text-xs text-slate-600 leading-relaxed",
                    children: i("privacy.rule1Desc")
                })]
            }), a.jsxs("div", {
                className: "p-5 bg-white rounded-2xl border border-slate-200 shadow-xs space-y-2",
                children: [a.jsx("div", {
                    className: "w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center",
                    children: a.jsx(Lt, {
                        className: "w-4 h-4"
                    })
                }), a.jsx("h3", {
                    className: "font-bold text-slate-900 text-sm",
                    children: i("privacy.rule2Title")
                }), a.jsx("p", {
                    className: "text-xs text-slate-600 leading-relaxed",
                    children: i("privacy.rule2Desc")
                })]
            }), a.jsxs("div", {
                className: "p-5 bg-white rounded-2xl border border-slate-200 shadow-xs space-y-2",
                children: [a.jsx("div", {
                    className: "w-8 h-8 rounded-lg bg-orange-50 text-orange-600 flex items-center justify-center",
                    children: a.jsx(mt, {
                        className: "w-4 h-4"
                    })
                }), a.jsx("h3", {
                    className: "font-bold text-slate-900 text-sm",
                    children: i("privacy.rule3Title")
                }), a.jsx("p", {
                    className: "text-xs text-slate-600 leading-relaxed",
                    children: i("privacy.rule3Desc")
                })]
            }), a.jsxs("div", {
                className: "p-5 bg-white rounded-2xl border border-slate-200 shadow-xs space-y-2",
                children: [a.jsx("div", {
                    className: "w-8 h-8 rounded-lg bg-purple-50 text-purple-600 flex items-center justify-center",
                    children: a.jsx(za, {
                        className: "w-4 h-4"
                    })
                }), a.jsx("h3", {
                    className: "font-bold text-slate-900 text-sm",
                    children: i("privacy.rule4Title")
                }), a.jsx("p", {
                    className: "text-xs text-slate-600 leading-relaxed",
                    children: i("privacy.rule4Desc")
                })]
            })]
        }), a.jsxs("div", {
            className: "bg-slate-50 p-6 rounded-2xl border border-slate-200 space-y-4",
            children: [a.jsx("h3", {
                className: "font-bold text-sm text-slate-900",
                children: "Exercise Your Data Rights"
            }), a.jsxs("div", {
                className: "flex flex-col sm:flex-row gap-3",
                children: [a.jsxs("button", {
                    onClick: h,
                    className: "inline-flex items-center justify-center gap-2 px-4 py-2.5 bg-white hover:bg-slate-100 text-rose-700 text-xs font-bold rounded-xl border border-rose-200 shadow-xs transition-colors",
                    children: [a.jsx(Fa, {
                        className: "w-4 h-4"
                    }), a.jsx("span", {
                        children: i("privacy.wipeAnswers")
                    })]
                }), u === "authenticated" && a.jsxs("button", {
                    onClick: g,
                    className: "inline-flex items-center justify-center gap-2 px-4 py-2.5 bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold rounded-xl shadow-xs transition-colors",
                    children: [a.jsx(za, {
                        className: "w-4 h-4"
                    }), a.jsx("span", {
                        children: i("privacy.wipeShortlist")
                    })]
                })]
            })]
        }), a.jsxs("div", {
            className: "bg-white p-6 rounded-2xl border border-slate-200 space-y-3 text-xs",
            children: [a.jsxs("h3", {
                className: "font-bold text-sm text-slate-900 flex items-center gap-2",
                children: [a.jsx(A0, {
                    className: "w-4 h-4 text-amber-600"
                }), a.jsx("span", {
                    children: "Technical Transparency"
                })]
            }), a.jsxs("p", {
                className: "text-slate-600 leading-relaxed",
                children: ["Anyone reviewing our open codebase can verify: the database schema contains tables only for ", a.jsx("code", {
                    children: "categories"
                }), ", ", a.jsx("code", {
                    children: "schemes"
                }), ", ", a.jsx("code", {
                    children: "scheme_documents"
                }), ", ", a.jsx("code", {
                    children: "scheme_steps"
                }), ", and ", a.jsx("code", {
                    children: "shortlist (user_id, scheme_id)"
                }), ". No table or column exists in our entire system to store user questionnaire responses."]
            })]
        })]
    })
}
  , ax = () => {
    const {t: i} = Je();
    return a.jsxs("div", {
        className: "max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10",
        children: [a.jsxs("div", {
            className: "space-y-3",
            children: [a.jsxs("div", {
                className: "inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-50 text-orange-800 border border-orange-200 text-xs font-bold shadow-xs",
                children: [a.jsx(Zr, {
                    className: "w-4 h-4 text-orange-600"
                }), a.jsx("span", {
                    children: "Constitutional Architecture"
                })]
            }), a.jsx("h1", {
                className: "text-3xl sm:text-4xl font-black text-slate-900",
                children: "About Yojana Setu"
            }), a.jsx("p", {
                className: "text-sm text-slate-600 leading-relaxed max-w-2xl",
                children: "An open, transparent, and private bridge connecting citizens to constitutional welfare guarantees without bureaucratic barriers."
            })]
        }), a.jsxs("div", {
            className: "space-y-4",
            children: [a.jsx("h2", {
                className: "text-xl font-bold text-slate-900",
                children: "The Four Pillars in Action"
            }), a.jsxs("div", {
                className: "grid grid-cols-1 sm:grid-cols-2 gap-4",
                children: [a.jsxs("div", {
                    className: "p-5 bg-white rounded-2xl border border-slate-200 shadow-xs space-y-2",
                    children: [a.jsx("span", {
                        className: "text-xs font-bold text-blue-700 uppercase tracking-wider block",
                        children: "1. Justice (Social, Economic & Political)"
                    }), a.jsx("h3", {
                        className: "font-bold text-slate-900 text-sm",
                        children: "Securing basic livelihoods & healthcare"
                    }), a.jsx("p", {
                        className: "text-xs text-slate-600 leading-relaxed",
                        children: "Article 38 and 39 direct the state to eliminate inequalities and secure equitable distribution of material resources. Schemes like PM-KISAN and PM-JAY fulfill this mandate."
                    }), a.jsx("div", {
                        className: "text-[11px] font-mono text-slate-500",
                        children: "Key Articles: 38, 39(b), 41, 47, 48"
                    })]
                }), a.jsxs("div", {
                    className: "p-5 bg-white rounded-2xl border border-slate-200 shadow-xs space-y-2",
                    children: [a.jsx("span", {
                        className: "text-xs font-bold text-amber-700 uppercase tracking-wider block",
                        children: "2. Liberty (Thought, Expression & Enterprise)"
                    }), a.jsx("h3", {
                        className: "font-bold text-slate-900 text-sm",
                        children: "Empowering self-reliance and education"
                    }), a.jsx("p", {
                        className: "text-xs text-slate-600 leading-relaxed",
                        children: "Article 19(1)(g) guarantees the right to practice any trade or business, while Article 21A guarantees education. Schemes like PM Vishwakarma and Post-Matric Scholarships enable citizens to pursue their potential freely."
                    }), a.jsx("div", {
                        className: "text-[11px] font-mono text-slate-500",
                        children: "Key Articles: 19(1)(g), 21A, 43, 46"
                    })]
                }), a.jsxs("div", {
                    className: "p-5 bg-white rounded-2xl border border-slate-200 shadow-xs space-y-2",
                    children: [a.jsx("span", {
                        className: "text-xs font-bold text-emerald-700 uppercase tracking-wider block",
                        children: "3. Equality (Status & Opportunity)"
                    }), a.jsx("h3", {
                        className: "font-bold text-slate-900 text-sm",
                        children: "Targeted affirmative welfare"
                    }), a.jsx("p", {
                        className: "text-xs text-slate-600 leading-relaxed",
                        children: "Article 15(3) empowers special provisions for women and children, while 15(4) enables advancement of SC/ST communities. Schemes like Ujjwala, Matru Vandana, and Sukanya Samriddhi bridge historic disparities."
                    }), a.jsx("div", {
                        className: "text-[11px] font-mono text-slate-500",
                        children: "Key Articles: 14, 15(3), 15(4), 39(a), 42"
                    })]
                }), a.jsxs("div", {
                    className: "p-5 bg-white rounded-2xl border border-slate-200 shadow-xs space-y-2",
                    children: [a.jsx("span", {
                        className: "text-xs font-bold text-purple-700 uppercase tracking-wider block",
                        children: "4. Fraternity (Dignity & Social Security)"
                    }), a.jsx("h3", {
                        className: "font-bold text-slate-900 text-sm",
                        children: "Universal dignity in old age & adversity"
                    }), a.jsx("p", {
                        className: "text-xs text-slate-600 leading-relaxed",
                        children: "Article 41 obligates public assistance in cases of unemployment, old age, sickness and disablement. Schemes like Atal Pension Yojana and IGNOAPS Old Age Pension safeguard dignity in old age."
                    }), a.jsx("div", {
                        className: "text-[11px] font-mono text-slate-500",
                        children: "Key Articles: 41, 43, Preamble"
                    })]
                })]
            })]
        }), a.jsxs("div", {
            className: "p-6 bg-slate-50 rounded-2xl border border-slate-200 space-y-3 text-xs leading-relaxed",
            children: [a.jsxs("h2", {
                className: "text-base font-bold text-slate-900 flex items-center gap-2",
                children: [a.jsx(E0, {
                    className: "w-5 h-5 text-orange-600"
                }), a.jsx("span", {
                    children: "Algorithmic Determinism & Zero Hallucination"
                })]
            }), a.jsx("p", {
                className: "text-slate-600",
                children: "Unlike black-box generative AI models that can hallucinate criteria, Yojana Setu uses an open, pure TypeScript evaluation engine. Every rule is evaluated using formal Boolean trees (with inclusive boundary operators and declared tolerances). Given the exact same inputs, the engine will always produce the exact same verdict and relevance score."
            })]
        })]
    })
}
  , ox = () => {
    const {initAuth: i} = un()
      , [s,l] = O.useState({
        lastVerified: "2026-09-15",
        source: "fallback"
    });
    return O.useEffect( () => {
        i(),
        bl().then(u => {
            l({
                lastVerified: u.lastVerified,
                source: u.source
            })
        }
        )
    }
    , [i]),
    a.jsx($m, {
        children: a.jsxs("div", {
            className: "min-h-screen flex flex-col bg-slate-50 text-slate-800",
            children: [a.jsx($0, {}), a.jsx(F0, {}), a.jsx("main", {
                className: "flex-1",
                children: a.jsxs(Rm, {
                    children: [a.jsx(It, {
                        path: "/",
                        element: a.jsx(U0, {})
                    }), a.jsx(It, {
                        path: "/find",
                        element: a.jsx(K0, {})
                    }), a.jsx(It, {
                        path: "/results",
                        element: a.jsx(nx, {})
                    }), a.jsx(It, {
                        path: "/scheme/:slug",
                        element: a.jsx(rx, {})
                    }), a.jsx(It, {
                        path: "/shortlist",
                        element: a.jsx(sx, {})
                    }), a.jsx(It, {
                        path: "/login",
                        element: a.jsx(lx, {})
                    }), a.jsx(It, {
                        path: "/privacy",
                        element: a.jsx(ix, {})
                    }), a.jsx(It, {
                        path: "/about",
                        element: a.jsx(ax, {})
                    })]
                })
            }), a.jsx(I0, {
                lastVerified: s.lastVerified,
                source: s.source
            })]
        })
    })
}
;
Fh.createRoot(document.getElementById("root")).render(a.jsx(tr.StrictMode, {
    children: a.jsx(ox, {})
}));
