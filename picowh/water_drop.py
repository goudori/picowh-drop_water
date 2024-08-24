import machine  # type: ignore
import utime  # type: ignore

sensor = machine.ADC(28)

# センサーの値を水滴の単位に変換するための係数
water_drop_coefficient = 0.1  # 例: 1単位のセンサーの値が0.1水滴に相当する

# センサーの値を水滴の単位を取得する
while True:
    value = sensor.read_u16()
    water_drops = value * water_drop_coefficient
    print(f"drop of water: {water_drops:.2f}")
    utime.sleep_ms(200)
