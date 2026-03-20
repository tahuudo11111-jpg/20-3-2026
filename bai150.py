using System;
using System.Linq;
using System.Windows.Forms;

namespace TongSoLe
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int OddSum(int[] a, int n)
        {
            if (n == 0) return 0;
            if (a[n - 1] % 2 != 0)
                return a[n - 1] + OddSum(a, n - 1);
            else
                return OddSum(a, n - 1);
        }

        private void btnTinh_Click(object sender, EventArgs e)
        {
            try
            {
                int[] arr = txtNhap.Text
                    .Split(' ')
                    .Select(int.Parse)
                    .ToArray();

                int tong = OddSum(arr, arr.Length);

                lblKetQua.Text = "Tổng số lẻ: " + tong;
            }
            catch
            {
                lblKetQua.Text = "Dữ liệu không hợp lệ!";
            }
        }
    }
}
