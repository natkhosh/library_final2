var app=function(){"use strict";function t(){}function e(t){return t()}function n(){return Object.create(null)}function o(t){t.forEach(e)}function r(t){return"function"==typeof t}function c(t,e){return t!=t?e==e:t!==e||t&&"object"==typeof t||"function"==typeof t}function i(t,e){t.appendChild(e)}function s(t,e,n){t.insertBefore(e,n||null)}function a(t){t.parentNode.removeChild(t)}function u(t){return document.createElement(t)}function l(t){return document.createTextNode(t)}function f(){return l(" ")}function d(t,e,n){null==n?t.removeAttribute(e):t.getAttribute(e)!==n&&t.setAttribute(e,n)}function p(t,e){e=""+e,t.data!==e&&(t.data=e)}let g;function m(t){g=t}function h(t){(function(){if(!g)throw new Error("Function called outside component initialization");return g})().$$.on_mount.push(t)}const y=[],b=[],$=[],v=[],x=Promise.resolve();let w=!1;function k(t){$.push(t)}let _=!1;const C=new Set;function E(){if(!_){_=!0;do{for(let t=0;t<y.length;t+=1){const e=y[t];m(e),S(e.$$)}for(y.length=0;b.length;)b.pop()();for(let t=0;t<$.length;t+=1){const e=$[t];C.has(e)||(C.add(e),e())}$.length=0}while(y.length);for(;v.length;)v.pop()();w=!1,_=!1,C.clear()}}function S(t){if(null!==t.fragment){t.update(),o(t.before_update);const e=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,e),t.after_update.forEach(k)}}const B=new Set;function A(t,e){-1===t.$$.dirty[0]&&(y.push(t),w||(w=!0,x.then(E)),t.$$.dirty.fill(0)),t.$$.dirty[e/31|0]|=1<<e%31}function I(c,i,s,u,l,f,d=[-1]){const p=g;m(c);const h=i.props||{},y=c.$$={fragment:null,ctx:null,props:f,update:t,not_equal:l,bound:n(),on_mount:[],on_destroy:[],before_update:[],after_update:[],context:new Map(p?p.$$.context:[]),callbacks:n(),dirty:d};let b=!1;if(y.ctx=s?s(c,h,(t,e,...n)=>{const o=n.length?n[0]:e;return y.ctx&&l(y.ctx[t],y.ctx[t]=o)&&(y.bound[t]&&y.bound[t](o),b&&A(c,t)),e}):[],y.update(),b=!0,o(y.before_update),y.fragment=!!u&&u(y.ctx),i.target){if(i.hydrate){const t=function(t){return Array.from(t.childNodes)}(i.target);y.fragment&&y.fragment.l(t),t.forEach(a)}else y.fragment&&y.fragment.c();i.intro&&(($=c.$$.fragment)&&$.i&&(B.delete($),$.i(v))),function(t,n,c){const{fragment:i,on_mount:s,on_destroy:a,after_update:u}=t.$$;i&&i.m(n,c),k(()=>{const n=s.map(e).filter(r);a?a.push(...n):o(n),t.$$.on_mount=[]}),u.forEach(k)}(c,i.target,i.anchor),E()}var $,v;m(p)}var N=function(t,e){return t(e={exports:{}},e.exports),e.exports}((function(t,e){var n;n=function(){function t(){for(var t=0,e={};t<arguments.length;t++){var n=arguments[t];for(var o in n)e[o]=n[o]}return e}function e(t){return t.replace(/(%[0-9A-Z]{2})+/g,decodeURIComponent)}return function n(o){function r(){}function c(e,n,c){if("undefined"!=typeof document){"number"==typeof(c=t({path:"/"},r.defaults,c)).expires&&(c.expires=new Date(1*new Date+864e5*c.expires)),c.expires=c.expires?c.expires.toUTCString():"";try{var i=JSON.stringify(n);/^[\{\[]/.test(i)&&(n=i)}catch(t){}n=o.write?o.write(n,e):encodeURIComponent(String(n)).replace(/%(23|24|26|2B|3A|3C|3E|3D|2F|3F|40|5B|5D|5E|60|7B|7D|7C)/g,decodeURIComponent),e=encodeURIComponent(String(e)).replace(/%(23|24|26|2B|5E|60|7C)/g,decodeURIComponent).replace(/[\(\)]/g,escape);var s="";for(var a in c)c[a]&&(s+="; "+a,!0!==c[a]&&(s+="="+c[a].split(";")[0]));return document.cookie=e+"="+n+s}}function i(t,n){if("undefined"!=typeof document){for(var r={},c=document.cookie?document.cookie.split("; "):[],i=0;i<c.length;i++){var s=c[i].split("="),a=s.slice(1).join("=");n||'"'!==a.charAt(0)||(a=a.slice(1,-1));try{var u=e(s[0]);if(a=(o.read||o)(a,u)||e(a),n)try{a=JSON.parse(a)}catch(t){}if(r[u]=a,t===u)break}catch(t){}}return t?r[t]:r}}return r.set=c,r.get=function(t){return i(t,!1)},r.getJSON=function(t){return i(t,!0)},r.remove=function(e,n){c(e,"",t(n,{expires:-1}))},r.defaults={},r.withConverter=n,r}((function(){}))},t.exports=n()}));function R(t,e,n){const o=t.slice();return o[4]=e[n],o}function O(t){let e,n,o,r,c,g,m,h,y,b,$,v,x,w,k,_,C,E,S=t[4].author+"",B=t[4].name+"",A=t[4].discount+"";return{c(){e=u("div"),n=u("div"),o=u("a"),r=u("img"),g=f(),m=u("h6"),h=l(S),y=f(),b=u("h6"),$=l(B),v=f(),x=u("h6"),w=u("span"),k=l(A),_=l(" / "),C=u("a"),C.textContent="Buy Now",E=f(),r.src!==(c="../static/"+t[4].image)&&d(r,"src",c),d(r,"alt","img"),d(o,"href","."),d(w,"class","price"),d(C,"href","."),d(n,"class","item"),d(e,"class","col-md-3")},m(t,c){s(t,e,c),i(e,n),i(n,o),i(o,r),i(o,g),i(o,m),i(m,h),i(o,y),i(o,b),i(b,$),i(n,v),i(n,x),i(x,w),i(w,k),i(x,_),i(x,C),i(e,E)},p(t,e){1&e&&r.src!==(c="../static/"+t[4].image)&&d(r,"src",c),1&e&&S!==(S=t[4].author+"")&&p(h,S),1&e&&B!==(B=t[4].name+"")&&p($,B),1&e&&A!==(A=t[4].discount+"")&&p(k,A)},d(t){t&&a(e)}}}function U(e){let n,o,r,c,l,p,g,m,h,y=e[0],b=[];for(let t=0;t<y.length;t+=1)b[t]=O(R(e,y,t));return{c(){n=u("main"),o=u("section"),r=u("div"),c=u("h2"),c.textContent="recently added books to our store",l=f(),p=u("div"),g=u("div");for(let t=0;t<b.length;t+=1)b[t].c();m=f(),h=u("div"),h.innerHTML='<button class="btn gray-btn">load More books</button>',d(g,"class","row"),d(h,"class","btn-sec"),d(p,"class","recent-book-sec"),d(r,"class","container"),d(o,"class","static about-sec"),d(n,"class","svelte-og6v3r")},m(t,e){s(t,n,e),i(n,o),i(o,r),i(r,c),i(r,l),i(r,p),i(p,g);for(let t=0;t<b.length;t+=1)b[t].m(g,null);i(p,m),i(p,h)},p(t,[e]){if(1&e){let n;for(y=t[0],n=0;n<y.length;n+=1){const o=R(t,y,n);b[n]?b[n].p(o,e):(b[n]=O(o),b[n].c(),b[n].m(g,null))}for(;n<b.length;n+=1)b[n].d(1);b.length=y.length}},i:t,o:t,d(t){t&&a(n),function(t,e){for(let n=0;n<t.length;n+=1)t[n]&&t[n].d(e)}(b,t)}}}function j(t,e,n){let o=[];N.get("csrftoken");const r=(c="shop-ref",document.getElementById(c).href);var c;h(async()=>{const t=await fetch(r,{headers:{Accept:"application/json, text-plain, */*","X-Requested-With":"XMLHttpRequest"}});let e=await t.json();n(0,o=e.books),n(0,o),console.log(o)});let i=new WebSocket("ws://localhost:8000");return i.onopen=function(t){console.log("[open] Соединение установлено"),console.log("C"),i.send("books?")},i.onmessage=function(t){console.log("[message] Данные получены с сервера: "+t.data);let e=JSON.parse(t.data).value;document.getElementById("book-count").innerText=e},[o]}return new class extends class{$destroy(){!function(t,e){const n=t.$$;null!==n.fragment&&(o(n.on_destroy),n.fragment&&n.fragment.d(e),n.on_destroy=n.fragment=null,n.ctx=[])}(this,1),this.$destroy=t}$on(t,e){const n=this.$$.callbacks[t]||(this.$$.callbacks[t]=[]);return n.push(e),()=>{const t=n.indexOf(e);-1!==t&&n.splice(t,1)}}$set(){}}{constructor(t){super(),I(this,t,j,U,c,{})}}({target:document.getElementById("books_list")})}();
//# sourceMappingURL=bundle.js.map
