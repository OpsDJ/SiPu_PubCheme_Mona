
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<title>中药对照品供应商/化合物库/标准品｜高分辨质谱+分离定制｜药品质量提升解决方案「成都普思生物」</title>
<meta name="keywords" content="中药对照品供应商,化合物库,高分辨质谱分析,分离提取,天然化合物,药品质量提升">
<meta name="description" content="成都普思生物（2005年成立）——国家高新技术企业，中检所标准物质供应商，专注天然药物分离纯化与药物研发服务。提供超5000种天然产物单体、千余种中药对照品（覆盖中国药典及地方标准），支持高分辨质谱检测与分离定制服务，助力中药制剂、化药杂质分离及药品质量提升。严格遵循GMP标准，确保产品溯源性、准确性，为医药行业提供一站式解决方案。">
<LINK href="favicon.ico" type="image/x-icon" rel="shortcut icon">
<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" /><link href="css/swiper-bundle.min.css" rel="stylesheet" /><link href="css/main.css" rel="stylesheet" /><link rel="stylesheet" type="text/css" href="css/style.css" />
<script type="text/javascript" src="js/jquery.min.js"></script>
<script src="js/swiper-bundle.min.js"></script>
<style type="text/css">
        /*youshi*/
        .pushDiv {
            overflow: hidden;
            width: 100%;
        }

            .pushDiv .ttitle {
                overflow: hidden;
                padding: 55px 0;
                /*background-color: #11a3a3;*/
            }

                .pushDiv .ttitle h2 {
                    text-align: center;
                }

                .pushDiv .ttitle em {
                    display: block;
                    text-align: center;
                    font-size: 16px;
                    color: #fff;
                    margin-top: 10px;
                }

            .pushDiv .yslist {
                overflow: hidden;
                width: 100%;
                height: 291px;
            }

                .pushDiv .yslist .wen {
                    overflow: hidden;
                    width: 407px;
                    color: #333;
                }

                .pushDiv .yslist h3 {
                    font-size: 20px;
                    margin-bottom: 20px;
                    line-height: 30px;
                }

                .pushDiv .yslist p {
                    padding-left: 14px;
                    background: url(/img/wenda/youshi_s02.png) no-repeat left 8px;
                    font-size: 13px;
                    line-height: 25px;
                }

        .youshi .yslist .wen.wen01 p {
            background: url(/img/wenda/youshi_s01.png) no-repeat left 8px;
        }

        .pushDiv .phone {
            overflow: hidden;
            padding-left: 55px;
            background: url(/img/wenda/phone.png) no-repeat left center;
            margin-top: 20px;
        }

            .pushDiv .phone span {
                display: block;
                font-size: 13px;
                color: #333;
            }

            .pushDiv .phone em {
                display: block;
                font-size: 22px;
                color: #ff6600;
            }

        .pushDiv .youshi01 {
            background: url(/img/wenda/youshi_01.jpg) no-repeat center top;
        }

        .pushDiv .youshi02 {
            background: url(/img/wenda/youshi_02.jpg) no-repeat center top;
        }

        .pushDiv .youshi03 {
            background: url(/img/wenda/youshi_03.jpg) no-repeat center top;
        }

        .pushDiv .youshi04 {
            background: url(/img/wenda/youshi_04.jpg) no-repeat center top;
        }

        .youshi .youshi05 {
            background: url(/img/wenda/youshi_05.jpg) no-repeat center top;
        }

        .pushDiv .wen.wen01 {
            color: #fff;
            margin-left: 168px;
            margin-top: 10px;
        }

        .pushDiv .wen02 {
            float: right;
            margin-top: 35px;
        }

        .pushDiv .wen03 {
            margin-left: 168px;
            margin-top: 35px;
        }

        .pushDiv .wen04 {
            float: right;
            margin-top: 55px;
        }

        .pushDiv .wen05 {
            margin-left: 168px;
            margin-top: 40px;
            width: 425px !important;
        }

        .pushDiv .container {
            padding: 0px;
        }

        .carouselDiv p {
            font-size: 16px;
            /*font-weight:600;*/
            line-height: 26px;
            margin-bottom: 10px;
        }

        #div_jsfw p {
            height: 38px;
        }

        @keyframes moveUp {
            0% {
                transform: translateY(0);
                opacity: 0;
            }

            100% {
                transform: translateY(-100px);
                opacity: 1;
            }
        }

        .animate-up {
            animation: moveUp 0.6s ease-out forwards; /* 动画名称, 持续时间, 缓动函数, 动画执行完毕后是否保持最后一帧 */
        }

        #video-container {
            position: relative;
            /*width: 640px;*/
        }

        #video {
            width: 100%;
        }

        #play-button {
            /*position: absolute;*/
            /*top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);*/
            margin: 20px 20px;
            width: 60px;
            height: 60px;
            background-color: rgba(25, 206, 103, 0.5);
            border: none;
            border-radius: 50%;
            cursor: pointer;
            /*display: none;*/
            /*align-items: center;
            justify-content: center;*/
        }

        .triangle {
            width: 0;
            height: 0;
            border-top: 14px solid transparent;
            border-bottom: 14px solid transparent;
            border-left: 20px solid #fff;
            position: absolute;
            top: 50%; /* 调整位置 */
            left: 50%; /* 调整位置 */
            transform: translate(-50%, -50%); /* 居中 */
            margin-left: 3px;
        }
        /************以下为具体实现************/

        .wave {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100px;
            height: 100px;
            cursor: pointer;
            /*background-color: #19ce67;*/
            /*border: none;*/
            /*border-radius: 50%;*/
            /*cursor: pointer;*/
            /*display: none;*/
            /*align-items: center;*/
            /*justify-content: center;*/
            /*width: 100px;
            height: 100px;
            text-align: center;*/
            /*line-height: 100px;
            font-size: 28px;*/
        }

            .wave .circle {
                position: absolute;
                border-radius: 50%;
                opacity: 0;
            }

            /* 波纹效果 */
            .wave.ripple .circle {
                width: calc(100% - 6px); /* 减去边框的大小 */
                height: calc(100% - 6px); /* 减去边框的大小 */
                border: 3px solid #fff;
            }

                .wave.ripple .circle:first-child {
                    animation: circle-opacity 1s infinite;
                }

                .wave.ripple .circle:nth-child(2) {
                    animation: circle-opacity 1s infinite;
                    animation-delay: .3s;
                }

                .wave.ripple .circle:nth-child(3) {
                    animation: circle-opacity 1s infinite;
                    animation-delay: .6s;
                }

            .wave.ripple.danger {
                color: red;
            }

                .wave.ripple.danger .circle {
                    border-color: red;
                }

            .wave.ripple.warning {
                color: orange;
            }

                .wave.ripple.warning .circle {
                    border-color: orange;
                }

            /* 波动效果 */
            .wave.solid .circle {
                width: 100%;
                height: 100%;
                background: #fff;
            }

                .wave.solid .circle:first-child {
                    animation: circle-opacity 2s infinite;
                }

            .wave.solid.danger {
                color: red;
            }

                .wave.solid.danger .circle {
                    background: red;
                }

            .wave.solid.warning {
                color: orange;
            }

                .wave.solid.warning .circle {
                    background: #19ce67;
                }

        @keyframes circle-opacity {
            from {
                opacity: 1;
                transform: scale(0);
            }

            to {
                opacity: 0;
                transform: scale(1);
            }
        }

        #swiper-zl {
            text-align: center;
        }

            #swiper-zl div img {
                width: 230px;
            }
    </style>
