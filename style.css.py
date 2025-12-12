/* 全体設定 */
html {
    scroll-behavior: smooth; /* スクロールを滑らかに */
}

body {
    margin: 0;
    padding-top: 70px; /* 固定ナビゲーション分の余白 */
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "YuGothic", "游ゴシック体", sans-serif;
    background: #0a0a0a;
    color: #f5f5f5;
    line-height: 1.8;
}

/* ナビゲーション */
nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: rgba(0, 0, 0, 0.9);
    padding: 10px 0;
    z-index: 1000;
    border-bottom: 1px solid #333;
    backdrop-filter: blur(6px);
}

nav ul {
    margin: 0;
    padding: 0;
    list-style: none;
    display: flex;
    justify-content: center;
    gap: 28px;
}

nav a {
    color: #f5f5f5;
    text-decoration: none;
    font-size: 14px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

nav a:hover {
    color: #00ffff;
}

/* セクション共通 */
section.block {
    max-width: 760px;
    margin: 0 auto;
    padding: 70px 20px;
    border-bottom: 1px solid #222;
}

#mission {
    max-width: 760px;
    margin: 0 auto;
    padding: 90px 20px 60px;
    text-align: center;
}

/* 見出し */
h1 {
    font-size: 28px;
    margin: 0 0 10px;
}

h1 .sub {
    font-size: 14px;
    font-weight: 400;
    color: #aaa;
}

h2 {
    font-size: 20px;
    margin-bottom: 16px;
}

/* 本文 */
p {
    font-size: 15px;
    margin: 0;
}

/* スマホ用ちょい調整 */
@media (max-width: 600px) {
    nav ul {
        gap: 16px;
        font-size: 12px;
    }

    section.block,
    #mission {
        padding: 60px 16px;
    }

    h1 {
        font-size: 22px;
    }

    h2 {
        font-size: 18px;
    }

    p {
        font-size: 14px;
    }
}