import os
import sublime, sublime_plugin


class GamyListingSwitchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # source file's path
        source_path = self.view.file_name()
        source_dir, source = os.path.split(source_path)

        # file path and extension
        file_name, file_extension = os.path.splitext(source)

        # Find target file
        target_file = None

        if file_extension == ".gms":
            target_file = os.path.join(source_dir, file_name+".lst")
            if not os.path.exists(target_file):
                target_file = os.path.join(source_dir, "LST")
                target_file = os.path.join(target_file, file_name+".lst")

        if file_extension == ".gmy":
            target_file = os.path.join(source_dir, file_name+".lst")
            if not os.path.exists(target_file):
                target_file = os.path.join(source_dir, "..", "LST", file_name+".gms")

        if file_extension == ".lst":
            target_file = os.path.join(source_dir, file_name+".gms")
            if not os.path.exists(target_file):
                target_file = os.path.join(source_dir, "..", file_name+".gms")

        if target_file and os.path.exists(target_file):
            self.view.window().open_file(target_file)