<title>
</title></head>
<body>
<link href="../layui/css/layui.css" rel="stylesheet" />
<style type="text/css">
    html {
        overflow: auto;
    }

    .image-cnascontainer {
        position: relative;
        display: inline-block;
    }

    .base-image {
        height: 30px;
    }

    .base-image, .hover-image {
        position: absolute;
        /*left: 0;*/
        top: 28px;
        transition: opacity 0.5s ease; /* 平滑过渡效果 */
    }

    .hover-image {
        margin-top: 50px;
        z-index: 500;
        display: none;
        border: solid 1px #49946f;
        height: 500px;
    }

    .image-cnascontainer:hover .hover-image {
        z-index: 500;
        display: block;
    }
    #childDiv li {
        line-height:30px;
    }
    #childDiv a {
        font:14px/1.8 "microsoft yahei",Arial, Helvetica, sans-serif;
    }
</style>
<div class="inner top clearfix" style="height: 90px; padding: 0px;">
<div class="logo">
<a href="index.aspx">
<img src="images/logo.png" alt="普思生物logo" class="png vt"></a>
<a href="javascript:" class="image-cnascontainer">
<img src="../images/cnas.png" class="base-image" />
<img id="img_cnas" src="../images/cnaszs.png" alt="cnas证书" class="hover-image" />
</a>
<a href="javascript:" class="image-cnascontainer" style="margin-left: 50px;">
<img src="../images/hj.png" class="base-image" />
<img src="../images/hjzs.jpg" alt="高新技术企业证书" class="hover-image" />
</a>
</div>
<div class="clearfix">
<div class="nav" style="padding: 0px; width: 650px;" id="nav1">
<div style="padding: 27px 0px 5px 0px; float: right;width: 100%;">
<form name="cscsearch" action="ps_Search.aspx" method="get" id="cscsearch">
<select id="selquery" name="selquery" style="border: none; margin-left: 1px; margin-top: 1px; height: 41px; border-radius: 5px 0px 0px 5px; position: absolute; float: left; border-right: none; line-height: 28px; padding: 0px 15px; width: 135px; font-size: 16px;">
<option value="0">全部查询</option>
<option value="1">化合物库</option>
<option value="2">对照品库</option>
<option value="3">来源库</option>
<option value="5">新闻资讯</option>
</select>
<input name="txtquery" id="txtquery" type="text" style="border-radius: 5px; width: 493px; height: 41px; border: solid 1px #0d673a; padding: 0px 15px 0px 140px; line-height: 28px;font-size:16px;" value="" autocomplete="off">
<div style="display:block;position:absolute;top:37px;right:3px;font-size:inherit;">
<a href="#" style="background-color: #0d673a; padding: 9px 12px; margin-top: 2px; color: white; font-size: 16px; border-radius: 5px;" onclick="document.getElementById('cscsearch').submit();return false">搜索</a>
<a href="javascript:" style="background-color: #0d673a; padding: 9px 12px; color: white; font-size: 16px; border-radius: 5px;" id="a_BatchSearch">批量搜索</a>
</div>
</form>
</div>
</div>
</div>
</div>
<div style="background-color:#0d673a; height: 50px; width: 100%;">
<div class="inner clearfix">
<div class="nav" style="padding: 0px; float: left;height:50px;width:100%;" id="nav">
<ul style="">
<li onmouseover='changeBg(1)' onmouseout='changeBg1(1)' class="act" style="height:50px;line-height:50px;">
<a id="ut_r_nav_list_hlMenu_0" href="/index.aspx"><a href="/index.aspx"style="font-size:18px;font-weight:600;">首页</a></a><br />
<div id='menuChildDiv_1' style="display: none; position: absolute; z-index: 999;margin-left:-30px;">
<ul id="childDiv" style="border: #11a3a3 solid 1px;">
</ul>
</div>
</li>
<li onmouseover='changeBg(2)' onmouseout='changeBg1(2)' style="height:50px;line-height:50px;">
<a id="ut_r_nav_list_hlMenu_1" href="td_counter/news.aspx?id=198"><a href="news.aspx?id=198"style="font-size:18px;font-weight:600;">关于普思</a></a><br />
<div id='menuChildDiv_2' style="display: none; position: absolute; z-index: 999;margin-left:-30px;">
<ul id="childDiv" style="border: #11a3a3 solid 1px;">
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_1_hlMenuChild_0" href="about.aspx?id=12">简要介绍</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_1_hlMenuChild_1" href="coursers.aspx?id=13">发展历程</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_1_hlMenuChild_2" href="about.aspx?id=324">研发机构</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_1_hlMenuChild_3" href="honor.aspx?id=16">资质荣誉</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_1_hlMenuChild_4" href="news.aspx?id=198">新闻资讯</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_1_hlMenuChild_5" href="about.aspx?id=15">服务平台</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_1_hlMenuChild_6" href="join.aspx?id=33">人力资源</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_1_hlMenuChild_7" href="contact.aspx?id=208">联系我们</a>
</li>
</ul>
</div>
</li>
<li onmouseover='changeBg(221)' onmouseout='changeBg1(221)' style="height:50px;line-height:50px;">
<a id="ut_r_nav_list_hlMenu_2" href="sitemap.aspx?id=222"><a href="../sitemap.aspx?id=222"style="font-size:18px;font-weight:600;">产品</a></a><br />
<div id='menuChildDiv_221' style="display: none; position: absolute; z-index: 999;margin-left:-30px;">
<ul id="childDiv" style="border: #11a3a3 solid 1px;">
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_2_hlMenuChild_0" href="ps_Product.aspx?id=222">中药化学对照品</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_2_hlMenuChild_1" href="ps_Product.aspx?id=223">高纯化学试剂</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_2_hlMenuChild_2" href="ps_danti.aspx?id=226">化合物库</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_2_hlMenuChild_3" href="ps_Product.aspx?id=227">对照药材</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_2_hlMenuChild_4" href="ps_Product.aspx?id=228">提取物/组分库</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_2_hlMenuChild_5" href="ps_Product.aspx?id=229">标准物质</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_2_hlMenuChild_6" href="ps_Product.aspx?id=230">生化试剂</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_2_hlMenuChild_7" href="ps_Product.aspx?id=231">菌株（菌种）</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_2_hlMenuChild_8" href="ps_Product.aspx?id=232">色谱柱/耗材</a>
</li>
</ul>
</div>
</li>
<li onmouseover='changeBg(4)' onmouseout='changeBg1(4)' style="height:50px;line-height:50px;">
<a id="ut_r_nav_list_hlMenu_3" href="ps_Product.aspx?id=271"><a href="../ps_Product.aspx?id=271"style="font-size:18px;font-weight:600;">技术服务</a></a><br />
<div id='menuChildDiv_4' style="display: none; position: absolute; z-index: 999;margin-left:-30px;">
<ul id="childDiv" style="border: #11a3a3 solid 1px;">
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_3_hlMenuChild_0" href="ps_Product.aspx?id=271">合同定制/研发生产服务——CMO/CDMO</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_3_hlMenuChild_1" href="ps_Product.aspx?id=280">医药研发合同外包服务——CRO</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_3_hlMenuChild_2" href="ps_Product.aspx?id=289">检验检测</a>
</li>
</ul>
</div>
</li>
<li onmouseover='changeBg(301)' onmouseout='changeBg1(301)' style="height:50px;line-height:50px;">
<a id="ut_r_nav_list_hlMenu_4" href="td_counter/ps_Product.aspx?id=305"><a href="ps_Product.aspx?id=305"style="font-size:18px;font-weight:600;">支持</a></a><br />
<div id='menuChildDiv_301' style="display: none; position: absolute; z-index: 999;margin-left:-30px;">
<ul id="childDiv" style="border: #11a3a3 solid 1px;">
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_4_hlMenuChild_0" href="ps_Product.aspx?id=305">品牌、等级</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_4_hlMenuChild_1" href="ps_Product.aspx?id=307">产品信息查询</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_4_hlMenuChild_2" href="ps_Product.aspx?id=308">纯度、含量</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_4_hlMenuChild_3" href="ps_Product.aspx?id=309">赋值产品</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_4_hlMenuChild_4" href="ps_Product.aspx?id=310">使用注意事项</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_4_hlMenuChild_5" href="ps_Product.aspx?id=311">包装与运输</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_4_hlMenuChild_6" href="ps_StandardLibrary.aspx?id=312">标准收录</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_4_hlMenuChild_7" href="ps_Product.aspx?id=313">售后</a>
</li>
</ul>
</div>
</li>
<li onmouseover='changeBg(302)' onmouseout='changeBg1(302)' style="height:50px;line-height:50px;">
<a id="ut_r_nav_list_hlMenu_5" href="ps_BulkGood.aspx?id=302"><a href="../ps_BulkGood.aspx?id=302"style="font-size:18px;font-weight:600;">热销原料</a></a><br />
<div id='menuChildDiv_302' style="display: none; position: absolute; z-index: 999;margin-left:-30px;">
<ul id="childDiv" style="border: #11a3a3 solid 1px;">
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_5_hlMenuChild_0" href="ps_BulkGood.aspx?id=315">木犀草苷</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_5_hlMenuChild_1" href="ps_BulkGood.aspx?id=316">人参皂苷Ro</a>
</li>
<li style="clear: both; width: 150px; min-width: 70px;margin-left:-30px; background-color: #fff; padding: 5px 15px; margin: 0px; border-bottom: #f5f5f5 solid 1px; border-left: #f5f5f5 solid 1px; border-right: #f5f5f5 solid 1px;">
<a id="ut_r_nav_list_rptMenuChild_5_hlMenuChild_2" href="ps_BulkGood.aspx?id=317">荭草苷</a>
</li>
</ul>
</div>
</li>
</ul>
</div>
</div>
</div>
<script src="../layui/layui.js"></script>
<script type="text/javascript">
    (function ($) {
        function toseach() {
            var keys = $('#txt_key').val();
            if (keys == '') {
                alert('请输入关键词！');
                $('#txt_key').focus();
                return false;
            }
            window.location = 'search.aspx?key=' + keys;
        }
        $('input').keyup(function (event) {
            if (event.keyCode == "13") {
                toseach();
                return false;
            }
        });
    });
    function changeBg(rep) {
        //$("#menuChildDiv_" + rep).show();
        if (rep != 1) {
            document.getElementById("menuChildDiv_" + rep).style.display = "inline";
        }

    }
    function changeBg1(rep) {
        //$("#menuChildDiv_" + rep).hide();
        document.getElementById("menuChildDiv_" + rep).style.display = "none";
    }
