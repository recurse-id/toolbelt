# import pulumi
#
# import asyncio
#
# # Import the Pulumi SDK and turn on test mode *before* allocating anything.
#
# pulumi.runtime.settings._set_test_mode_enabled(True)    # This should be able to be set via PULUMI_TEST_MODE
# pulumi.runtime.settings._set_project('spark-emr')
# pulumi.runtime.settings._set_stack('dev')
#
# ref = pulumi.StackReference(f"{pulumi.get_project(), pulumi.get_stack()}")
# master = ref.get_output(pulumi.Output.from_input("master_node")).future()
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.run_until_complete(master)
# loop.close()