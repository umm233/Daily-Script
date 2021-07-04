// ==UserScript==
// @name         豆瓣电影直达 RARBG
// @namespace    http://umm.js.org/
// @version      0.1
// @description  豆瓣电影直达 RARBG
// @author       umm
// @match        https://movie.douban.com/*
// @grant        none
// ==/UserScript==

(function () {
    'use strict';
    let title = document.getElementsByTagName('h1')[0].children[0].innerText;
    let info = document.getElementById('info');
    let btlink = document.createElement('a');
    let imdb_id = info.innerText.match(/tt\d+/)[0];
    btlink.href=`https://rarbgprx.org/torrents.php?search=${imdb_id}&order=seeders&by=DESC`;
    btlink.target = '_blank';
    btlink.innerText = 'Go To RARBG';
    info.appendChild(btlink);
})();
