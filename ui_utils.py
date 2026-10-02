import streamlit as st
import random
import json
import streamlit.components.v1 as components

# ─── TTS: inject listener vào PARENT page (st.markdown, không bị sandbox) ───
# Dùng postMessage để iframe → parent phát âm tiếng Trung chuẩn
_TTS_PARENT_JS = r"""
<script>
(function(){
  if (window.__chineseTTSReady) return;
  window.__chineseTTSReady = true;

  // Map: pinyin+tone_number → chữ Hán đại diện
  const P2H = {
    'a1':'啊','a2':'阿','a3':'啊','a4':'啊',
    'o1':'哦','o2':'哦','o3':'哦','o4':'哦',
    'e1':'鹅','e2':'鹅','e3':'鹅','e4':'鹅',
    'ai1':'哎','ai2':'哎','ai3':'哎','ai4':'哎',
    'ei1':'欸','ei2':'欸','ei3':'欸','ei4':'欸',
    'ao1':'熬','ao2':'熬','ao3':'袄','ao4':'奥',
    'ou1':'欧','ou2':'欧','ou3':'呕','ou4':'偶',
    'an1':'安','an2':'安','an3':'安','an4':'暗',
    'en1':'恩','en2':'恩','en3':'恩','en4':'恩',
    'ang1':'昂','ang2':'昂','ang3':'昂','ang4':'昂',
    'eng1':'嗯','eng2':'嗯','eng3':'嗯','eng4':'嗯',
    'er2':'儿','er3':'耳','er4':'二',
    'yi1':'一','yi2':'宜','yi3':'已','yi4':'义',
    'wu1':'乌','wu2':'吴','wu3':'五','wu4':'物',
    'yu1':'淤','yu2':'鱼','yu3':'语','yu4':'玉',
    'ba1':'巴','ba2':'拔','ba3':'把','ba4':'爸',
    'bo1':'波','bo2':'伯','bo3':'钵','bo4':'薄',
    'bi1':'逼','bi2':'鼻','bi3':'比','bi4':'必',
    'bu1':'逋','bu2':'步','bu3':'补','bu4':'布',
    'bai1':'掰','bai2':'白','bai3':'百','bai4':'败',
    'bei1':'杯','bei2':'北','bei3':'北','bei4':'被',
    'bao1':'包','bao2':'薄','bao3':'保','bao4':'报',
    'ban1':'班','ban2':'版','ban3':'板','ban4':'办',
    'ben1':'奔','ben2':'盆','ben3':'本','ben4':'笨',
    'bang1':'帮','bang2':'棒','bang3':'绑','bang4':'棒',
    'beng1':'崩','beng2':'绷','beng3':'绷','beng4':'蹦',
    'bian1':'边','bian2':'编','bian3':'扁','bian4':'变',
    'biao1':'标','biao3':'表','biao4':'裱',
    'bie1':'憋','bie2':'别','bie4':'别',
    'bin1':'宾','bin2':'贫','bin4':'鬓',
    'bing1':'冰','bing2':'瓶','bing3':'饼','bing4':'病',
    'pa1':'趴','pa2':'爬','pa3':'爬','pa4':'怕',
    'po1':'泼','po2':'婆','po3':'颇','po4':'破',
    'pi1':'批','pi2':'皮','pi3':'屁','pi4':'屁',
    'pu1':'扑','pu2':'葡','pu3':'普','pu4':'铺',
    'pai1':'拍','pai2':'排','pai4':'派',
    'pei1':'胚','pei2':'培','pei4':'配',
    'pao1':'抛','pao2':'跑','pao3':'跑','pao4':'炮',
    'pan1':'攀','pan2':'盘','pan4':'盼',
    'pen1':'喷','pen2':'盆','pen4':'喷',
    'pang1':'乒','pang2':'旁','pang4':'胖',
    'peng1':'烹','peng2':'朋','peng3':'捧','peng4':'碰',
    'pian1':'偏','pian2':'便','pian4':'骗',
    'piao1':'飘','piao2':'漂','piao3':'漂','piao4':'票',
    'pie1':'撇','pie2':'撇','pie4':'撇',
    'pin1':'拼','pin2':'贫','pin3':'品','pin4':'品',
    'ping1':'乒','ping2':'平','ping3':'屏','ping4':'评',
    'ma1':'妈','ma2':'麻','ma3':'马','ma4':'骂',
    'mi1':'眯','mi2':'迷','mi3':'米','mi4':'密',
    'mo1':'摸','mo2':'摩','mo3':'摩','mo4':'末',
    'mu1':'亩','mu2':'木','mu3':'母','mu4':'木',
    'mai1':'埋','mai2':'埋','mai3':'买','mai4':'卖',
    'mei1':'没','mei2':'没','mei3':'美','mei4':'妹',
    'mao1':'猫','mao2':'毛','mao3':'卯','mao4':'帽',
    'mou1':'谋','mou2':'谋','mou3':'某',
    'man1':'蛮','man2':'蛮','man3':'满','man4':'慢',
    'men1':'闷','men2':'门','men4':'闷',
    'mang1':'忙','mang2':'忙','mang3':'莽','mang4':'莽',
    'meng1':'蒙','meng2':'蒙','meng3':'猛','meng4':'梦',
    'mian1':'棉','mian2':'棉','mian3':'免','mian4':'面',
    'miao1':'喵','miao2':'描','miao3':'秒','miao4':'庙',
    'mie1':'灭','mie2':'灭','mie4':'灭',
    'min1':'敏','min2':'民','min3':'闽','min4':'敏',
    'ming1':'明','ming2':'明','ming3':'皿','ming4':'命',
    'fa1':'发','fa2':'罚','fa3':'法','fa4':'发',
    'fo1':'佛','fo2':'佛',
    'fei1':'飞','fei2':'肥','fei3':'匪','fei4':'费',
    'fu1':'夫','fu2':'服','fu3':'辅','fu4':'父',
    'fan1':'翻','fan2':'凡','fan3':'反','fan4':'饭',
    'fen1':'分','fen2':'坟','fen3':'粉','fen4':'奋',
    'fang1':'方','fang2':'房','fang3':'访','fang4':'放',
    'feng1':'风','feng2':'冯','feng3':'讽','feng4':'奉',
    'da1':'搭','da2':'答','da3':'打','da4':'大',
    'de1':'的','de2':'的','de3':'的',
    'di1':'低','di2':'敌','di3':'底','di4':'地',
    'du1':'都','du2':'读','du3':'赌','du4':'度',
    'dai1':'呆','dai2':'代','dai3':'逮','dai4':'代',
    'dao1':'刀','dao2':'到','dao3':'倒','dao4':'到',
    'dou1':'都','dou2':'豆','dou3':'斗','dou4':'豆',
    'dan1':'单','dan2':'淡','dan3':'胆','dan4':'淡',
    'deng1':'灯','deng2':'等','deng3':'等','deng4':'瞪',
    'dang1':'当','dang2':'党','dang3':'当','dang4':'挡',
    'dong1':'东','dong2':'同','dong3':'懂','dong4':'动',
    'dian1':'颠','dian2':'甜','dian3':'点','dian4':'店',
    'diao1':'刁','diao2':'吊','diao4':'吊',
    'die1':'跌','die2':'碟','die4':'叠',
    'ding1':'丁','ding2':'钉','ding3':'顶','ding4':'定',
    'diu1':'丢',
    'duan1':'端','duan2':'段','duan3':'短','duan4':'段',
    'dui1':'堆','dui4':'对',
    'dun1':'敦','dun2':'吨','dun4':'盾',
    'ta1':'他','ta2':'他','ta3':'她','ta4':'踏',
    'ti1':'踢','ti2':'题','ti3':'体','ti4':'替',
    'tu1':'凸','tu2':'图','tu3':'土','tu4':'吐',
    'tai1':'胎','tai2':'台','tai3':'太','tai4':'太',
    'tao1':'掏','tao2':'逃','tao3':'讨','tao4':'套',
    'tou1':'偷','tou2':'投','tou4':'透',
    'tan1':'贪','tan2':'谈','tan3':'毯','tan4':'探',
    'teng1':'疼','teng2':'疼',
    'tang1':'汤','tang2':'糖','tang3':'躺','tang4':'趟',
    'tong1':'通','tong2':'同','tong3':'桶','tong4':'痛',
    'tian1':'天','tian2':'甜','tian3':'舔','tian4':'填',
    'tiao1':'挑','tiao2':'调','tiao4':'跳',
    'tie1':'贴','tie3':'铁',
    'ting1':'听','ting2':'停','ting3':'艇',
    'tuan1':'团','tuan2':'团',
    'tui1':'推','tui3':'腿','tui4':'退',
    'tun1':'吞','tun2':'臀',
    'na1':'拿','na2':'拿','na3':'那','na4':'那',
    'ne1':'呢','ne2':'呢',
    'ni1':'泥','ni2':'泥','ni3':'你','ni4':'逆',
    'nu1':'奴','nu2':'奴','nu3':'努','nu4':'怒',
    'nai1':'奶','nai2':'奶','nai3':'乃','nai4':'耐',
    'nei1':'内','nei4':'内',
    'nao1':'挠','nao2':'挠','nao3':'脑','nao4':'闹',
    'nan1':'难','nan2':'南','nan3':'赧','nan4':'难',
    'nen1':'嫩','nen4':'嫩',
    'nang1':'囔','nang2':'囊',
    'neng1':'能','neng2':'能',
    'nong1':'农','nong2':'农','nong4':'弄',
    'nian1':'拈','nian2':'年','nian3':'捻','nian4':'念',
    'niao1':'尿','niao2':'鸟','niao3':'鸟','niao4':'尿',
    'nie1':'捏','nie2':'捏','nie4':'啮',
    'nin2':'您','nin3':'您',
    'ning1':'拧','ning2':'宁','ning3':'拧','ning4':'泞',
    'niu1':'纽','niu2':'牛','niu3':'扭','niu4':'纽',
    'nuan3':'暖',
    'la1':'拉','la2':'蜡','la3':'辣','la4':'辣',
    'le1':'了','le2':'了',
    'li1':'里','li2':'离','li3':'里','li4':'力',
    'lu1':'路','lu2':'炉','lu3':'旅','lu4':'路',
    'lai1':'来','lai2':'来','lai3':'来','lai4':'赖',
    'lei1':'类','lei2':'雷','lei3':'类','lei4':'类',
    'lao1':'捞','lao2':'老','lao3':'老','lao4':'烙',
    'lou1':'楼','lou2':'楼','lou3':'搂','lou4':'露',
    'lan1':'兰','lan2':'蓝','lan3':'懒','lan4':'烂',
    'leng1':'冷','leng2':'棱','leng3':'冷','leng4':'愣',
    'lang1':'琅','lang2':'郎','lang3':'朗','lang4':'浪',
    'long1':'龙','long2':'龙','long3':'拢','long4':'弄',
    'lian1':'帘','lian2':'联','lian3':'脸','lian4':'链',
    'liao1':'撩','liao2':'了','liao3':'了','liao4':'料',
    'lie1':'列','lie2':'列','lie4':'裂',
    'lin1':'淋','lin2':'林','lin3':'凛','lin4':'吝',
    'ling1':'令','ling2':'零','ling3':'领','ling4':'令',
    'liu1':'溜','liu2':'流','liu3':'柳','liu4':'六',
    'luan1':'乱','luan2':'卵','luan4':'乱',
    'lun1':'轮','lun2':'轮','lun4':'论',
    'ga1':'嘎','ga2':'尬','ga4':'嘎',
    'ge1':'歌','ge2':'格','ge3':'个','ge4':'个',
    'gu1':'估','gu2':'骨','gu3':'古','gu4':'故',
    'gai1':'该','gai2':'改','gai3':'改','gai4':'盖',
    'gei3':'给',
    'gao1':'高','gao2':'搞','gao3':'搞','gao4':'告',
    'gou1':'钩','gou2':'狗','gou3':'狗','gou4':'够',
    'gan1':'干','gan2':'感','gan3':'感','gan4':'干',
    'gen1':'根','gen2':'亘','gen4':'根',
    'gang1':'钢','gang2':'肛','gang3':'港','gang4':'钢',
    'geng1':'更','geng2':'耕','geng4':'更',
    'gong1':'工','gong2':'共','gong3':'弓','gong4':'共',
    'guan1':'关','guan2':'观','guan3':'管','guan4':'惯',
    'guai1':'乖','guai2':'拐','guai3':'拐','guai4':'怪',
    'guo1':'锅','guo2':'国','guo3':'果','guo4':'过',
    'gui1':'规','gui2':'鬼','gui3':'鬼','gui4':'贵',
    'gun1':'滚','gun3':'滚',
    'guang1':'光','guang3':'广','guang4':'逛',
    'ka1':'喀','ka2':'卡','ka3':'卡','ka4':'咔',
    'ke1':'科','ke2':'课','ke3':'可','ke4':'课',
    'ku1':'枯','ku2':'苦','ku3':'苦','ku4':'库',
    'kai1':'开','kai2':'凯','kai3':'凯','kai4':'凯',
    'kao1':'考','kao2':'靠','kao3':'考','kao4':'靠',
    'kou1':'口','kou3':'口','kou4':'扣',
    'kan1':'看','kan2':'砍','kan3':'砍','kan4':'看',
    'ken1':'肯','ken2':'垦','ken3':'肯','ken4':'啃',
    'kang1':'抗','kang2':'扛','kang4':'抗',
    'keng1':'坑',
    'kong1':'空','kong2':'控','kong3':'孔','kong4':'空',
    'kuan1':'宽','kuan3':'款',
    'kuai1':'快','kuai2':'筷','kuai4':'快',
    'kuo1':'扩','kuo4':'阔',
    'kui1':'亏','kui2':'愧','kui3':'魁','kui4':'愧',
    'kun1':'昆','kun2':'困','kun3':'捆','kun4':'困',
    'kuang1':'筐','kuang2':'狂','kuang3':'矿','kuang4':'旷',
    'ha1':'哈','ha2':'哈','ha3':'哈','ha4':'哈',
    'he1':'喝','he2':'和','he3':'喝','he4':'和',
    'hu1':'呼','hu2':'胡','hu3':'虎','hu4':'护',
    'hai1':'还','hai2':'还','hai3':'海','hai4':'害',
    'hei1':'黑',
    'hao1':'好','hao2':'好','hao3':'好','hao4':'好',
    'hou1':'后','hou2':'喉','hou3':'吼','hou4':'后',
    'han1':'寒','han2':'汉','han3':'汉','han4':'汉',
    'hen1':'很','hen2':'很','hen3':'很','hen4':'恨',
    'hang1':'航','hang2':'行',
    'heng1':'哼','heng2':'横',
    'hong1':'轰','hong2':'红','hong3':'哄',
    'huan1':'欢','huan2':'环','huan3':'缓','huan4':'换',
    'huai1':'怀','huai2':'怀','huai4':'坏',
    'huo1':'豁','huo2':'活','huo3':'火','huo4':'货',
    'hui1':'灰','hui2':'回','hui3':'汇','hui4':'会',
    'hun1':'婚','hun2':'魂','hun4':'混',
    'huang1':'慌','huang2':'黄','huang3':'谎','huang4':'晃',
    'ji1':'鸡','ji2':'及','ji3':'几','ji4':'计',
    'jia1':'家','jia2':'夹','jia3':'假','jia4':'价',
    'jie1':'街','jie2':'节','jie3':'姐','jie4':'借',
    'jiao1':'交','jiao2':'嚼','jiao3':'脚','jiao4':'叫',
    'ju1':'居','ju2':'菊','ju3':'举','ju4':'句',
    'juan1':'卷','juan3':'卷','juan4':'卷',
    'jue1':'绝','jue2':'绝','jue4':'绝',
    'jun1':'君','jun2':'均','jun3':'俊','jun4':'峻',
    'jian1':'间','jian2':'剪','jian3':'简','jian4':'见',
    'jiang1':'江','jiang2':'讲','jiang3':'讲','jiang4':'降',
    'jiong1':'窘',
    'jin1':'今','jin2':'进','jin3':'紧','jin4':'进',
    'jing1':'京','jing2':'净','jing3':'景','jing4':'静',
    'jiu1':'究','jiu2':'就','jiu3':'久','jiu4':'就',
    'qi1':'七','qi2':'其','qi3':'起','qi4':'气',
    'qia1':'掐','qia3':'洽','qia4':'恰',
    'qie1':'切','qie2':'且','qie4':'切',
    'qiao1':'敲','qiao2':'桥','qiao3':'巧','qiao4':'翘',
    'qu1':'区','qu2':'取','qu3':'取','qu4':'去',
    'quan1':'圈','quan2':'全','quan3':'犬','quan4':'劝',
    'que1':'缺','que2':'确','que4':'确',
    'qun2':'裙',
    'qian1':'千','qian2':'钱','qian3':'浅','qian4':'欠',
    'qiang1':'枪','qiang2':'强','qiang3':'抢',
    'qiong2':'穷',
    'qin1':'亲','qin2':'琴','qin3':'寝',
    'qing1':'清','qing2':'情','qing3':'请','qing4':'庆',
    'qiu1':'秋','qiu2':'球',
    'xi1':'西','xi2':'习','xi3':'洗','xi4':'系',
    'xia1':'霞','xia2':'峡','xia4':'夏',
    'xie1':'鞋','xie2':'斜','xie3':'写','xie4':'谢',
    'xiao1':'消','xiao2':'笑','xiao3':'小','xiao4':'笑',
    'xu1':'需','xu2':'续','xu3':'许','xu4':'序',
    'xuan1':'宣','xuan2':'旋','xuan3':'选','xuan4':'炫',
    'xue1':'学','xue2':'学','xue3':'雪','xue4':'血',
    'xun1':'寻','xun2':'训','xun4':'训',
    'xian1':'先','xian2':'闲','xian3':'显','xian4':'现',
    'xiang1':'香','xiang2':'祥','xiang3':'想','xiang4':'向',
    'xiong1':'兄','xiong2':'熊',
    'xin1':'心','xin2':'信','xin4':'信',
    'xing1':'星','xing2':'行','xing3':'醒','xing4':'兴',
    'xiu1':'修','xiu2':'秀','xiu4':'秀',
    'zha1':'渣','zha2':'炸','zha3':'眨','zha4':'诈',
    'zhe1':'这','zhe2':'折','zhe3':'者','zhe4':'这',
    'zhi1':'知','zhi2':'直','zhi3':'只','zhi4':'至',
    'zhu1':'猪','zhu2':'住','zhu3':'主','zhu4':'住',
    'zhua1':'抓','zhua3':'爪',
    'zhuo1':'桌','zhuo2':'桌','zhuo4':'卓',
    'zhui1':'追','zhui4':'坠',
    'zhun3':'准',
    'zhai1':'摘','zhai2':'宅','zhai3':'窄','zhai4':'债',
    'zhao1':'招','zhao2':'找','zhao3':'找','zhao4':'照',
    'zhou1':'周','zhou2':'肘','zhou4':'皱',
    'zhan1':'占','zhan2':'站','zhan3':'展','zhan4':'战',
    'zhen1':'真','zhen2':'针','zhen3':'枕','zhen4':'阵',
    'zhang1':'张','zhang2':'掌','zhang3':'掌','zhang4':'障',
    'zheng1':'征','zheng2':'整','zheng3':'整','zheng4':'正',
    'zhong1':'中','zhong2':'重','zhong3':'种','zhong4':'重',
    'zhuan1':'专','zhuan2':'转','zhuan3':'转','zhuan4':'传',
    'zhuang1':'装','zhuang4':'壮',
    'cha1':'插','cha2':'茶','cha3':'差','cha4':'差',
    'che1':'车','che2':'扯','che4':'彻',
    'chi1':'吃','chi2':'迟','chi3':'尺','chi4':'翅',
    'chu1':'出','chu2':'厨','chu3':'楚','chu4':'处',
    'chuo1':'戳','chuo4':'戳',
    'chui1':'吹','chui2':'锤',
    'chun1':'春','chun2':'纯','chun3':'蠢',
    'chai1':'拆','chai2':'柴',
    'chao1':'超','chao2':'潮','chao3':'炒',
    'chou1':'抽','chou2':'愁','chou3':'丑','chou4':'臭',
    'chan1':'掺','chan2':'蝉','chan3':'产','chan4':'颤',
    'chen1':'趁','chen2':'沉','chen4':'称',
    'chang1':'昌','chang2':'长','chang3':'场','chang4':'唱',
    'cheng1':'称','cheng2':'城','cheng3':'逞',
    'chong1':'充','chong2':'虫','chong3':'宠','chong4':'冲',
    'chuan1':'穿','chuan2':'船','chuan3':'喘','chuan4':'串',
    'chuang1':'闯','chuang2':'床','chuang4':'创',
    'sha1':'沙','sha2':'傻','sha3':'傻','sha4':'厦',
    'she1':'蛇','she2':'社','she3':'舍','she4':'社',
    'shi1':'师','shi2':'十','shi3':'使','shi4':'是',
    'shu1':'书','shu2':'熟','shu3':'鼠','shu4':'树',
    'shua1':'刷','shua3':'耍',
    'shuo1':'说','shuo4':'硕',
    'shui1':'水','shui2':'睡','shui4':'睡',
    'shun4':'顺',
    'shai1':'晒','shai4':'晒',
    'shao1':'烧','shao2':'勺','shao3':'少','shao4':'哨',
    'shou1':'收','shou2':'手','shou3':'手','shou4':'售',
    'shan1':'山','shan2':'善','shan3':'闪','shan4':'善',
    'shen1':'深','shen2':'什','shen3':'神','shen4':'渗',
    'shang1':'商','shang4':'上',
    'sheng1':'生','sheng2':'省','sheng3':'省','sheng4':'胜',
    'shuan4':'涮',
    'shuai1':'摔','shuai3':'甩','shuai4':'帅',
    'shuang1':'霜','shuang2':'双','shuang3':'爽',
    're1':'热','re2':'惹','re4':'热',
    'ri4':'日',
    'ru1':'如','ru2':'入','ru3':'乳','ru4':'入',
    'ruo1':'弱','ruo2':'若','ruo4':'弱',
    'rui1':'锐','rui2':'蕊','rui4':'锐',
    'run4':'润',
    'rao1':'扰','rao2':'绕','rao4':'绕',
    'rou1':'揉','rou2':'肉','rou4':'肉',
    'ran1':'燃','ran2':'然','ran3':'染','ran4':'染',
    'ren1':'任','ren2':'人','ren3':'忍','ren4':'任',
    'rang1':'嚷','rang2':'让','rang4':'让',
    'reng1':'扔','reng2':'仍',
    'rong1':'荣','rong2':'绒','rong4':'绒',
    'ruan3':'软',
    'za1':'杂','za2':'砸','za3':'咱','za4':'砸',
    'ze1':'则','ze2':'则','ze4':'责',
    'zi1':'字','zi2':'字','zi3':'子','zi4':'字',
    'zu1':'租','zu2':'族','zu3':'阻','zu4':'足',
    'zuo1':'左','zuo2':'作','zuo3':'左','zuo4':'坐',
    'zui1':'最','zui3':'嘴','zui4':'最',
    'zun1':'尊','zun2':'遵',
    'zai1':'载','zai2':'在','zai4':'在',
    'zao1':'遭','zao2':'枣','zao3':'早','zao4':'造',
    'zou1':'走','zou2':'奏','zou3':'走','zou4':'奏',
    'zan1':'赞','zan2':'咱','zan3':'攒','zan4':'暂',
    'zen3':'怎',
    'zang1':'脏','zang2':'葬',
    'zeng1':'增','zeng4':'赠',
    'zong1':'总','zong2':'纵','zong3':'总','zong4':'纵',
    'ca1':'擦','ca2':'擦',
    'ce1':'测','ce2':'策','ce4':'测',
    'ci1':'刺','ci2':'词','ci3':'此','ci4':'刺',
    'cu1':'粗','cu2':'促','cu4':'促',
    'cuo1':'搓','cuo2':'错','cuo4':'错',
    'cui1':'催','cui2':'翠','cui4':'翠',
    'cun1':'村','cun2':'存','cun4':'寸',
    'cai1':'猜','cai2':'才','cai3':'采','cai4':'菜',
    'cao1':'操','cao2':'槽','cao3':'草',
    'cou4':'凑',
    'can1':'餐','can2':'残','can3':'惨','can4':'灿',
    'cang1':'仓','cang2':'藏',
    'ceng2':'层','ceng4':'蹭',
    'cong1':'从','cong2':'葱','cong3':'丛','cong4':'从',
    'cuan1':'蹿',
    'sa1':'撒','sa2':'洒','sa3':'洒',
    'se1':'色','se4':'色',
    'si1':'丝','si2':'死','si3':'死','si4':'四',
    'su1':'酥','su2':'俗','su4':'速',
    'suo1':'缩','suo3':'所','suo4':'索',
    'sui1':'虽','sui2':'随','sui4':'岁',
    'sun1':'孙','sun3':'笋',
    'sai1':'腮','sai4':'赛',
    'sao1':'骚','sao3':'嫂','sao4':'扫',
    'sou1':'搜','sou2':'艘','sou3':'叟','sou4':'嗽',
    'san1':'三','san3':'伞','san4':'散',
    'sen1':'森',
    'sang1':'桑','sang3':'嗓','sang4':'丧',
    'song1':'松','song2':'颂','song3':'耸','song4':'送',
    'suan1':'酸','suan4':'算',
  };

  const TONE_MAP = {
    '\u0101':'a1','\u00e1':'a2','\u01ce':'a3','\u00e0':'a4',
    '\u014d':'o1','\u00f3':'o2','\u01d2':'o3','\u00f2':'o4',
    '\u0113':'e1','\u00e9':'e2','\u011b':'e3','\u00e8':'e4',
    '\u012b':'i1','\u00ed':'i2','\u01d0':'i3','\u00ec':'i4',
    '\u016b':'u1','\u00fa':'u2','\u01d4':'u3','\u00f9':'u4',
    '\u01d6':'v1','\u01d8':'v2','\u01da':'v3','\u01dc':'v4',
    '\u00fc':'v'
  };

  function py2num(py) {
    let base = py.toLowerCase().trim();
    let tone = '';
    for (const [ch, repl] of Object.entries(TONE_MAP)) {
      if (base.includes(ch)) {
        base = base.replace(ch, repl.slice(0,-1));
        tone = repl.slice(-1);
        break;
      }
    }
    base = base.replace(/\u00fc/g, 'v');
    if (tone) return base + tone;
    const m = base.match(/^([a-z]+)([1-5])$/);
    return m ? m[1]+m[2] : base;
  }

  function getZhVoice() {
    if (!window.speechSynthesis) return null;
    const vs = window.speechSynthesis.getVoices();
    return vs.find(v =>
      (v.lang && (v.lang==='zh-CN'||v.lang==='zh-TW'||v.lang.startsWith('zh'))) ||
      (v.name && v.name.toLowerCase().includes('chinese'))
    ) || null;
  }

  let _activeAudio = null;

  function playUrl(url, onFail) {
    if (_activeAudio) { try{_activeAudio.pause();}catch(e){} _activeAudio=null; }
    const a = new Audio();
    _activeAudio = a;
    let done = false;
    const fail = () => { if(!done){done=true; if(onFail)onFail();} };
    const t = setTimeout(() => { if(a.readyState<2) fail(); }, 4000);
    a.onerror = () => { clearTimeout(t); fail(); };
    a.onended = () => { done=true; clearTimeout(t); };
    a.oncanplay = () => clearTimeout(t);
    a.src = url;
    a.load();
    a.play().then(()=>clearTimeout(t)).catch(()=>{clearTimeout(t);fail();});
  }

  function speakText(txt) {
    if (!txt) return;
    txt = txt.trim();
    const hasChinese = /[\u4e00-\u9fa5]/.test(txt);

    if (hasChinese) {
      // Chữ Hán: Youdao TTS trực tiếp
      playUrl('https://dict.youdao.com/dictvoice?audio='+encodeURIComponent(txt)+'&le=zh', () => {
        const v = getZhVoice();
        if (!v) return;
        const u = new SpeechSynthesisUtterance(txt);
        u.voice=v; u.lang='zh-CN'; u.rate=0.85;
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(u);
      });
      return;
    }

    // Pinyin: chuyển sang chữ Hán tương ứng
    const numbered = py2num(txt);
    const hanzi = P2H[numbered] || P2H[numbered.replace(/\d/,'')] || null;

    if (hanzi) {
      // Ưu tiên 1: Web Speech API với chữ Hán zh-CN (đọc đúng âm Mandarin)
      const v = getZhVoice();
      if (v) {
        const u = new SpeechSynthesisUtterance(hanzi);
        u.voice=v; u.lang='zh-CN'; u.rate=0.75;
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(u);
        return;
      }
      // Ưu tiên 2: Youdao với chữ Hán
      playUrl('https://dict.youdao.com/dictvoice?audio='+encodeURIComponent(hanzi)+'&le=zh', () => {
        // Ưu tiên 3: writtenchinese.com
        playUrl('https://dictionary.writtenchinese.com/sounds/'+encodeURIComponent(numbered)+'.mp3', null);
      });
    } else {
      // Không có map: thử writtenchinese.com
      playUrl('https://dictionary.writtenchinese.com/sounds/'+encodeURIComponent(numbered)+'.mp3', null);
    }
  }

  // Lắng nghe postMessage từ các iframe con
  window.addEventListener('message', function(e) {
    if (e.data && e.data.type === 'CHINESE_TTS') {
      speakText(e.data.text);
    }
  });

  window.chineseTTSParent = speakText;

  // Pre-load danh sách giọng nói
  if (window.speechSynthesis) {
    window.speechSynthesis.getVoices();
    window.speechSynthesis.addEventListener('voiceschanged', ()=>window.speechSynthesis.getVoices());
  }
})();
</script>
"""

