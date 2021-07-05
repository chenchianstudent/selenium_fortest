/**
 * 通過Selenuim啟動chrome瀏覽器
 * @author Baopz
 * @date 2018/05/24
 */
public class SeleniumApplication {
    private static final String base = "https://www.baidu.com";

    public static void main(String[] args) {
        //設定驅動所在位置
        System.setProperty("webdriver.chrome.driver","C:\\Users\\Baopz\\Desktop\\dcm\\2.37\\chromedriver.exe");
        WebDriver driver = new ChromeDriver(initChromeOpts());
        driver.get(base);
        //做一些事
        try {
            TimeUnit.SECONDS.sleep(5);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        //關閉瀏覽器
        driver.quit();
    }

    /**
     * 設定瀏覽器所需引數
     * @return
     */
    private static ChromeOptions initChromeOpts() {
        ChromeOptions chromeOptions = new ChromeOptions();
        //這裡可以不設定瀏覽器所在位置，這樣系統會尋找所需瀏覽器，如果沒有找到，拋錯
        chromeOptions.setBinary("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe");

        HashMap<String, Object> chromePrefs = new HashMap<String, Object>();
        //禁止彈窗
        chromePrefs.put("profile.default_content_settings.popups", 0);
        //下載地址
        chromePrefs.put("download.default_directory", "C://xx//");
        //禁止圖片載入
        chromePrefs.put("profile.managed_default_content_settings.images", 2);
        //userAgent=ie11
        String userAgentIE11="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36";
        chromePrefs.put("profile.general_useragent_override", userAgentIE11);
        
        HashMap<String, Object> mobileEmulation = new HashMap<String, Object>();
        //用iPhone X 螢幕啟動
        mobileEmulation.put("deviceName","iPhone X");

        chromeOptions.setExperimentalOption("prefs",chromePrefs);
        chromeOptions.setExperimentalOption("mobileEmulation",mobileEmulation);
        /***********************************以下設定啟動引數******************************************/
        //消除安全校驗
        chromeOptions.addArguments("--allow-running-insecure-content");
        //啟動最大化，防止失去焦點
        chromeOptions.addArguments("--start-maximized");
        //關閉gpu圖片渲染
        chromeOptions.addArguments("--disable-gpu");
        return chromeOptions;
    }
}