</script>
<script>
    $("#a_BatchSearch").click(function () {
        layui.use(['jquery', 'form'], function () {
            var index = layer.open({
                type: 1,
                title: '批量CAS号查询(一行一个)',
                skin: 'layui-layer-lan',
                //shadeClose: true, //点击遮罩关闭层
                area: ['310px', '380px'],
                content: '<div style="padding-top:15px;padding-left:15px;"><textarea rows="15" cols="200" id="txtSearchStr" style="width:275px;resize:none"></textarea></div> ',//弹框显示的
                btn: ['确认', '取消'], //只是为了演示
                yes: function (index, layero) {
                    var str = $("#txtSearchStr").val().trim();
                    if (str != null) {
                        //var strlist = str.split(/[(\r\n)\r\n]+/);
                        var reg = new RegExp(/[(\r\n)\r\n]+/, "g");
                        var strlist = str.replace(reg, ',');
                        location.href = "../BatchQuery.aspx?txtquery=" + strlist;
                    }
                },
                cancel: function () {

                }
            });
        });
    });
</script>
<div class="banner">
<div class="bannerbox">
<ul>
<li><a href="sitemap.aspx?id=222" style="background-image: url(Uploadfiles/Picture/2025-9-5/202509051119223968.jpg); background-size: contain;" class="pic" target="_blank">&nbsp;</a></li>
<li><a href="/ps_BulkGood.aspx?id=315" style="background-image: url(Uploadfiles/Picture/2025-9-4/202509041620023840.png); background-size: contain;" class="pic" target="_blank">&nbsp;</a></li>
<li><a href="/ps_Product.aspx?id=272" style="background-image: url(Uploadfiles/Picture/2025-9-4/202509041616032990.png); background-size: contain;" class="pic" target="_blank">&nbsp;</a></li>
<li><a href="/ps_Product.aspx?id=289" style="background-image: url(Uploadfiles/Picture/2025-9-4/202509041615296610.png); background-size: contain;" class="pic" target="_blank">&nbsp;</a></li>
<li><a href="/ps_Product.aspx?id=280" style="background-image: url(Uploadfiles/Picture/2025-9-5/202509051130590068.jpg); background-size: contain;" class="pic" target="_blank">&nbsp;</a></li>
</ul>
</div>
<div class="bannerbot"><img class="png" src="img/banner_i1.png"></div>
</div>
<div class="pushDiv" style="">
<dl class="iboxlist clearfix">
<dd style="height: 450px; position: relative;">
<div class="aboutibox animate-up">
<a href="ps_danti.aspx">
<img src="/img/6.png" alt="药物技术服务" class="vt1" /></a>
<div style="padding: 10px;">
<div style="height: 34px; font-size: 18px; text-align: right;">
<a href="sitemap.aspx?id=222"><span>[探索产品矩阵 →]</span></a>
</div>
<div style="font-size: 32px; color: #0d673a; font-weight: 600; height: 45px; animation-delay: 0s;">
5,000+ 
</div>
<div style="height: 34px; font-size: 18px;">
中药化学对照品 & 高纯试剂
</div>
<div style="height: 45px; color: #0d673a; font-size: 26px;">
一站式采购
</div>
<div style="height: 34px; font-size: 18px;">
定制化服务
</div>
<div style="height: 45px; color: #0d673a; font-size: 26px;">
毫克级→公斤级
</div>
</div>
</div>
</dd>
<dd style="height: 400px; display: grid; justify-content: center; position: relative;">
<div class="aboutibox animate-up" style="margin: 0 auto; left: 0px; right: 0px; top: 0px; margin-top: 100px; animation-delay: 0.5s;">
<a href="ps_danti.aspx">
<img src="/img/4.png" alt="检验检测服务" class="vt1" /></a>
<div style="padding: 10px;">
<div style="height: 34px; font-size: 18px; text-align: right;">
<a href="ps_danti.aspx"><span>[访问化合物库 →]</span></a>
</div>
<div style="font-size: 32px; color: #0d673a; font-weight: 600; height: 45px;">
500+ 
</div>
<div style="height: 34px; font-size: 18px;">
药用植物来源库
</div>
<div style="height: 45px; color: #0d673a; font-size: 26px;">
12大类
</div>
<div style="height: 34px; font-size: 18px;">
天然产物结构
</div>
<div style="height: 45px; color: #0d673a; font-size: 26px;">
固体+液体 化合物库
</div>
</div>
</div>
</dd>
<dd style="height: 400px; position: relative;">
<div class="aboutibox animate-up" style="right: 0px; animation-delay: 1s;">
<a href="ps_BulkGood.aspx?id=315" target="_blank">
<img src="/img/5.png" alt="天然化合物库" class="vt1" /></a>
<div style="padding: 10px;">
<div style="height: 34px; font-size: 18px; text-align: right;">
<a href="ps_BulkGood.aspx?id=315"><span>[重点产品详情 →]</span></a>
</div>
<div style="font-size: 32px; color: #0d673a; font-weight: 600; height: 45px;">
300+
</div>
<div style="height: 34px; font-size: 18px;">
合作企业
</div>
<div style="height: 45px; color: #0d673a; font-size: 26px;">
20年
</div>
<div style="height: 34px; font-size: 18px;">
行业经验
</div>
<div style="height: 45px; color: #0d673a; font-size: 26px;">
克级→公斤级
</div>
</div>
</div>
</dd>
</dl>
</div>
<div class="pushDiv" style="background: url(../images/df1.png) no-repeat  right top; background-size: cover; padding: 30px 0px;">
<dl class="iboxlist clearfix" style="display: flex; border-radius: 10px; overflow: hidden; border: solid 1px #e9e8e8; background-color: white; padding: 30px 0px;">
<dd style="align-content: center; text-align: center;">
<div id="video-container">
<video id="video" src="images/gs-2024.mp4?v=1" controls="controls" style="width: 490px; height: 300px;"></video>
<div id="divwarning" class="wave solid warning">
<div class="circle"></div>
<div id="play-button" class="content">
<div class="triangle"></div>
</div>
</div>
</div>
</dd>
<dd style="align-content: center; text-align: center;">
<div id="div_jsfw" style="text-align: left;">
<div style="color: cadetblue; font-weight: 600; font-size: 20px;">
<p>药物单体纯化、定制生产服务</p>
<p>检验检测、高分辨质谱分析</p>
<p>中药新药、经典名方研发合同外包服务</p>
</div>
<div style="font-size: 20px;">
<p>CNAS认证实验室</p>
<p>四川省天然药物分离纯化工程技术研究中心</p>
<p>四川省药物单体高效分离纯化平台</p>
<p>成都市中药创新药物中试研发服务平台</p>
</div>
<a href="ps_Product.aspx?id=272"><span>[技术服务详细 →]</span></a>
</div>
</dd>
</dl>
</div>
<div class="pushDiv" style="padding: 30px 0px;">
<div class="iboxlist clearfix" style="display: flex; border-radius: 10px; overflow: hidden; border: solid 1px #e9e8e8; padding: 0px; background-color: #faf9f9;">
<div style="text-align: center; width: 100%; margin: 20px;">
<h2 style="font-size: 26px; font-weight: 600;">为什么选择普思生物？
</h2>
</div>
<div class="layui-tab layui-tab-brief" id="tab-zyxx" style="width: 100%;" lay-filter="tab-pushtab">
<ul class="layui-tab-title" style="float: right; width: 100%;">
<li><strong style="font-size: 18px;">重点项目</strong></li>
<li><strong style="font-size: 18px;">先进设备</strong></li>
<li class="layui-this"><strong style="font-size: 18px;">荣誉资质</strong> </li>
</ul>
<div class="layui-tab-content">
<div class="layui-tab-item" style="padding: 40px 20px 10px 20px;">
<dl style="display: flex; width: 100%;">
<dd style="height: 400px;">
<div class="layui-carousel" id="ID-carousel-2" style="margin-top: 10px;">
<div carousel-item>
<div>
<img src="images/zd1.png" />
</div>
<div style="background-color: white; text-align: center; line-height: 400px;">
<img src="images/zd2.png" style="height: 100%" />
</div>
<div style="background-color: white; text-align: center; line-height: 400px;">
<img src="images/zd3.png" style="width: 100%; height: 100%;" />
</div>
</div>
</div>
</dd>
<dd style="height: 400px; text-align: center;">
<div style="text-align: left; padding-left: 20px; margin-top: 30px;" class="carouselDiv">
<p>凭借先进的检测平台、资深的技术团队和严格的质量管理体系，普思生物已成功参与多项国家级、省级重大药物技术研究项目。</p>
<p><strong>2012年</strong> 普思参与了国际合作项目“香港中药材标准研究项目”，公司是唯一一家参与了该项目的民营企业，主要承担相关品种指纹图谱建立、活性成分或指标成分对照品的提取制备工作；</p>
<p><strong>2017年</strong> 普思的科技项目“高附加值中药成分分离纯化技术研究及产业化”荣获武侯区2015-2016年度科技进步特等奖；</p>
<p><strong>2019年</strong> 普思作为主要完成单位之一申报的“基于构效关系的中药活性物质发现及其开发应用”项目，荣获四川省科学技术厅科技进步一等奖。</p>
</div>
</dd>
</dl>
</div>
<div class="layui-tab-item" style="padding: 40px 20px 10px 20px;">
<dl style="display: flex; width: 100%;">
<dd style="height: 400px;">
<div class="layui-carousel" id="ID-carousel-1" style="margin-top: 10px;">
<div carousel-item>
<div>
<img src="images/sb1.png" />
</div>
<div>
<img src="images/sb2.png" />
</div>
</div>
</div>
</dd>
<dd style="height: 400px; text-align: center;">
<div style="text-align: left; padding-left: 20px; margin-top: 30px;" class="carouselDiv">
<p>我们配备多台<strong>一线品牌仪器设备，确保试验结果稳定可靠 </strong></p>
<p><strong>二维液相串联高分辨质谱系统（2D-UHPLC-QTOF） </strong>支持化合物鉴定、成分分析、中药标准、杂质等研究</p>
<p><strong>全自动半制备液相 </strong>具有良好的分离性能，可实现复杂样品中目标组分的有效分离且能满足毫克至克级样品的制备需求。</p>
<p><strong>中试生产级制备液相 </strong>覆盖从毫克级到百克级的分离需求；实验室级探索，单次处理量1-10g原料，快速验证工艺；中试级生产，单次处理量50-100g原料，百克级成分最快7天内交付；</p>
<p><strong>微量粉末自动分装仪 </strong>全球首台集安剖瓶粉末灌装、称量、融封于一体的设备，性能稳定、计量精确、运行安全可靠。</p>
<p>此外，我们还配备液相色谱仪、气相色谱仪和多功能提取罐等中试级生产设备，实现了“分析检测—工艺验证—中试支持”的一体化服务能力。</p>
</div>
</dd>
</dl>
</div>
<div class="layui-tab-item layui-show" style="padding: 40px 20px 10px 20px;">
<dl style="display: flex; width: 100%;">
<dd style="height: 400px;">
<div class="layui-carousel" id="ID-carousel-0" style="margin-top: 10px;">
<div carousel-item>
<div>
<img style="width: 100%" src="/Uploadfiles/Picture/2021-11-30/202111301346189407.jpg" />
</div>
<div>
<img style="width: 100%" src="/Uploadfiles/Picture/2021-11-30/202111301346591448.jpg" />
</div>
<div>
<img style="width: 100%" src="/Uploadfiles/Picture/2021-11-30/202111301345508450.jpg" />
</div>
</div>
</div>
</dd>
<dd style="height: 400px; text-align: center;">
<div class="carouselDiv" style="text-align: left; padding-left: 20px; margin-top: 30px;">
<p><strong>2007年</strong> 国家高新技术企业</p>
<p><strong>2011年</strong> 四川省天然药物分离纯化工程技术研究中心</p>
<p><strong>2015年</strong> 四川省天然化合物库获得四川省科技厅及四川省经信厅项目立项</p>
<p><strong>2017年</strong> 国家中小企业公共服务示范平台，四川省服务型制造示范企业，成都市科技进步奖三等奖</p>
<p><strong>2018年</strong> 中国食品药品检定研究院标准物质原料供应商（第一批），成都市天然药物分离纯化创新示范中心</p>
<p><strong>2019年</strong> CNAS认证检验检能力认可实验室</p>
<p><strong>2021年</strong> 成都市“守合同 重信用”企业</p>
<p><strong>2023年</strong> 武侯区创新药（含中医药）产业优势企业，武侯区优质创新平台</p>
<p><strong>2024年</strong> 成都市中药创新药物中试研发服务平台</p>
</div>
</dd>
</dl>
</div>
</div>
</div>
</div>
</div>
<div class="pushDiv" style="background-color: #f4f9fd; padding: 30px 0px;">
<div class="iboxlist clearfix" style="display: flex; border-radius: 10px; overflow: hidden; border: solid 1px #e9e8e8; padding: 0px; background-color: white;">
<div class="layui-tab layui-tab-brief" id="tab-zyxx1" style="width: 100%; height: 410px;" lay-filter="tab-pushtab1">
<ul class="layui-tab-title" style="width: 100%;">
<li class="layui-this" style="float: left; right: -10px;"><strong style="font-size: 18px;">专利</strong> </li>
<li style="float: left; right: -10px;"><strong style="font-size: 18px;">论文</strong></li>
</ul>
<div class="layui-tab-content">
<div class="layui-tab-item layui-show">
<div class="swiper" id="swiper-zl">
<div class="swiper-wrapper">
<div class="swiper-slide">
<a href="/images/zl/zl1.png" class="pimg" title="发明专利">
<img src="images/zl/zl1.png" /></a>
</div>
<div class="swiper-slide">
<a href="/images/zl/zl2.png" class="pimg" title="发明专利">
<img src="images/zl/zl2.png" /></a>
</div>
<div class="swiper-slide">
<a href="/images/zl/zl3.png" class="pimg" title="发明专利">
<img src="images/zl/zl3.png" /></a>
</div>
<div class="swiper-slide">
<a href="/images/zl/zl4.png" class="pimg" title="发明专利">
<img src="images/zl/zl4.png" /></a>
</div>
<div class="swiper-slide">
<a href="/images/zl/zl5.png" class="pimg" title="发明专利">
<img src="images/zl/zl5.png" /></a>
</div>
<div class="swiper-slide">
<a href="/images/zl/zl6.png" class="pimg" title="发明专利">
<img src="images/zl/zl6.png" /></a>
</div>
<div class="swiper-slide">
<a href="/images/zl/zl7.png" class="pimg" title="发明专利">
<img src="images/zl/zl7.png" /></a>
</div>
<div class="swiper-slide">
<a href="/images/zl/zl8.png" class="pimg" title="发明专利">
<img src="images/zl/zl8.png" /></a>
</div>
<div class="swiper-slide">
<a href="/images/zl/zl9.png" class="pimg" title="发明专利">
<img src="images/zl/zl9.png" /></a>
</div>
</div>
<div class="swiper-button-next"></div>
<div class="swiper-button-prev"></div>
</div>
</div>
<div class="layui-tab-item">
<div style="padding: 12px 20px; border-bottom: solid 1px #eee;">
<a target="_blank" href="info.aspx?id=540">Lei Xiang.et al.High-throughput profiling of chemical-induced gene expression across 93,644 perturbations[J].Nature Methods,2025(22):1954-1963
</a>
</div>
</dl>
<div style="padding: 12px 20px; border-bottom: solid 1px #eee;">
<a target="_blank" href="info.aspx?id=543">Qi Cui.et al.Synergistic coupling of ultrasonic cavitation with tailored deep eutectic solvent systems for intensified extraction of Scutellaria Radix flavonoids: Modelling and optimization by genetic algorithm[J].Ultrasonics Sonochemistry,2025(119):107386
</a>
</div>
</dl>
<div style="padding: 12px 20px; border-bottom: solid 1px #eee;">
<a target="_blank" href="info.aspx?id=544">Chenlu Liu.et al.Ultrasound-assisted enzyme extraction of total flavonoids from lotus leaf (Nelumbo nucifera Gaertn.) and its antioxidant activity[J].LWT-Food Science and Technology,2025(215):117224
</a>
</div>
</dl>
<div style="padding: 12px 20px; text-align: right;">
<a href="/news.aspx?id=303">[访问更多信息 →]</a>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footbox">
<dl class="foot clearfix" style="width:1170px;">
<dl style="height:135px;display:flex;justify-content:space-between;"><dd class="finfobox"><p class="clearfix" style="font-weight:600;font-size:16px;width:360px;">联系我们</p><p class="clearfix"><span class="i fi1"></span>4000-369-963 &nbsp;028-85370565</p><p class="clearfix num"><span class="i fi2"></span>3004654993@qq.com</p><p class="clearfix"><span class="i fi3"></span>四川省 成都市 武侯区 武科西二路8号</p></dd><dd class="finfobox"><p class="clearfix" style="font-weight:600;font-size:16px;text-align:center;">关于普思</p><p class="clearfix" style="text-align:center;"> &nbsp;<a href="https://www.push-herbchem.com/news.aspx?id=198" target="_self">新闻资讯</a></p><p class="clearfix" style="text-align:center;"><a href="https://www.push-herbchem.com/about.aspx?id=324" target="_self">研发机构</a></p><p class="clearfix" style="text-align:center;"> &nbsp;<a href="https://www.push-herbchem.com/about.aspx?id=15" target="_self">服务平台</a></p></dd><dd class="finfobox"><p class="clearfix" style="font-weight:600;font-size:16px;text-align:center;">产品</p><p class="clearfix" style="text-align:center;"><a href="https://www.push-herbchem.com/ps_Product.aspx?id=222" target="_self">中药化学对照品</a></p><p class="clearfix" style="text-align:center;"><a href="https://www.push-herbchem.com/ps_danti.aspx?id=226" target="_self">化合物库</a></p><p class="clearfix" style="text-align:center;"><a href="https://www.push-herbchem.com/ps_BulkGood.aspx?id=316" target="_self">热销原料</a></p></dd><dd class="finfobox"><p class="clearfix" style="font-weight:600;font-size:16px;text-align:center;">技术服务</p><p class="clearfix" style="text-align:center;"><a href="https://www.push-herbchem.com/ps_Product.aspx?id=295" target="_self">高分辨质谱分析</a></p><p class="clearfix" style="text-align:center;"><a href="https://www.push-herbchem.com/ps_Product.aspx?id=271" target="_self">药物单体纯化</a></p><p class="clearfix" style="text-align:center;"><a href="https://www.push-herbchem.com/ps_Product.aspx?id=287" target="_self">中药创新药</a></p></dd><dd class="finfobox"> <img style="width:110px;height:110px;float:right;" src="/img/ewm.jpg" /></dd></dl><div style="text-align:center;border-top:solid 1px #565555;"><p style="padding:8px;">普思生物为您提供中药化学对照品、高纯化学试剂、天然产物化合物库等优质产品，<br />仅用于科学研究、工业应用等非医疗用途范畴，不可用于人的临床治疗或试验，非药用，非食用。</p></div><div style="text-align:center;"><p style="padding:5px;">友情链接：<a title="全球化学品供应商搜索" href="https://www.chemicalbook.com/" target="_self" textvalue="chemical book"></a><a title="全球化学品供应商搜索" href="https://www.chemicalbook.com/" target="_self">全球化学品供应商搜索</a> &nbsp; <a title="盖德化工网" href="http://china.guidechem.com/" target="_self">盖德化工网</a> &nbsp; &nbsp;成都普思生物科技股份有限公司版权所有 &nbsp; 蜀ICP备08100078号 </p></div>
</dl>
</div>
<script type="text/javascript" src="js/page.js"></script>
<script type="text/javascript" src="js/jquery.bxslider.js"></script>
<script>
    var _hmt = _hmt || [];
    (function () {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?20387fea3ba5aa2fad465840f41225a3";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(hm, s);
    })();
