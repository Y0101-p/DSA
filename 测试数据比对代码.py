import subprocess


def call_external_program(data, program_path):
    try:
        # 使用subprocess调用外部程序
        result = subprocess.run(
            ['python', program_path],  # 执行命令
            input=data,  # 输入数据
            capture_output=True,  # 捕获输出
            text=True,  # 以文本模式处理
            encoding='utf-8',  # 使用UTF-8编码
            shell=True  # 允许在Windows下直接执行
        )

        # 检查返回码
        if result.returncode == 0:
            return result.stdout
        else:
            return f"程序执行失败，错误信息：\n{result.stderr}"

    except Exception as e:
        return f"调用程序时发生错误：{str(e)}"


def main():

    program_path = r'C:\Users\10191\Code\openjudge\01961.py'
    file_path = r'C:\Users\10191\Code\data&solve\1961\a'
    with open(rf'{file_path}.in', 'r', encoding='utf-8') as f:
        data_in = f.read()
    with open(rf'{file_path}.out', 'r', encoding='utf-8') as f:
        data_out = f.read()
    output = call_external_program(data_in, program_path)
    output = output.split('\n')
    data_out = data_out.split('\n')
    if output == data_out:
        print(f'True')
    else:
        print(f'False')

        cnt = 0
        while True:
            if data_out[cnt] != output[cnt]:
                print(data_out[cnt], output[cnt], cnt)
                break
            cnt += 1

    r"""
    program_path = input('program_path: ')
    file_path = input('file_path: ')

    name_range = int(input('name_range: ')) + 1
    for i in range(1, name_range):
        if i < 10:
            name = f'00{i}'
        else:
            name = f'0{i}'
        with open(rf'{file_path}\{name}.in', 'r', encoding='utf-8') as f:
            data_in = f.read()
        with open(rf'{file_path}\{name}.out', 'r', encoding='utf-8') as f:
            data_out = f.read()
        output = call_external_program(data_in, program_path)
        if output == data_out:
            print(f'{i}:True')
        else:
            print(f'{i}:False')
            print(output)
            print(data_out)
            break
    """

if __name__ == '__main__':
    main()
