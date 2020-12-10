#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: BFSKtx
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time
from gnuradio import qtgui

class BFSKtx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BFSKtx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BFSKtx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "BFSKtx")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.bit_rate = bit_rate = 8
        self.sensitivity = sensitivity = 2*3.14*100000
        self.lowfreq = lowfreq = 50e3
        self.frequency_spread = frequency_spread = 50e3
        self.eye_offset = eye_offset = 1800e-6
        self.carrier_freq = carrier_freq = 2.49e9
        self.Repeat = Repeat = int(samp_rate/bit_rate)
        self.RF_gain = RF_gain = 60
        self.PacketSize = PacketSize = 8

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.01)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            int(2*Repeat), #size
            samp_rate, #samp_rate
            "", #name
            8 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(.1)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(False)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(8):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            50e3, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.01)
        self.qtgui_freq_sink_x_1.set_y_axis(-200, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(carrier_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(30, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(40, 0)
        self.osmosdr_sink_0.set_antenna('TX1', 0)
        self.osmosdr_sink_0.set_bandwidth(300e3, 0)
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                2e3,
                10e3,
                firdes.WIN_HAMMING,
                6.76))
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, sensitivity, 1)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(PacketSize)
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_char*1, Repeat)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(2*3.14*frequency_spread/sensitivity)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, int(eye_offset*samp_rate))
        self.blocks_delay_0_0_0_0_0_0_0_0_0_0_0 = blocks.delay(gr.sizeof_float*1, 7*Repeat+int(eye_offset*samp_rate))
        self.blocks_delay_0_0_0_0_0_0_0_0_0_0 = blocks.delay(gr.sizeof_float*1, 6*Repeat+int(eye_offset*samp_rate))
        self.blocks_delay_0_0_0_0_0 = blocks.delay(gr.sizeof_float*1, 3*Repeat+int(eye_offset*samp_rate))
        self.blocks_delay_0_0_0_0 = blocks.delay(gr.sizeof_float*1, 2*Repeat+int(eye_offset*samp_rate))
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_float*1, 4*Repeat+int(eye_offset*samp_rate))
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 5*Repeat+int(eye_offset*samp_rate))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Repeat+int(eye_offset*samp_rate))
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(2*3.14*lowfreq/sensitivity)
        self.analog_const_source_x_0 = analog.sig_source_b(0, analog.GR_CONST_WAVE, 0, 0, 110)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0_0_0, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 5))
        self.connect((self.blocks_delay_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 4))
        self.connect((self.blocks_delay_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 2))
        self.connect((self.blocks_delay_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 3))
        self.connect((self.blocks_delay_0_0_0_0_0_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 6))
        self.connect((self.blocks_delay_0_0_0_0_0_0_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 7))
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_delay_0_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_delay_0_0_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_delay_0_0_0_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_delay_0_0_0_0_0_0_0_0_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_delay_0_0_0_0_0_0_0_0_0_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "BFSKtx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Repeat(int(self.samp_rate/self.bit_rate))
        self.blocks_delay_0.set_dly(self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0.set_dly(5*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0.set_dly(4*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0.set_dly(2*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0_0.set_dly(3*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0_0_0_0_0_0_0.set_dly(6*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0_0_0_0_0_0_0_0.set_dly(7*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_1.set_dly(int(self.eye_offset*self.samp_rate))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 2e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_bit_rate(self):
        return self.bit_rate

    def set_bit_rate(self, bit_rate):
        self.bit_rate = bit_rate
        self.set_Repeat(int(self.samp_rate/self.bit_rate))

    def get_sensitivity(self):
        return self.sensitivity

    def set_sensitivity(self, sensitivity):
        self.sensitivity = sensitivity
        self.blocks_add_const_vxx_0.set_k(2*3.14*self.lowfreq/self.sensitivity)
        self.blocks_multiply_const_vxx_0.set_k(2*3.14*self.frequency_spread/self.sensitivity)

    def get_lowfreq(self):
        return self.lowfreq

    def set_lowfreq(self, lowfreq):
        self.lowfreq = lowfreq
        self.blocks_add_const_vxx_0.set_k(2*3.14*self.lowfreq/self.sensitivity)

    def get_frequency_spread(self):
        return self.frequency_spread

    def set_frequency_spread(self, frequency_spread):
        self.frequency_spread = frequency_spread
        self.blocks_multiply_const_vxx_0.set_k(2*3.14*self.frequency_spread/self.sensitivity)

    def get_eye_offset(self):
        return self.eye_offset

    def set_eye_offset(self, eye_offset):
        self.eye_offset = eye_offset
        self.blocks_delay_0.set_dly(self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0.set_dly(5*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0.set_dly(4*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0.set_dly(2*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0_0.set_dly(3*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0_0_0_0_0_0_0.set_dly(6*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0_0_0_0_0_0_0_0.set_dly(7*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_1.set_dly(int(self.eye_offset*self.samp_rate))

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.osmosdr_sink_0.set_center_freq(self.carrier_freq, 0)

    def get_Repeat(self):
        return self.Repeat

    def set_Repeat(self, Repeat):
        self.Repeat = Repeat
        self.blocks_delay_0.set_dly(self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0.set_dly(5*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0.set_dly(4*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0.set_dly(2*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0_0.set_dly(3*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0_0_0_0_0_0_0.set_dly(6*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_delay_0_0_0_0_0_0_0_0_0_0_0.set_dly(7*self.Repeat+int(self.eye_offset*self.samp_rate))
        self.blocks_repeat_0.set_interpolation(self.Repeat)

    def get_RF_gain(self):
        return self.RF_gain

    def set_RF_gain(self, RF_gain):
        self.RF_gain = RF_gain

    def get_PacketSize(self):
        return self.PacketSize

    def set_PacketSize(self, PacketSize):
        self.PacketSize = PacketSize



def main(top_block_cls=BFSKtx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
