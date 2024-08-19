'''我的主页'''
import streamlit as st
from PIL import Image



page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区','我的小问题','我的进度条','我的滑块开关','我的跳转','我的单选框','我的滑动条','我的勾选框'])

def page_1():
    '''我的兴趣推荐'''
    with open('ivorytower.mp3','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('小秘密.png')
    tab1,tab2,tab3,tab4=st.tabs(['动画推荐','游戏推荐','图书推荐','宠物推荐'])
    with tab1:
        st.image('龙族.jpg')
        st.write('动画推荐')            
        st.write('路明非原本是一个普通懵懂的高中生，一封来自卡塞尔学院的来信改变了他平淡的人生。')
        st.write('在热血与神秘的呼唤下，在爱与梦想的抉择下，他毅然选择了未知。')
        st.write('黑的直升机划过天际，陌生国度的大门向他缓缓开启，平凡的中国小孩走上不平凡的屠龙之路。')
        st.write('遥远的卡塞尔学院却处处透着神秘——奇怪的课程、搞笑的学长.疯狂的教师.骄傲的同学……路明非刚刚进入学校就遭遇了无数的怪事。')
        st.write('但是，随之而来的挑战也开始了，等级考试、言灵考验、地图搜索……龙的世界也终于在水下露出了神秘面纱。')
    with tab2:
        st.image('我的世界.jpg')
        st.write('游戏推荐')
        st.write('''《我的世界》（Minecraft）是一款由瑞典游戏开发者马库斯·泊松（Markus Persson）创造并由Mojang Studios（前身为Mojang AB）开发的沙盒式游戏。
                 游戏于2011年11月正式发布，从发布以来，它一直是游戏界的一颗明星，吸引了全球无数玩家的喜爱。 
                 在《我的世界》中，玩家可以进入一个由立方体组成的巨大世界。
                 这个世界几乎无限大，由各种不同的生物群落、地形、资源和环境组成。
                 玩家可以自由地探索、挖掘矿物、建造建筑、种植作物、捕猎生物、制作物品和与其他玩家互动。
                 游戏中有两种主要模式： 创造模式：玩家可以无限使用所有资源，并且拥有飞行能力。
                 这使得创造模式成为建筑者和艺术家喜欢的模式，他们可以尽情发挥创意，构建宏伟的建筑和场景。
                 生存模式：玩家需要管理自己的饥饿度、生命值和资源，并要面对敌对生物的攻击。
                 在生存模式下，玩家需要在探索与冒险中获取资源，建造庇护所，养活自己，并对抗敌对生物，同时保持自己的生存。 
                 游戏的核心是采集和合成。玩家可以通过在游戏中采集各种资源（如木材、石头、矿石、动植物等）来制作各种工具和物品。
                 使用这些工具和物品，玩家可以建造房屋、城堡、桥梁、农场等，创造自己的世界。
                 除了单人模式外，游戏还支持多人联机模式。
                 玩家可以通过局域网或互联网与其他玩家一起合作或竞争，共同建设世界或进行创意和生存挑战。''')
    with tab3:
        st.image('哈利波特.jpeg')
        st.write('图书推荐')
        st.write('1、《哈利波特》电影一共有八部。结局分上下两部。第一部《哈利波特与魔法石》、第二部《哈利波特与密室》、第三部《哈利波特与阿兹卡班的囚徒》、第四部《哈利波特与火焰杯》、第五部《哈利波特与凤凰社》、第六部《哈利波特与混血王子》、第七部《哈利波特与死亡圣器（上）》、第八部《哈利波特与死亡圣器（下）》。')
        st.write('2、《哈利波特》剧情简介：《哈利·波特》是英国作家J·K·罗琳于1997～2007年所著的魔幻文学系列小说，共7部。其中前六部以霍格沃茨魔法学校为主要舞台，描写的是主人公——年轻的巫师学生哈利·波特在霍格沃茨前后六年的学习生活和冒险故事；第七本描写的是哈利·波特在第二次魔法界大战中在外寻找魂器并消灭伏地魔的故事。')

    with tab4:
        st.image('银渐层.jpg')
        st.write('宠物推荐')
        st.write('''英短银渐层是由英国短毛猫（蓝灰色）与金吉拉猫繁育而出的英短品种，由于具备了金吉拉猫白色的毛色，又具备了英国短毛猫重要的特征，所以非常受大家的喜爱。
                 2/6
                 毛色：既然称之为银渐层，就是毛色是有渐变色的，既背毛的六分之以到八分之一为灰黑色，其他部分为白色，对于新手猫迷来说，简单一句话，银渐层的毛色，越浅越好，越白越好。
                 3/6
                 头版：1 耳距，既小猫两个耳朵之间的距离，要尽量的长这样的小猫未来头会比较大，会更加的可爱。2 眼睛：眼睛圆润而，初生银渐层的眼色要在4个月大左右时才会定型，一般在满月时期看到的都是蓝色眼睛，这不是小猫最后的眼睛眼色哦。银渐层的眼睛眼色分为几种，以价格高低依次为，蓝色，绿色，黄绿，黄。如果不确定小猫未来眼睛的眼色，看父母的眼睛眼色。
                 4/6
                 四肢：英国短毛猫为中大型猫品种，银渐层属于中型品种的猫咪，没有传统英短那么的大，但是依然需要挑选四肢较为强壮，行走奔跑有力的小猫。
                 5/6                        
                 性别：个人家养建议选择公猫弟弟，因为公猫绝育手术比较简便，且费用较低，早起进行绝育后未来一劳永逸，母猫妹妹体型也会同步小于未来的成年公猫，而且发情会有很大的叫声，母猫绝育需要进行开腹手术取出卵巢和子宫，各位猫迷挑选时一定要注意哦。当然如果想要生小猫咪的话，那必然是要优选妹妹了。可以选合适的公猫进行借配即可。
                 6/6
                 银色渐层猫：毛色标准 取脊背部分的毛，整根毛除了毛尖部分为黑色，其他部分应该都是白色，并且着色部分的长度与整根毛长度比例应为1:3--1:8。着色比例方面 如果，出现大于3分之一的 ，毛色失格，只能按银虎斑 算了，如果小于8分之一，也属于失格，是不被承认的。被毛及四肢出现明显纹路的，
                 说明是罕见的返祖现象，其他标准 其实毛色浅，眼色绿色 ，都是市场炒作。蓝绿 黄绿都是被认同的，只要不是纯黄色，随着年龄不同程度呈现黄绿、绿蓝绿色，比赛中都是被允许的。并有一圈黑色眼线；鼻色应该是樱桃红色，外围一圈黑色的鼻线；爪垫皮肤与毛均为黑色''')
    
   
    
    
    pass

def page_2():
    '''我的图片处理工具'''
    st.write(':sunglasses:图片换色小程序:sunglasses:')
    uploaded_file=st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        #file.size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4=st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,2,0,1))
    
def img_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
    

def page_3():
    '''我的智能词典'''
    st.write('智能词典')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list=f.read().split('\n')
        #print(words_list)
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    word=st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n] +=1
        else:
            times_dict[n]=1
        with open('check_out_times.txt','w',encoding='utf-8')as f:
            message=''
            for k,v in times_dict.items():
                message +=str(k) + '#'+ str(v) + '\n'
            message=message[:-1]
            f.write(message)
        st.write('查询次数:',times_dict[n])
        if word =='green':
            st.snow()
            st.balloons()
    pass

