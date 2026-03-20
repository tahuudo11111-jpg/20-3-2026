using System;
using System.Windows.Forms;

namespace BitOperationGUI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int bitOff(int d, int n) => d & ~(1 << n);
        int bitOn(int d, int n) => d | (1 << n);
        int bitFlip(int d, int n) => d ^ (1 << n);
        int isBit(int d, int n) => (d >> n) & 1;

        string ToBinary(int x)
        {
            return Convert.ToString(x, 2).PadLeft(32, '0');
        }

        private void btnXuLy_Click(object sender, EventArgs e)
        {
            try
            {
                int d = int.Parse(txtSo.Text);
                int n = int.Parse(txtBit.Text);

                txtGoc.Text = $"{d} = {ToBinary(d)}";

                int on = bitOn(d, n);
                int off = bitOff(d, n);
                int flip = bitFlip(d, n);

                txtOn.Text = $"{on} = {ToBinary(on)}";
                txtOff.Text = $"{off} = {ToBinary(off)}";
                txtFlip.Text = $"{flip} = {ToBinary(flip)}";

                lblCheck.Text = $"Bit {n} = {isBit(d, n)}";
            }
            catch
            {
                MessageBox.Show("Dữ liệu không hợp lệ!");
            }
        }
    }
}
