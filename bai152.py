using System;
using System.Linq;
using System.Windows.Forms;

namespace KiemTraMangDoiXung
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        bool isSym(int[] a, int left, int right)
        {
            if (left >= right) return true;
            if (a[left] != a[right]) return false;
            return isSym(a, left + 1, right - 1);
        }

        private void btnKiemTra_Click(object sender, EventArgs e)
        {
            try
            {
                int[] arr = txtNhap.Text
                    .Split(' ')
                    .Select(int.Parse)
                    .ToArray();

                bool kq = isSym(arr, 0, arr.Length - 1);

                if (kq)
                    lblKetQua.Text = "Mảng đối xứng ✅";
                else
                    lblKetQua.Text = "Mảng không đối xứng ❌";
            }
            catch
            {
                lblKetQua.Text = "Dữ liệu không hợp lệ!";
            }
        }
    }
}
