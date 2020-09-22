#!/usr/bin/python3
import sys
from __save__ import *

########################################################
def runAllData(MyCodeTitle,MyCodeString,MyCodeName):
    global package1,package2,extension,count

    count = count + 1    

    (data1,data2,data3) = makeCode(MyCodeTitle,MyCodeString,MyCodeName+str(count))

    package1  = package1  + data1
    package2  = package2  + data2
    extension = extension + data3
########################################################


package1   = ""
package2   = ""
extension  = ""
count      = 0
MyCodeName = sys.argv[2]


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode C# ( 範例 )"
# MyCodeString = '''
# ###  C# 範例程式 ####
# ### file: mainCode_C_Sharp ###
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)

# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode C# ( 範例 )"
# MyCodeString = '''
# ###  C# 範例程式 ####
# ### file: mainCode_C_Sharp ###
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)
# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode C# ( 範例 )"
# MyCodeString = '''
# ###  C# 範例程式 ####
# ### file: mainCode_C_Sharp ###
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)

# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode C# ( 範例 )"
# MyCodeString = '''
# ###  C# 範例程式 ####
# ### file: mainCode_C_Sharp ###
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)

# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode C# ( 範例 )"
# MyCodeString = '''
# ###  C# 範例程式 ####
# ### file: mainCode_C_Sharp ###
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode C# (Global變數)"
MyCodeString = '''
###  C# Global變數 ####
### file: mainCode_C_Sharp ###

public class Global
{
    public static int    test1 = 0;
    public static string test2 = "123";
}
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode C# ( Telnet 遠端下指令 )"
MyCodeString = '''
###  C#  Telnet 遠端下指令 ####
### file: mainCode_C_Sharp ###
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net.Sockets;
using System.Threading;

namespace downSmartIT
{
    class TelnetConnection
    {

        TcpClient tcpSocket;
        public TelnetConnection(String Hostname, int Port){ tcpSocket = new TcpClient(Hostname, Port); }

        public void WriteLine(string cmd){ Write(cmd + "\r\n"); }

        public void Write(string cmd)
        {
            if (!tcpSocket.Connected) return;
            byte[] buf = System.Text.ASCIIEncoding.ASCII.GetBytes(cmd.Replace("\0xFF", "\0xFF\0xFF"));
            tcpSocket.GetStream().Write(buf, 0, buf.Length);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                var url = args[0];
                TelnetConnection tc = new TelnetConnection(url, 12345);
                Thread.Sleep(1000);
                tc.WriteLine("!aabbccdd");
                Thread.Sleep(1000);
                tc.WriteLine("11223344");
            }
            catch (Exception e)
            {
                Console.WriteLine("使用範例: test.exe 192.168.0.10");
            }
        }
    }
}
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode C# ( 讀取檔案，比對字串 )"
MyCodeString = '''
###  C# 讀取檔案，比對字串 ####
### file: mainCode_C_Sharp ###
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

System.IO.StreamReader file = new System.IO.StreamReader(@"test.ini");
while ((line = file.ReadLine()) != null)
{
    if (line.Contains("Version=") == true)
    {
        Console.WriteLine(line);
    }
}
file.Close();

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode C# ( POST 傳送資料 to web )"
MyCodeString = '''
###  C# POST DATA TO WEB ####
### file: mainCode_C_Sharp ###
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Net;

namespace post
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public class myData
        {
            public static string name = "Rose";
        }

        private void post_data()
        {

            string url = "http://127.0.0.1/test/aa.php";

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.Method = "POST";

            // POST 的資料
            string formContent = "name=" + myData.name + "&age=18";

            byte[] byteArray = Encoding.UTF8.GetBytes(formContent);
            request.ContentType = "application/x-www-form-urlencoded";
            request.ContentLength = byteArray.Length;

            Stream dataStream = request.GetRequestStream();
            dataStream.Write(byteArray, 0, byteArray.Length);
            dataStream.Close();

            WebResponse response = request.GetResponse();
            string myStatus = ((HttpWebResponse)response).StatusDescription;  // 取得狀態

            using (dataStream = response.GetResponseStream())
            {
                StreamReader reader = new StreamReader(dataStream);
                string responseFromServer = reader.ReadToEnd();
                string responseText = responseFromServer;  // 輸出回傳內容
            }
            response.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            post_data();
        }
    }
}
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode C# ( GET Web DATA )"
MyCodeString = '''
###  C# GET WEB DATA ####
### file: mainCode_C_Sharp ###

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net;
using System.IO;

namespace test
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string url = "http://127.0.0.1/test.html";
            WebRequest request = WebRequest.Create(url);

            request.Method = "GET";

            using (var httpResponse = (HttpWebResponse)request.GetResponse())
            using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
            {
                var webData = streamReader.ReadToEnd();
                string[] stringSeparators = new string[] { "\n" };
                string[] arr = webData.Split(stringSeparators, StringSplitOptions.None);

                foreach (var dat in arr)
                {
                    listBox1.Items.Add(dat);
                }
            }
        }
    }
}

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)






### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode C# ( Download progressBar )"
MyCodeString = '''
###  C# Download progressBar ####
### file: mainCode_C_Sharp ###

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net;