def page_4():
    '''我的留言区'''
    st.write('我的留言区')

    with open('leave_messages.txt','r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] =='阿短':
            with st .chat_message('🍀'):
                st.write(i[1],':',i[2])
        if i[1] =='编程猫':
            with st.chat_message('🍁'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是....',['阿短','编程猫'])
    new_message = st.text_input('想要说的话.......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8')as f:
            message=''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message=message[:-1]
            f.write(message)
    pass
def page_5():
    st.write('路明非的弟弟是谁')
    cb1 = st.checkbox('A.路明泽')
    cb2 = st.checkbox('B.路泽明')
    cb3 = st.checkbox('C.路非明')
    cb4 = st.checkbox('D.路明')
    b1 = st.button('第1题答案')
    if b1:
        if cb1 == True and cb2 == False and cb3 == False and cb4 == False:
            st.write('回答正确！')
        else:
            st.write('再想想')

    def page_6():
        roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')

# 如何创建组件？
# 创建组件之后如何调用组件实现效果？
# 两个参数的作用分别是？

# 应用：词典_单词记忆挑战
    words_lst = ['fruit：水果', 'apple：苹果', 'banana：香蕉', 'orange：橘子']

    words = st.progress(0, '准备开始单词记忆挑战！')
    for i in range(4, 0, -1):
        time.sleep(3)
        words.progress(i*25, words_lst[-i])
    time.sleep(3)
    words.progress(0, '开始猜词吧！')
    st.write('刚才出现的单词是？他们的意思是？')
def page_7():
    st.write("主要功能未开发完全")
    ex = st.toggle('开关')
    if ex:
        st.write('开启')
    else:
        st.write('关闭')

# 如何创建组件？
# 创建组件之后如何通过判断实现效果？

# 应用：图片_功能判断开关
    ch = st.toggle('反色滤镜')
    bw = st.toggle('黑白滤镜')
    co = st.toggle('增强对比度')

    message = ''
    if ch:
        message += '反色' + ','
    if bw:
        message += '黑白' + ','
    if co:
        message += '增强对比度'
    st.write('你将会得到一张', message, '的图片')
def page_8():
    st.link_button('百度首页', 'https://www.baidu.com/')

# 如何创建跳转按钮
# 普通的按钮需要编写if判断触发效果，跳转按钮需要吗？

# 应用：兴趣推广_分享链接指引
    st.write('----')
    st.write('你喜欢用什么')
    go = st.selectbox( ['我的贴吧', '我的bilibili'])
    if go == '贴吧':
        st.link_button('https://www.baidu.com/')
    elif go == 'bilibili':
        st.link_button('https://www.bilibili.com/')
def page_9():
    st.write("主要功能未开发完全")
#       '选择：',
 #       ['选项1', '选项2', '选项3'],
  #      captions=['这是第一个选项', '这是第二个选项', '这是第三个选项']
   # )

# 如何创建单选框？
# 单选框中的两个必填参数分别是？都有什么作用？
# captions参数的作用是？

# 应用：游戏_数据模拟器
    #st.write('----')
    level = st.radio(
        '选择游戏难度：',
        ['普通', '困难', '地狱'],
        captions=['怪物血量为100%,攻击力为100%', '怪物血量为200%,攻击力为150%', '怪物血量为300%,攻击力为200%']
        )
    hp = 100
    damage = 10
    if level == '困难':
        hp = 200
        damage = 15
    elif level == '地狱':
        hp = 300
        damage = 20
    st.write('怪物血量：', hp, '，怪物攻击力：', damage)
def page_10():
    st.write("主要功能未开发完全")
    number1 = st.slider('数据1：', 1, 100, 50)
    number2, number3 = st.slider('数据2和3：', 1, 10, (4, 6))
    st.write('数据1：', number1)
    st.write('数据2-3：', number2, '-', number3)

# 如何创建滑动条？
# 滑动条中可以有几个数据点？

# 应用：留言_显示范围控制
    st.write('----')
    msg_lst = ['留言1', '留言2', '留言3', '留言4', '留言5', '留言6', '留言7', '留言8']
    begin, end = st.slider('选择显示的留言信息：', 1, len(msg_lst), (1, len(msg_lst)))
    for i in range(begin-1, end):
        st.write(msg_lst[i])
def page_11():
    cb = st.checkbox('勾选选项')
    if cb:
        st.write('选项被勾选', cb)

# 如何创建勾选框？
# 勾选框更适合单选还是多选？
# 勾选框的返回值是选框中的字符串吗？不是的话，返回值是什么？

# 应用：宣传_互联网知识
    st.write('----')
    st.write('你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
    cb1 = st.checkbox('易于管理')
    cb2 = st.checkbox('效率高')
    cb3 = st.checkbox('网速快')
    cb4 = st.checkbox('安全性好')
    l = [cb1, cb2, cb3, cb4]
    if st.button('确认答案'):
        if True in l:
            st.write('其实都不对，答案是“历史问题，不得已而为之”')
        else:
            st.write('好厉害！确实都不对，真实答案是“历史问题，不得已而为之”，下面就让我来讲讲吧！')
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的小问题':
    page_5()
elif page == '我的进度条':
    page_6()
elif page == '我的滑块开关':
    page_7()
elif page == '我的跳转':
    page_8()
elif page == '我的单选框':
    page_9()
elif page == '我的滑动条':
    page_10()
elif page == '我的勾选框':
    page_11()
#st.write("<span style='font-size:20px; color:blue'>这是20px大小的蓝色的字</span>", unsafe_allow_html=True)