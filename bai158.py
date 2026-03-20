using System;
using System.Windows.Forms;

namespace GCD_DeQuy
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int GCD(int a, int b)
        {
            if (a == 0) return Math.Abs(b);
            return GCD(b % a, a);
        }

        private void btnTinh_Click(object sender, EventArgs e)
        {
            try
            {
                int a = int.Parse(txtA.Text);
                int b = int.Parse(txtB.Text);

                if (a == 0 && b == 0)
                {
                    lblKetQua.Text = "GCD(0,0) không xác định!";
                    return;
                }

                int kq = GCD(Math.Abs(a), Math.Abs(b));

                lblKetQua.Text = $"GCD({a}, {b}) = {kq}";
            }
            catch
            {
                lblKetQua.Text = "Dữ liệu không hợp lệ!";
            }
        }
    }
}