</script>
<script>
    (function () {
        var bp = document.createElement('script');
        var curProtocol = window.location.protocol.split(':')[0];
        if (curProtocol === 'https') {
            bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
        }
        else {
            bp.src = 'http://push.zhanzhang.baidu.com/push.js';
        }
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(bp, s);
    })();
</script>
<style type="text/css">
    /*new right*/
.cndns-right{position:fixed;right:1px;top:75%;margin-top:-100px;z-index:100}
.cndns-right-meau{position:relative;}
.cndns-right-btn{width:48px;height:48px;border:1px solid #ddd;text-align:center;display:block;margin-bottom:6px;position:relative;background-color:#fff}
.cndns-right-btn span{color:#848484;font-size:26px;line-height:48px;}
.cndns-right-btn p{color:#1580c4;font-size:14px;line-height:18px;padding-top:5px;display:none;}
.cndns-right-meau:hover .cndns-right-btn span{display:none}
.cndns-right-meau:hover .cndns-right-btn p{display:block;}
.meau-car .cndns-right-btn {border-color:#1580c4;margin-bottom:20px;}
.meau-car.cndns-right-meau:hover .cndns-right-btn{background-color:#1580c4}
.meau-car.cndns-right-meau:hover .cndns-right-btn span{color:#fff;display:block;}
.meau-car .cndns-right-btn span{color:#1580c4;}
.meau-sev .cndns-right-btn{border-color:#ff6800;background:url(../images/zxkf.gif) no-repeat #ff6800 center;} 
.meau-sev .cndns-right-btn p{color:#fff}
.meau-sev .cndns-right-btn span{color:#fff}
.meau-top .cndns-right-btn span{font-size:12px;line-height:12px;padding-top:10px;display:block}
.meau-top .cndns-right-btn i{display:block;color:#999}
.meau-top.cndns-right-meau:hover .cndns-right-btn{background-color:#1580c4}
.meau-top.cndns-right-meau:hover .cndns-right-btn span{display:block;color:#fff} 
.meau-top.cndns-right-meau:hover .cndns-right-btn i{color:#fff;}
.cndns-right-box{position:absolute;top:-15px;right:48px;padding-right:25px;display:none;}
.cndns-right-box .box-border{border:1px solid #ccc;border-top:4px solid #1580c4;padding:20px;background-color:#fff;-webkit-box-shadow: 0 3px 8px rgba(0,0,0,.15);-moz-box-shadow: 0 3px 8px rgba(0,0,0,.15);box-shadow: 0 3px 8px rgba(0,0,0,.15);position:relative}
.cndns-right-box .box-border .arrow-right{display:block;width:13px;height:16px;background:url(../images/arrow1.png) no-repeat;position:absolute;right:-13px;top:26px;}
.cndns-right-box .box-border .sev-t span{font-size:42px;float:left;display:block;line-height:56px;margin-right:20px;color:#d3d3d3}
.cndns-right-box .box-border .sev-t p{float:left;color:#ff6800;font-size:24px;line-height:28px;}
.cndns-right-box .box-border .sev-t p i{display:block;font-size:14px;color:#aaa;}
.cndns-right-box .box-border .sev-b{padding-top:15px;margin-top:15px;border-top:1px solid #e4e4e4}
.cndns-right-box .box-border .sev-b h4{color:#666;font-size:14px;font-weight:normal;padding-bottom:15px;}
.cndns-right-box .box-border .sev-b li{float:left;width:33.33333%}
.cndns-right-box .box-border .sev-b li a{display:inline-block;color:#999;font-size:13px;padding-left:43px;background:url(../images/qq.gif) no-repeat left 3px;line-height:36px;}
.cndns-right-box .box-border .sev-b li a:hover{color:#1580c4}
.meau-sev .cndns-right-box .box-border{width:430px;height:150px;}
.meau-contact .cndns-right-box .box-border{width:230px;height:80px;}
.cndns-right-meau:hover .cndns-right-box{display:block}
.meau-code .cndns-right-box{top:inherit;bottom:-35px;}
.meau-code .cndns-right-box .box-border{width:156px;text-align:center;border-top:1px solid #ccc;}
.meau-code .cndns-right-box .box-border i{display:block;color:#1580c4;font-size:16px;line-height:16px;}
.meau-code .cndns-right-box .box-border .arrow-right{top:inherit;bottom:50px;}
.meau-sev .cndns-right-btn .demo-icon{display:none;}
.meau-sev:hover .cndns-right-btn{background:#1580c4;border-color: #1580c4;}
.meau-zs .cndns-right-btn{background-color:#1580c4;color:#fff;margin-top:80px;border-color:#1580c4}
.meau-zs .cndns-right-btn span{color:#fff}
.meau-zs .cndns-right-btn p{color:#fff}
@font-face {
	font-family: 'icomoon';
    src:url('../font/icomoon.eot?qradjf');
    src:url('../font/icomoon.eot?qradjf#iefix') format('embedded-opentype'),
        url('../font/icomoon.ttf?qradjf') format('truetype'),
        url('../font/icomoon.woff?qradjf') format('woff'),
        url('../font/icomoon.svg?qradjf#icomoon') format('svg');
    font-weight: normal;
    font-style: normal;
}
</style>
<div class="cndns-right">
<div class="cndns-right-meau meau-sev">
<a href="javascript:" class="cndns-right-btn">
<span class="demo-icon">&#xe901;</span>
<p>
在线<br />
咨询
</p>
</a>
<div class="cndns-right-box">
<div class="box-border">
<div class="sev-t" style="height:50px;">
<span class="demo-icon">&#xe901;</span>
<p>在线咨询<i>服务时间：8:30-17:30</i></p>
<div class="clear"></div>
</div>
<div class="sev-b">
<h4>选择客服在线沟通：</h4>
<ul id="zixunUl">
<li><a href="javascript:void(0);" onclick="javascript:window.open('https://wpa.qq.com/msgrd?v=3&uin=3004654993&site=qq&menu=yes')">何女士</a></li>
</ul>
<div class="clear"></div>
</div>
<span class="arrow-right"></span>
</div>
</div>
</div>
<div class="cndns-right-meau meau-contact">
<a href="javascript:" class="cndns-right-btn">
<span class="demo-icon">&#xe902;</span>
<p>
咨询<br />
热线
</p>
</a>
<div class="cndns-right-box">
<div class="box-border">
<div class="sev-t">
<span class="demo-icon">&#xe902;</span>
<p>4000-369-963&nbsp;&nbsp;<br />
<i>7*24小时客服服务热线</i></p><br />
028-85370565 / 18080489829 （何女士）
<div class="clear"></div>
</div>
<span class="arrow-right"></span>
</div>
</div>
</div>
<div class="cndns-right-meau meau-code">
<a href="javascript:" class="cndns-right-btn">
<span class="demo-icon">&#xe903;</span>
<p>
关注<br />
微信
</p>
</a>
<div class="cndns-right-box">
<div class="box-border">
<div class="sev-t">
<img src="images/ewm.jpg" width="117" height="117"/>
<i>关注官方微信</i>
</div>
<span class="arrow-right"></span>
</div>
</div>
</div>
<div class="cndns-right-meau meau-top" id="top-back">
<a href="javascript:scroll(0,0)" class="cndns-right-btn">
<span class="demo-icon">&#xe904;</span>
<i>顶部</i>
</a>
</div>
</div>
<script src="js/jquery.lightbox-0.5.js"></script>
<script type="text/javascript">
        //<![CDATA[ 
        jQuery(function () {
            //banner
            var bannersider = jQuery('.bannerbox ul').bxSlider({
                auto: true,
                //autoControls: true,
                speed: 1500,
            });
            jQuery('.bannerbox').mouseenter(function () {
                jQuery(this).find(".bx-prev").stop().animate({ left: "0px" }, 400);
                jQuery(this).find(".bx-next").stop().animate({ right: "0px" }, 400);
                bannersider.stopAuto();
            })
            jQuery('.bannerbox').mouseleave(function () {
                jQuery(this).find(".bx-prev").stop().animate({ left: "-48px" }, 400);
                jQuery(this).find(".bx-next").stop().animate({ right: "-48px" }, 400);
                bannersider.startAuto();
            })
            jQuery(".new-lbox li").mouseenter(function () {
                alert(1);
                jQuery(this).addClass("act");
            })
            jQuery(".new-lbox li").mouseleave(function () {
                alert(2);
                jQuery(this).removeClass("act");
            })

            var swiper = new Swiper('.swiper', {
                slidesPerView: 4,
                direction: 'horizontal',
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
                on: {
                    resize: function () {
                        swiper.changeDirection('horizontal');
                    },
                },
            });
        })
        //]]>
        layui.use(function () {
            var carousel = layui.carousel;
            // 渲染 - 常规轮播
            //carousel.render({
            //    elem: '#ID-carousel-demo-1',
            //    width: 'auto'
            //});
            //var element = layui.element;
            //element.on('tab(tab-pushtab)', function (data) {
            //    // 更稳妥的方法是先销毁再重新创建
            //    var carouselInstance = carousel.reload('tab-pushtab', {}); // 这里只是为了演示，实际上你应该先调用 destroy 方法。
            //    carouselInstance.destroy('tab-pushtab'); // 销毁 carousel 实例，确保完全清除之前的实例和事件绑定。
            //    carousel.render({
            //        elem: '#ID-carousel-' + data.index,
            //        interval: 1800,
            //        anim: 'fade',
            //        width: 'auto',
            //        height: '120px'
            //    });
            //});
            //element.tabChange('tab-zyxx', 0);
            // 渲染 - 设置时间间隔、动画类型、宽高度等属性
            //$("#tab-zyxx ul :first-child").click();
            carousel.render({
                elem: '#ID-carousel-0',
                interval: 1800,
                anim: 'fade',
                width: 'auto',
                height: '400px'
            });
            carousel.render({
                elem: '#ID-carousel-1',
                interval: 1800,
                anim: 'fade',
                width: 'auto',
                height: '400px'
            });
            carousel.render({
                elem: '#ID-carousel-2',
                interval: 1800,
                anim: 'fade',
                width: 'auto',
                height: '400px'
            });

        });

        const video = document.getElementById('video');
        const playButton = document.getElementById('play-button');
        const playWarn = document.getElementById('divwarning');
        video.addEventListener('click', () => {

            if (video.paused) {
                //video.play();
                //playButton.style.display = 'none';
            } else {
                //video.pause();
                //playWarn.style.display = 'flex';
                //alert(2);
            }
        });
        playButton.addEventListener('click', () => {

            if (video.paused) {
                video.play();
                //playWarn.style.display = 'none';
                //alert(1);
            }
        });
        video.addEventListener('pause', () => {
            playWarn.style.display = 'flex';
        });

        video.addEventListener('play', () => {
            playWarn.style.display = 'none';
        });

        window.onload = () => {
            playButton.style.display = 'flex'; // Initially show play button
        };

        jQuery('#swiper-zl div a.pimg').lightBox();
    </script>
</body>
</html>
