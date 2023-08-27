---
title: RT-Thread开源贡献入门级指南
tags:
  - github
  - rt-thread
categories:
  - 开源社区贡献
date: 2023-06-03 00:33:29

---

## RT-Thread简介

RT-Thread 是一款主要由中国开源社区主导开发的开源实时操作系统。据最新2021 RT-Thread开发者大会上官方公布的数据，其装机量已经超过14亿，开源企业用户已经有数万家，有超过100家国内外芯片厂家的支持，RT-Thread Studio工具拥有了超过15万用户。

> RT-Thread文档中心：[RT-Thread 简介](https://www.rt-thread.org/document/site/#/rt-thread-version/rt-thread-standard/README) 
>
> RT-Thread学习路线：[docs-online: RT-Thread在线文档中心 (gitee.com)](https://gitee.com/rtthread/docs-online#学习路线) 
>
> 仓库地址：[RT-Thread](https://gitee.com/rtthread/rt-thread)

### 将RT-Thread运行在开发板上

以stm3232u575-st-nucleo为例，请参考下列说明文档（其他开发板同理）

> NUCLEO-U575ZI-1开发板BSP说明：[rt-thread/README_zh.md at master · RT-Thread/rt-thread · GitHub](https://github.com/RT-Thread/rt-thread/blob/master/bsp/stm32/stm32u575-st-nucleo/README_zh.md) 

## RT-Thread开源贡献

### 文档或注释修改类

#### 失效链接

对gitee下RT-Thread/docs-online项目——RT-Thread在线文档中心里的链接进行查阅，寻找失效的链接或是访问速度比较慢的重定向链接进行修复。

**工作说明**

1. 修复了24个rt-thread-version/rt-thread-standard/packages-manual/micropython-docs/目录下的文档中访问速度比较慢的重定向链接，形如：`http://docs.micropython.org/en/latest/pyboard/library/`
2. 不修复将会导致文档跳转访问速度变慢

形成的第一个开源贡献成果如下：

> [【修改】 修复了24个rt-thread-version/rt-thread-standard/packages-manual/micropython-docs/目录下的文档中访问速度比较慢的重定向链接http://docs.micropython.org/en/latest/pyboard/library/ · Pull Request !490 · RT-Thread/docs-online - Gitee.com](https://gitee.com/rtthread/docs-online/pulls/490) 

### 安全修复类

#### 数据类型使用不当

> 问题描述：[[pin\][5.0.0] 修正pin框架数据类型使用不当 by ZosCat1 · Pull Request #6934 · RT-Thread/rt-thread (github.com)](https://github.com/RT-Thread/rt-thread/pull/6934) 
>
> 修改示例：[[HUST CSE\][bsp] fix mismatched function types in rt_pin_ops by hustlixiang21 · Pull Request #7161 · RT-Thread/rt-thread (github.com)](https://github.com/RT-Thread/rt-thread/pull/7161) 
>
> 同类修改示例：[[HUST CSE\][bsp]fix mismatched function types in rt_pin_ops for all drv_gpio.c by hustlixiang21 · Pull Request #7185 · RT-Thread/rt-thread (github.com)](https://github.com/RT-Thread/rt-thread/pull/7185) 

**工作说明**

1. pin的数据类型有些采用uint16 有些使用rt_bsse_t, 还有些采用int16_t，应该统一为rt_base_t。
2. 部分变量使用的数据类型明显超过其所需，例如enabled变量使用的是一个rt_uint32_t，但是这个变量只需要存储enable/disable二值即可，结果搞了个32位的整形。修改均是一些非重大影响，但是看起来非常难受的问题。影响到sensor框架重构。
3. 把不匹配的参数类型修改成正确的类型。具体来说把drv_gpio.c中下列函数的形参或返回值修改为跟rt_pin_ops操作方法中的成员形参与返回值一致。重新修改drv_gpio.c中的函数原型。

struct rt_pin_ops原型：

```
struct rt_pin_ops
{
    void (*pin_mode)(struct rt_device *device, rt_base_t pin, rt_uint8_t mode);
    void (*pin_write)(struct rt_device *device, rt_base_t pin, rt_uint8_t value);
    rt_int8_t  (*pin_read)(struct rt_device *device, rt_base_t pin);
    rt_err_t (*pin_attach_irq)(struct rt_device *device, rt_base_t pin,
            rt_uint8_t mode, void (*hdr)(void *args), void *args);
    rt_err_t (*pin_detach_irq)(struct rt_device *device, rt_base_t pin);
    rt_err_t (*pin_irq_enable)(struct rt_device *device, rt_base_t pin, rt_uint8_t enabled);
    rt_base_t (*pin_get)(const char *name);
};
```

将drv_gpio.c中下列函数形参或返回值改为与rt_pin_ops形参返回值类型一致，修改之后drv_gpio.c函数原型如下：

```
static void at32_pin_mode(rt_device_t dev, rt_base_t pin, rt_uint8_t mode)
static void at32_pin_write(rt_device_t dev, rt_base_t pin, rt_uint8_t value)
static rt_int8_t at32_pin_read(rt_device_t dev, rt_base_t pin)
static rt_err_t at32_pin_attach_irq(struct rt_device *device, rt_base_t pin,
                                    rt_uint8_t mode, void (*hdr)(void *args), void *args)
static rt_err_t at32_pin_dettach_irq(struct rt_device *device, rt_base_t pin)
static rt_err_t at32_pin_irq_enable(struct rt_device *device, rt_base_t pin,
                                    rt_uint8_t enabled)
static rt_base_t at32_pin_get(const char *name)
```

快速修改：

> static ***void***  (rt_device_t dev, rt_base_t pin, **rt_uint8_t** mode) 
> static ***void***  (rt_device_t dev, rt_base_t pin, **rt_uint8_t** value)
> static **rt_int8_t** (*rt_device_t dev, **rt_base_t** pin*)
> **rt_int8_t** *value* = PIN_LOW;
> static ***rt_err_t*** (struct rt_device \*device, **rt_base_t** pin,
>                                  **rt_uint8_t** mode, void (*hdr)(void *args), void *args)
> static ***rt_err_t*** (struct rt_device \*device, **rt_base_t** pin)
> static ***rt_err_t*** (struct rt_device \*device, rt_base_t pin,
>                                  **rt_uint8_t** enabled)

以此形成的第二个开源贡献成果如下：

> [[bsp\] fix mismatched function types in rt_pin_ops for all drv_gpio.c by Placebo27 · Pull Request #7457 · RT-Thread/rt-thread (github.com)](https://github.com/RT-Thread/rt-thread/pull/7457) 

**小插曲**

提交PR之后有个CI（Continuous Integration，持续集成）检测  **Check File Format and License / Scan code format and license** 不通过，原因是代码格式不规范，有些之前遗留下来的小问题比如空格之类的 。解决办法就是用官方的**源码格式自动化调整工具**跑一下。

> Formatting源码格式自动化调整工具：[mysterywolf/formatting: 源码格式自动化调整工具 (github.com)](https://github.com/mysterywolf/formatting) 

### Formatting 源码格式自动化调整工具

该文件会自动递归遍历**指定文件夹**下的所有文件或者**指定的文件**（默认对`.c`/`.h`/`.cpp`/`.hpp`，也可以改成你想要的文件类型）进行扫描：

- 将源文件编码统一为UTF-8
- 将TAB键替换为4空格
- 将每行末尾多余的空格删除，并统一换行符为'\n'
- 将RT-Thread版权信息的截至年份修改至今年(若文件不涉及此问题，程序会自动忽略)
- 将上海睿赛德版权信息的截至年份修改至今年(若文件不涉及此问题，程序会自动忽略)

**工作路径**

注意格式自动化调整工具的路径与所要遍历的文件路径之间的关系：

```
../rt-thread/
```

**部分遍历文件列表**

> 1. ../rt-thread/bsp/allwinner/libraries/drivers/drv_pin.c
> 2. ../rt-thread/bsp/apollo2/board/gpio.c
> 3. ../rt-thread/bsp/beaglebone/drivers/gpio.c
> 4. ../rt-thread/bsp/bouffalo_lab/libraries/rt_drivers/drv_gpio.c
> 5. ../rt-thread/bsp/essemi/es32f0654/drivers/drv_gpio.c
> 6. ../rt-thread/bsp/essemi/es32f369x/drivers/drv_gpio.c
> 7. ../rt-thread/bsp/fm33lc026/libraries/HAL_Drivers/drv_gpio.c
> 8. ../rt-thread/bsp/ft32/libraries/Drivers/drv_gpio.c
> 9. ../rt-thread/bsp/gd32/arm/libraries/gd32_drivers/drv_gpio.c
> 10. ../rt-thread/bsp/gd32/risc-v/libraries/gd32_drivers/drv_gpio.c
> 11. ../rt-thread/bsp/gd32105c-eval/drivers/drv_gpio.c
> 12. ../rt-thread/bsp/gd32107c-eval/drivers/drv_gpio.c
> 13. ../rt-thread/bsp/gd32303e-eval/drivers/drv_gpio.c
> 14. ../rt-thread/bsp/gd32350r-eval/drivers/drv_gpio.c
> 15. ../rt-thread/bsp/gd32e230k-start/drivers/drv_gpio.c
> 16. ../rt-thread/bsp/gd32vf103v-eval/drivers/drv_gpio.c
> 17. ../rt-thread/bsp/hc32/libraries/hc32_drivers/drv_gpio.c
> 18. ../rt-thread/bsp/hc32l136/drivers/drv_gpio.c
> 19. ../rt-thread/bsp/hc32l196/drivers/drv_gpio.c
> 20. ../rt-thread/bsp/hk32/libraries/rt_drivers/drv_gpio.c
> 21. ../rt-thread/bsp/hpmicro/libraries/drivers/drv_gpio.c

**人工判读**

bsp/loongson/ls1cdev/drivers/drv_gpio.c

**格式调整结果**

> **Commit：**[bsp] Formatting  Source code format

`git status`命令结果：

```bash
        modified:   bsp/hc32l136/drivers/drv_gpio.c
        modified:   bsp/mm32l3xx/drivers/drv_gpio.c
        modified:   bsp/rv32m1_vega/ri5cy/driver/drv_gpio.c
        modified:   bsp/smartfusion2/drivers/drv_gpio.c
```