# ─── TTS JS cho iframe (postMessage → parent) ────────────────────────────────
# iframe Streamlit bị sandbox → không dùng được Web Speech API trực tiếp
# → gửi postMessage lên parent window để phát âm
_TTS_JS_CORE = """
<script>
(function(){
  window.chineseTTS = function(txt) {
    if (!txt) return;
    window.parent.postMessage({type:'CHINESE_TTS', text: String(txt).trim()}, '*');
  };
})();
</script>
"""


def inject_tts_to_parent():
    """Inject TTS listener vào parent page (không bị sandbox).
    Gọi HÀM NÀY một lần duy nhất ở đầu mỗi trang."""
    st.markdown(_TTS_PARENT_JS, unsafe_allow_html=True)



def render_play_button(text, label, key=None, height=45, type="secondary"):
    inject_tts_to_parent()
    safe_text = json.dumps(text, ensure_ascii=False)
    bg      = "#2563eb" if type == "primary" else "#ffffff"
    color   = "#ffffff" if type == "primary" else "#31333F"
    border  = "#2563eb" if type == "primary" else "#e2e8f0"
    bg_hov  = "#1d4ed8" if type == "primary" else "#eff6ff"
    brd_hov = "#1d4ed8" if type == "primary" else "#2563eb"
    clr_hov = "#ffffff" if type == "primary" else "#2563eb"

    components.html(
        f"""
        {_TTS_JS_CORE}
        <style>
        body {{ margin:0; padding:0; background:transparent; overflow:hidden; }}
        .play-btn {{
            display:inline-flex; align-items:center; justify-content:center;
            width:100%; height:38px;
            background-color:{bg}; color:{color};
            border:1px solid {border}; border-radius:8px;
            font-size:0.88rem; font-weight:500; cursor:pointer;
            transition:all 0.2s ease;
            box-shadow:0 1px 2px rgba(0,0,0,0.05);
            font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
            box-sizing:border-box; user-select:none;
        }}
        .play-btn:hover {{
            background-color:{bg_hov}; border-color:{brd_hov}; color:{clr_hov};
        }}
        .play-btn:active {{ transform:scale(0.98); }}
        </style>
        <button class="play-btn" onclick="handlePlay()">{label}</button>
        <script>
        function handlePlay() {{
            const txt = {safe_text};
            if (window.chineseTTS) {{
                window.chineseTTS(txt);
            }}
        }}
        </script>
        """,
        height=height,
    )