namespace test2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public class Global
        {
            public static List<String> uurl = new List<String>();
            public static List<String> ff = new List<String>();
        }
        
        private void button1_Click(object sender, EventArgs e)
        {
            Global.uurl.Add(@"http://ftp.isu.edu.tw/pub/MySQL/Downloads/MySQL-4.1/mysql-4.1.21-win-src.zip");
            Global.uurl.Add(@"http://ftp.isu.edu.tw/pub/MySQL/Downloads/MySQL-4.1/MySQL-4.1.22-0.glibc23.src.rpm");
            Global.uurl.Add(@"http://ftp.isu.edu.tw/pub/MySQL/Downloads/MySQL-4.1/MySQL-bench-4.1.22-0.glibc23.x86_64.rpm");
            Global.uurl.Add(@"http://ftp.isu.edu.tw/pub/MySQL/Downloads/MySQL-4.1/MySQL-client-standard-4.1.21-0.rhel4.ia64.rpm");

            using (WebClient client = new WebClient())
            {
                label1.Text = "下載必要檔案 , 剩餘" + Global.uurl.Count + "個未完成";

                if ( Global.uurl.Count > 0)
                {
                    string urlfile = Global.uurl[0];
                    string[] tmp = urlfile.Split('/');
                    string filename = tmp[tmp.Length - 1];

                    progressBar1.Value = 0;
                    client.DownloadProgressChanged += Client_DownloadProgressChanged;
                    client.DownloadFileCompleted += Client_DownloadFileCompleted;
                    client.DownloadFileAsync(new Uri( urlfile ) , @"C:\TEST\" + filename  );
                }
            }
        }

        private void Client_DownloadFileCompleted(object sender, AsyncCompletedEventArgs e)
        {
            using (WebClient client = new WebClient())
            {
                Global.uurl.RemoveAt(0);

                label1.Text = "下載必要檔案 , 剩餘" + Global.uurl.Count + "個未完成"  ;

                if (Global.uurl.Count > 0)
                {
                    string urlfile = Global.uurl[0];
                    string[] tmp = urlfile.Split('/');
                    string filename = tmp[tmp.Length - 1];

                    progressBar1.Value = 0;
                    client.DownloadProgressChanged += Client_DownloadProgressChanged;
                    client.DownloadFileCompleted += Client_DownloadFileCompleted;
                    client.DownloadFileAsync(new Uri(urlfile), @"C:\TEST\" + filename);
                }
                else
                {
                    label1.Text = "下載完成";
                }
            }
        }

        private void Client_DownloadProgressChanged(object sender, DownloadProgressChangedEventArgs e)
        {
            progressBar1.Maximum = (int)e.TotalBytesToReceive;
            progressBar1.Value = (int)e.BytesReceived;
            progressBar1.Update();
        }
    }
}
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode C# ( process 執行程式 )"
MyCodeString = '''
###  C# process 執行程式 ####
### file: mainCode_C_Sharp ###
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;
using System.Security;

using System.Net;
using System.Net.Sockets;
using System.Text.RegularExpressions;

// -- 一般執行 -------------------------------------------
Process myCommand = new Process();
myCommand.StartInfo.FileName = filename;
myCommand.Start();
this.Close();

// -- 切換身份執行 -------------------------------------------
ProcessStartInfo myProcess = new ProcessStartInfo(filename);

string usr = @"administrator";
string pwd = @"12345678";

SecureString passWord = new SecureString();
foreach (char c in pwd)
{
    passWord.AppendChar(c);
}

myProcess.UserName = usr;
myProcess.Password = passWord;

myProcess.WorkingDirectory = Environment.GetEnvironmentVariable("TEMP");
myProcess.UseShellExecute = false;
Process.Start(myProcess);
this.Close();

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode C# ( cmd compiler )"
MyCodeString = '''
###  C# cmd compiler ####
### file: mainCode_C_Sharp ###
C:\Windows\Microsoft.NET\Framework\v3.5\MSBuild.exe Source\\TVinstall.sln
c:\windows\Microsoft.NET\Framework\v3.5\bin\csc.exe /t:exe /out:MyApplication.exe MyApplication.cs
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
