import re

rule = r"((http(s)?|ftp|tcp|mysql|sql|):\/\/)([\w-]+\.)+[\w-]+(/[-\w./?%&=]*)?"


def get_line(path, str):
    with open(path, "r", encoding="utf-8",errors='ignore') as f:
        count = 0
        for line in f.readlines():
            if str in line:
                return count
            count += 1


def get_result(path):
    context_list = []
    with open(path, "r", encoding="utf-8", errors='ignore') as f:
        source = f.read()
        result = re.finditer(rule, source)
    for res in result:
        url = res.group()
        dict = {}
        line = get_line(path, url)
        dict["line"] = line
        dict["context"] = url
        context_list.append(dict)

    return context_list


def get_url(path_list):
    match_list = []
    for path in path_list:
        match_result = {}
        res = get_result(path)
        if res:
            match_result["path"] = path
            match_result["value"] = res
            match_list.append(match_result)
    return match_list


if __name__ == '__main__':
    path = ['/Users/ios/Downloads/out/resources/com/github/mikephil/charting/data/LineData.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/data/PieDataSet.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/data/RadarData.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/data/Entry.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/exception/DrawingDataSetNotCreatedException.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/matrix/Vector3.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/interfaces/BarLineScatterCandleBubbleDataProvider.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/interfaces/ScatterDataProvider.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/interfaces/BubbleDataProvider.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/interfaces/ChartInterface.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/interfaces/LineDataProvider.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/interfaces/BarDataProvider.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/interfaces/CandleDataProvider.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/buffer/ScatterBuffer.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/buffer/LineBuffer.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/buffer/HorizontalBarBuffer.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/buffer/AbstractBuffer.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/buffer/CandleBodyBuffer.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/buffer/BarBuffer.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/buffer/CandleShadowBuffer.java', '/Users/ios/Downloads/out/resources/com/github/mikephil/charting/buffer/CircleBuffer.java', '/Users/ios/Downloads/out/resources/dao-master.ftl', '/Users/ios/Downloads/out/resources/androidsupportmultidexversion.txt', '/Users/ios/Downloads/out/sources/.DS_Store', '/Users/ios/Downloads/out/sources/com/p000qq/.DS_Store', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/.DS_Store', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/.DS_Store', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/splash/C0023b.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/.DS_Store', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/util/C0036c.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/util/C0034av.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/util/C0035bf.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/util/C0033aj.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p007t/C0024a.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p003b/C0005b.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p005s/C0021g.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p005s/C0020f.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p005s/p006a/C0014e.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p005s/p006a/C0016h.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p005s/p006a/C0017i.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p005s/p006a/C0013d.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p005s/p006a/C0015f.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p005s/C0012a.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p005s/C0022h.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p005s/C0019e.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p005s/C0018d.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/POFactoryImpl.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/intersitial2/fullscreen/C0006a.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/rewardvideo/View$OnClickListenerC0010k.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/rewardvideo/C0009i.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/rewardvideo/C0011m.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p008u/AbstractC0025a.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p008u/C0029p.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p008u/C0030q.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p008u/C0027l.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p008u/C0026j.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p008u/C0031r.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p008u/C0028m.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p008u/C0032s.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p004q/C0007e.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p002a/C0004h.java', '/Users/ios/Downloads/out/sources/com/p000qq/p001e/comm/plugin/p002a/C0003d.java', '/Users/ios/Downloads/out/sources/com/.DS_Store', '/Users/ios/Downloads/out/sources/com/syezon/wifi/R.java', '/Users/ios/Downloads/out/sources/com/syezon/.DS_Store', '/Users/ios/Downloads/out/sources/com/qihoo/.DS_Store', '/Users/ios/Downloads/out/sources/com/qihoo/util/RunnableC0000.java', '/Users/ios/Downloads/out/sources/com/qihoo/util/Configuration.java', '/Users/ios/Downloads/out/sources/com/qihoo/util/QHDialog.java', '/Users/ios/Downloads/out/sources/com/qihoo/util/C0002.java', '/Users/ios/Downloads/out/sources/com/qihoo/util/DialogInterface$OnClickListenerC0001.java', '/Users/ios/Downloads/out/sources/com/stub/StubApp.java']
    res = get_url(path)
    print(res)
