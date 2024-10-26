import logging
import os

class AutoSaveLogger:
    def __init__(self, filename, level=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)
        self.filename = filename

        # 创建文件处理器
        self.file_handler = logging.FileHandler(self.filename)
        self.file_handler.setLevel(level)
        selfformatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(selfformatter)

        # 创建控制台处理器
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(level)
        self.stream_handler.setFormatter(selfformatter)

        # 添加处理器到日志记录器
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)

    def get_logger(self):
        return self.logger

    def close_logger(self):
        self.file_handler.close()
        self.stream_handler.close()
        self.logger.removeHandler(self.file_handler)
        self.logger.removeHandler(self.stream_handler)

# 使用示例
if __name__ == "__main__":
    log_filename = 'auto_save_log.log'
    logger = AutoSaveLogger(log_filename)
    logger.get_logger().info('This is an info message')
    logger.get_logger().warning('This is a warning message')
    logger.get_logger().error('This is an error message')

    # 当你完成日志记录时，关闭日志处理器
    logger.close_logger()