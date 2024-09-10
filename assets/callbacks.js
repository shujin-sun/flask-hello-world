window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        newEffect: (n_clicks, originChildren, gongdeData) => {
            // 控制出金概率
            let threshold = 0.05
            // 出金模拟随机数
            let randomNum = Math.random()
            let newChildren = [
                ...originChildren,
                {
                    namespace: 'feffery_utils_components',
                    type: 'FefferyMotion',
                    props: {
                        children: randomNum <= threshold ? "功德无量" : "功德+1",
                        key: String(n_clicks),
                        destroyWhenAnimated: true,
                        initial: {
                            left: `${Math.random() * 100}%`,
                            top: '4em'
                        },
                        animate: {
                            top: 'calc(-75%)',
                            opacity: 0
                        },
                        transition: {
                            duration: randomNum <= threshold ? 3 : 1,
                            ease: 'linear',
                            repeat: 0
                        },
                        style: {
                            position: 'absolute',
                            color: 'white',
                            userSelect: 'none',
                            whiteSpace: 'pre',
                            writingMode: 'vertical-lr',
                            ...(
                                randomNum <= threshold ?
                                    {
                                        fontWeight: 'bold',
                                        fontSize: 28,
                                        color: '#ffec3d',
                                        fontFamily: 'KaiTi'
                                    } :
                                    {}
                            )
                        }
                    }
                }
            ];

            let newAudio = randomNum <= threshold ?
                {
                    namespace: 'dash_html_components',
                    type: 'Audio',
                    props: {
                        src: 'assets/金色传说音效.mp3',
                        autoPlay: true,
                        key: String(n_clicks)
                    }
                } :
                {
                    namespace: 'dash_html_components',
                    type: 'Audio',
                    props: {
                        src: 'assets/木鱼音效.mp3',
                        autoPlay: true,
                        key: String(n_clicks)
                    }
                }

            return [
                newChildren,
                randomNum <= threshold ? newAudio : window.dash_clientside.no_update,
                randomNum <= threshold ? window.dash_clientside.no_update : newAudio,
                {
                    gongde: gongdeData.gongde + 1,
                    gold: randomNum <= threshold ? gongdeData.gold + 1 : gongdeData.gold
                }
            ];
        }
    }
});