def render_pronunciation_card(item, key_prefix):
    st.markdown(f"### {item['chu']}")
    st.write(item["hdsd"])
    st.write(f"Ví dụ: **{item['vd_han']}** — *{item['vd_py']}*.")
    render_play_button(item["nghe"], "🔊 Nghe ví dụ", key=f"{key_prefix}_{item['chu']}")

def render_lesson_intro(title, objective=None):
    st.markdown(
        f"""
        <style>
        /* ===== GLOBAL MOBILE FIXES ===== */
        .lesson-title {{
            white-space: normal;
            word-break: break-word;
            font-size: calc(1.1rem + 0.6vw);
            font-weight: 800;
            margin-top: 0;
            margin-bottom: 16px;
            color: #0f172a;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 10px;
            line-height: 1.3;
        }}
        /* Tabs: allow horizontal scroll on mobile instead of clipping */
        [data-testid="stTabs"] [role="tablist"] {{
            overflow-x: auto;
            flex-wrap: nowrap;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }}
        [data-testid="stTabs"] [role="tablist"]::-webkit-scrollbar {{ display: none; }}
        [data-testid="stTabs"] button[role="tab"] {{
            white-space: nowrap;
            flex-shrink: 0;
            font-size: 0.82rem;
            padding: 8px 12px;
        }}
        /* Radio buttons: bigger tap targets on mobile */
        @media (max-width: 640px) {{
            .lesson-title {{
                font-size: 1.15rem;
            }}
            [data-testid="stRadio"] label {{
                font-size: 0.9rem;
                padding: 6px 0;
            }}
            /* Columns on mobile: stack vertically */
            [data-testid="column"] {{
                min-width: 100% !important;
            }}
            /* Buttons full width */
            [data-testid="stButton"] > button {{
                width: 100%;
                font-size: 0.9rem;
            }}
            /* Cards: reduce padding */
            .adv-card, .nasal-card {{
                padding: 12px;
            }}
        }}
        </style>
        <h1 class="lesson-title">{title}</h1>
        {f'<p style="color:#475569;font-size:0.95rem;margin-top:-8px;margin-bottom:16px;">{objective}</p>' if objective else ''}
        """,
        unsafe_allow_html=True
    )

def shuffled_options(options, seed_text):
    opts = options[:]
    rnd = random.Random(seed_text)
    rnd.shuffle(opts)
    return opts

def render_quiz_section(questions, key_prefix, title, caption, save_func):
    with st.expander(title, expanded=False):
        st.caption(caption)
        score = 0
        for idx, item in enumerate(questions):
            raw_choices = item["choices"]
            choices = shuffled_options(raw_choices, f"{key_prefix}-{idx}")
            
            # Đảm bảo câu đầu tiên không phải đáp án đúng để học viên phải chọn
            if choices[0] == item["answer"] and len(choices) > 1:
                choices[0], choices[1] = choices[1], choices[0]
                
            key = f"{key_prefix}_q_{idx}"
            selected = st.radio(
                f"Câu {idx + 1}: {item['q']}?",
                choices,
                index=0,
                key=key,
            )
            if selected == item["answer"]:
                score += 1
        
        if st.button(f"Chấm điểm {title}", key=f"btn_{key_prefix}"):
            total = len(questions)
            st.session_state.scores[key_prefix] = (score, total)
            save_func()
            st.success(f"Bạn đúng {score}/{total} câu.")
            return score, total
    return None



